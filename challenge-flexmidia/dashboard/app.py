"""
EDUBOT - Dashboard Interativo
Sprint 2 - Challenge FlexMedia

Dashboard Streamlit para visualização e análise
dos dados de interação do totem inteligente.
"""

import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import sqlite3
import joblib
import os
from datetime import datetime, timedelta

# Configuração da página
st.set_page_config(
    page_title="EDUBOT Dashboard",
    page_icon="🤖",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Caminhos
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
DB_PATH = os.path.join(SCRIPT_DIR, "..", "database", "totem.db")
MODEL_PATH = os.path.join(SCRIPT_DIR, "..", "ml_model", "model.pkl")


# ============================================
# Funções de Carregamento de Dados
# ============================================

@st.cache_data(ttl=300)
def load_data():
    """Carrega dados do banco SQLite."""
    try:
        conn = sqlite3.connect(DB_PATH)
        df = pd.read_sql_query("SELECT * FROM interacoes", conn)
        conn.close()
        
        df['timestamp'] = pd.to_datetime(df['timestamp'])
        df['data'] = df['timestamp'].dt.date
        df['hora'] = df['timestamp'].dt.hour
        df['dia_semana'] = df['timestamp'].dt.day_name()
        
        return df
    except Exception as e:
        st.error(f"Erro ao carregar dados: {e}")
        return pd.DataFrame()


@st.cache_resource
def load_model():
    """Carrega o modelo de ML."""
    try:
        if os.path.exists(MODEL_PATH):
            return joblib.load(MODEL_PATH)
        return None
    except Exception as e:
        st.warning(f"Modelo não encontrado: {e}")
        return None


# ============================================
# Funções de KPIs
# ============================================

def calculate_kpis(df):
    """Calcula KPIs principais."""
    total_interacoes = len(df)
    total_ativacoes = df['ativacao'].sum()
    taxa_ativacao = (total_ativacoes / total_interacoes * 100) if total_interacoes > 0 else 0
    
    df_ativos = df[df['ativacao'] == 1]
    tempo_medio = df_ativos['tempo_permanencia'].mean() if len(df_ativos) > 0 else 0
    
    interacoes_curtas = len(df_ativos[df_ativos['tipo_interacao'] == 'curto'])
    interacoes_longas = len(df_ativos[df_ativos['tipo_interacao'] == 'longo'])
    
    return {
        'total_interacoes': total_interacoes,
        'total_ativacoes': int(total_ativacoes),
        'taxa_ativacao': taxa_ativacao,
        'tempo_medio': tempo_medio,
        'interacoes_curtas': interacoes_curtas,
        'interacoes_longas': interacoes_longas
    }


# ============================================
# Componentes do Dashboard
# ============================================

def render_header():
    """Renderiza o cabeçalho."""
    col1, col2, col3 = st.columns([1, 3, 1])
    
    with col2:
        st.markdown("""
        <div style='text-align: center;'>
            <h1>🤖 EDUBOT Dashboard</h1>
            <p style='font-size: 1.2em; color: #666;'>
                Totem Inteligente Acessível para Ambientes Educacionais
            </p>
            <p style='color: #888;'>Sprint 2 - Challenge FlexMedia</p>
        </div>
        """, unsafe_allow_html=True)


def render_kpis(kpis):
    """Renderiza os KPIs principais."""
    st.markdown("### 📊 KPIs Principais")
    
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.metric(
            label="Total de Detecções",
            value=f"{kpis['total_interacoes']:,}",
            delta=None
        )
    
    with col2:
        st.metric(
            label="Ativações Efetivas",
            value=f"{kpis['total_ativacoes']:,}",
            delta=f"{kpis['taxa_ativacao']:.1f}% taxa"
        )
    
    with col3:
        st.metric(
            label="Tempo Médio",
            value=f"{kpis['tempo_medio']:.1f}s",
            delta=None
        )
    
    with col4:
        st.metric(
            label="Interações Longas",
            value=f"{kpis['interacoes_longas']:,}",
            delta=f"{kpis['interacoes_longas']/(kpis['interacoes_curtas']+kpis['interacoes_longas'])*100:.1f}%"
        )


def render_charts(df):
    """Renderiza os gráficos principais."""
    
    # Linha do tempo
    st.markdown("### 📈 Interações ao Longo do Tempo")
    
    daily = df.groupby('data').agg({
        'id': 'count',
        'ativacao': 'sum',
        'tempo_permanencia': 'mean'
    }).reset_index()
    daily.columns = ['data', 'total', 'ativacoes', 'tempo_medio']
    
    fig_timeline = make_subplots(
        rows=2, cols=1,
        subplot_titles=('Interações por Dia', 'Tempo Médio de Permanência'),
        vertical_spacing=0.15
    )
    
    fig_timeline.add_trace(
        go.Bar(x=daily['data'], y=daily['total'], name='Total', marker_color='#2196F3'),
        row=1, col=1
    )
    
    fig_timeline.add_trace(
        go.Scatter(x=daily['data'], y=daily['ativacoes'], name='Ativações', 
                  mode='lines+markers', line=dict(color='#4CAF50', width=2)),
        row=1, col=1
    )
    
    fig_timeline.add_trace(
        go.Scatter(x=daily['data'], y=daily['tempo_medio'], name='Tempo Médio',
                  mode='lines+markers', line=dict(color='#FF9800', width=2),
                  fill='tozeroy'),
        row=2, col=1
    )
    
    fig_timeline.update_layout(height=500, showlegend=True)
    st.plotly_chart(fig_timeline, use_container_width=True)
    
    # Gráficos lado a lado
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("### 🎯 Tipos de Interação")
        df_ativos = df[df['ativacao'] == 1]
        tipo_counts = df_ativos['tipo_interacao'].value_counts()
        
        fig_pie = px.pie(
            values=tipo_counts.values,
            names=tipo_counts.index,
            color_discrete_sequence=['#4CAF50', '#2196F3', '#FF9800'],
            hole=0.4
        )
        fig_pie.update_traces(textposition='inside', textinfo='percent+label')
        st.plotly_chart(fig_pie, use_container_width=True)
    
    with col2:
        st.markdown("### ⏰ Distribuição por Hora")
        hourly = df.groupby('hora').size().reset_index(name='count')
        
        fig_hourly = px.bar(
            hourly, x='hora', y='count',
            color='count',
            color_continuous_scale='Viridis'
        )
        fig_hourly.update_layout(
            xaxis_title="Hora do Dia",
            yaxis_title="Número de Interações",
            showlegend=False
        )
        st.plotly_chart(fig_hourly, use_container_width=True)


def render_heatmap(df):
    """Renderiza o heatmap de uso."""
    st.markdown("### 🗓️ Mapa de Calor - Uso por Dia e Hora")
    
    # Criar pivot table
    df['dia_semana_num'] = df['timestamp'].dt.dayofweek
    heatmap_data = df.groupby(['dia_semana_num', 'hora']).size().unstack(fill_value=0)
    
    dias = ['Segunda', 'Terça', 'Quarta', 'Quinta', 'Sexta', 'Sábado', 'Domingo']
    heatmap_data.index = [dias[i] for i in heatmap_data.index]
    
    fig_heatmap = px.imshow(
        heatmap_data,
        labels=dict(x="Hora", y="Dia da Semana", color="Interações"),
        color_continuous_scale='YlOrRd',
        aspect='auto'
    )
    
    fig_heatmap.update_layout(height=400)
    st.plotly_chart(fig_heatmap, use_container_width=True)


def render_table(df):
    """Renderiza a tabela de dados."""
    st.markdown("### 📋 Tabela de Interações")
    
    # Configurar colunas para exibição
    df_display = df[['timestamp', 'ativacao', 'tipo_interacao', 'tempo_permanencia', 'sessao_id']].copy()
    df_display['timestamp'] = df_display['timestamp'].dt.strftime('%Y-%m-%d %H:%M:%S')
    df_display.columns = ['Data/Hora', 'Ativação', 'Tipo', 'Tempo (s)', 'Sessão']
    
    # Paginação
    page_size = 20
    total_pages = len(df_display) // page_size + (1 if len(df_display) % page_size > 0 else 0)
    
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        page = st.selectbox("Página", range(1, total_pages + 1), key="page_selector")
    
    start_idx = (page - 1) * page_size
    end_idx = start_idx + page_size
    
    st.dataframe(
        df_display.iloc[start_idx:end_idx],
        use_container_width=True,
        hide_index=True
    )
    
    st.caption(f"Mostrando {start_idx + 1}-{min(end_idx, len(df_display))} de {len(df_display)} registros")


def render_ml_section(model_data, df):
    """Renderiza a seção de Machine Learning."""
    st.markdown("### 🤖 Modelo de Machine Learning")
    
    if model_data is None:
        st.warning("⚠️ Modelo não encontrado. Execute o treinamento primeiro.")
        st.code("python ml_model/train_model.py")
        return
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("#### 📊 Métricas do Modelo")
        
        metrics = model_data.get('metrics', {})
        model_name = model_data.get('model_name', 'Desconhecido')
        
        st.info(f"**Modelo:** {model_name}")
        
        metrics_df = pd.DataFrame({
            'Métrica': ['Acurácia', 'Precisão', 'Recall', 'F1-Score'],
            'Valor': [
                f"{metrics.get('accuracy', 0):.2%}",
                f"{metrics.get('precision', 0):.2%}",
                f"{metrics.get('recall', 0):.2%}",
                f"{metrics.get('f1_score', 0):.2%}"
            ]
        })
        
        st.dataframe(metrics_df, hide_index=True, use_container_width=True)
    
    with col2:
        st.markdown("#### 🔮 Teste de Predição")
        
        tempo = st.slider("Tempo de Permanência (s)", 10, 300, 60)
        hora = st.slider("Hora do Dia", 8, 22, 14)
        dia = st.selectbox("Dia da Semana", 
                          options=list(range(7)),
                          format_func=lambda x: ['Segunda', 'Terça', 'Quarta', 'Quinta', 'Sexta', 'Sábado', 'Domingo'][x])
        
        if st.button("🔍 Prever Tipo de Interação"):
            try:
                model = model_data['model']
                scaler = model_data['scaler']
                label_encoder = model_data['label_encoder']
                
                # Criar features
                horario_pico = 1 if (10 <= hora <= 14) or (18 <= hora <= 20) else 0
                fim_semana = 1 if dia >= 5 else 0
                
                features = np.array([[tempo, hora, dia, horario_pico, fim_semana]])
                features_scaled = scaler.transform(features)
                
                prediction = model.predict(features_scaled)
                prediction_label = label_encoder.inverse_transform(prediction)[0]
                
                if prediction_label == 'longo':
                    st.success(f"🎯 Predição: **{prediction_label.upper()}** (interação detalhada)")
                else:
                    st.info(f"🎯 Predição: **{prediction_label.upper()}** (consulta rápida)")
                    
            except Exception as e:
                st.error(f"Erro na predição: {e}")


def render_sidebar(df):
    """Renderiza a sidebar com filtros."""
    st.sidebar.markdown("## 🔧 Filtros")
    
    # Filtro de data
    min_date = df['timestamp'].min().date()
    max_date = df['timestamp'].max().date()
    
    date_range = st.sidebar.date_input(
        "Período",
        value=(min_date, max_date),
        min_value=min_date,
        max_value=max_date
    )
    
    # Filtro de tipo de interação
    tipos = ['Todos'] + list(df['tipo_interacao'].unique())
    tipo_selecionado = st.sidebar.selectbox("Tipo de Interação", tipos)
    
    # Filtro de ativação
    ativacao = st.sidebar.radio("Ativação", ['Todos', 'Sim', 'Não'])
    
    # Aplicar filtros
    df_filtered = df.copy()
    
    if len(date_range) == 2:
        df_filtered = df_filtered[
            (df_filtered['timestamp'].dt.date >= date_range[0]) &
            (df_filtered['timestamp'].dt.date <= date_range[1])
        ]
    
    if tipo_selecionado != 'Todos':
        df_filtered = df_filtered[df_filtered['tipo_interacao'] == tipo_selecionado]
    
    if ativacao == 'Sim':
        df_filtered = df_filtered[df_filtered['ativacao'] == 1]
    elif ativacao == 'Não':
        df_filtered = df_filtered[df_filtered['ativacao'] == 0]
    
    st.sidebar.markdown("---")
    st.sidebar.markdown(f"**Registros filtrados:** {len(df_filtered):,}")
    
    return df_filtered


# ============================================
# Função Principal
# ============================================

def main():
    """Função principal do dashboard."""
    
    # Carregar dados
    df = load_data()
    model_data = load_model()
    
    if df.empty:
        st.error("❌ Não foi possível carregar os dados. Verifique o banco de dados.")
        st.info("Execute os scripts na seguinte ordem:")
        st.code("""
        python sensors_simulation/simulated_sensors.py
        python database/init_db.py
        """)
        return
    
    # Renderizar sidebar e obter dados filtrados
    df_filtered = render_sidebar(df)
    
    # Renderizar componentes
    render_header()
    
    st.markdown("---")
    
    # KPIs
    kpis = calculate_kpis(df_filtered)
    render_kpis(kpis)
    
    st.markdown("---")
    
    # Tabs para organização
    tab1, tab2, tab3, tab4 = st.tabs(["📈 Gráficos", "🗓️ Heatmap", "📋 Dados", "🤖 ML"])
    
    with tab1:
        render_charts(df_filtered)
    
    with tab2:
        render_heatmap(df_filtered)
    
    with tab3:
        render_table(df_filtered)
    
    with tab4:
        render_ml_section(model_data, df_filtered)
    
    # Footer
    st.markdown("---")
    st.markdown("""
    <div style='text-align: center; color: #888;'>
        <p>EDUBOT Dashboard - Sprint 2 | Challenge FlexMedia | FIAP 2025</p>
        <p>Desenvolvido com ❤️ usando Streamlit e Plotly</p>
    </div>
    """, unsafe_allow_html=True)


if __name__ == "__main__":
    main()
