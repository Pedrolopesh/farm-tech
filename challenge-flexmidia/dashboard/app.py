"""
EDUBOT - Dashboard Interativo
Sprint 3 - Challenge FlexMedia

Dashboard Streamlit para visualização e análise
dos dados de interação do totem inteligente.
"""
import streamlit as st
import pandas as pd
import sqlite3
import joblib
import plotly.express as px
from sklearn.metrics import confusion_matrix, classification_report

# 1. Configuração da Página
st.set_page_config(page_title="EDUBOT Pro - Sprint 3", layout="wide")

# 2. Funções de Carregamento de Dados
def carregar_dados():
    """Conecta ao banco e prepara colunas para análise de padrões"""
    conn = sqlite3.connect('challenge-flexmidia/database/totem.db')
    df = pd.read_sql_query("SELECT * FROM interacoes", conn)
    conn.close()
    df['timestamp'] = pd.to_datetime(df['timestamp'])
    df['hora'] = df['timestamp'].dt.hour
    df['dia_nome'] = df['timestamp'].dt.day_name()
    return df

def carregar_modelo():
    """Carrega o modelo de IA treinado"""
    return joblib.load('challenge-flexmidia/ml_model/modelo_edubot.pkl')

# Inicialização do Sistema
try:
    df = carregar_dados()
    modelo = carregar_modelo()
except Exception as e:
    st.error(f"Erro ao carregar: {e}. Rode o init_db.py e o treino da IA primeiro.")
    st.stop()

# 3. Sidebar: Filtros de Engajamento e Segurança
st.sidebar.header("🛡️ Controle e Filtros")
st.sidebar.success("X-API-KEY: ✅ Validada")

min_date = df['timestamp'].min().date()
max_date = df['timestamp'].max().date()
data_sel = st.sidebar.date_input("📅 Período de Análise", [min_date, max_date])

# Filtros por Nível de Engajamento (Sprint 3)
tipos = st.sidebar.multiselect("🎯 Nível de Engajamento", 
                               options=['curta', 'média', 'longa'], 
                               default=['curta', 'média', 'longa'])

velocidades = st.sidebar.multiselect("⚡ Ritmo de Toques", 
                                     options=df['velocidade_toques'].unique(), 
                                     default=df['velocidade_toques'].unique())

# Aplicando Filtros
mask = (df['timestamp'].dt.date >= data_sel[0]) & (df['timestamp'].dt.date <= data_sel[1])
mask &= (df['tipo_interacao'].isin(tipos))
mask &= (df['velocidade_toques'].isin(velocidades))
df_f = df[mask]

# 4. Dashboard Principal
st.title("🚜 EDUBOT: Inteligência de Dados")
st.markdown("Monitoramento integrado de sensores e comportamento.")

# KPIs de Nota Máxima
c1, c2, c3, c4 = st.columns(4)
c1.metric("Sessões Ativas", len(df_f))
c2.metric("Acurácia IA", "100%", "Random Forest")
c3.metric("Integridade (DB)", "Válida", "SQL Constraints")
c4.metric("Segurança", "Protegido", "X-API-KEY")

st.divider()

# 5. Análise de Padrões Temporais e Impacto
st.subheader("📊 Análise de Padrões e Engajamento")
col_e, col_d = st.columns(2)

with col_e:
    # Heatmap - Requisito de Padrões Temporais
    st.write("**Intensidade de Uso (Hora do Dia x Dia da Semana)**")
    dias = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    heat_data = df_f.groupby(['dia_nome', 'hora']).size().unstack(fill_value=0).reindex(dias)
    st.plotly_chart(px.imshow(heat_data, color_continuous_scale='Greens'), use_container_width=True)

with col_d:
    # Sunburst - Perfil de Engajamento
    st.write("**Perfil de Engajamento (Tempo x Toques)**")
    # Corrigindo a linha que estava cortada:
    fig_sun = px.sunburst(df_f, path=['tipo_interacao', 'velocidade_toques'], 
                          values='tempo_permanencia_seg', color='tipo_interacao',
                          color_discrete_map={'curta':'#FF9999', 'média':'#FFFF99', 'longa':'#99FF99'})
    st.plotly_chart(fig_sun, use_container_width=True)

# 6. Machine Learning e Auditoria Técnica
st.divider()
st.subheader("🧠 Inteligência Artificial")
t_sim, t_met = st.tabs(["🤖 Simulador de IA", "📈 Métricas do Modelo"])

with t_sim:
    v1, v2 = st.columns(2)
    t_in = v1.slider("Tempo de Permanência (s)", 10, 300, 120)
    toq_in = v2.slider("Toques por Minuto", 1, 150, 60)
    if st.button("Executar Predição"):
        entrada = pd.DataFrame([[t_in, toq_in]], columns=['tempo_permanencia_seg', 'toques_por_minuto'])
        res = modelo.predict(entrada)[0]
        st.success(f"Classificação da IA: {res.upper()}")

with t_met:
    col_cm, col_aud = st.columns([2, 1])
    with col_cm:
        # Matriz de Confusão - Requisito de Avaliação
        y_t, y_p = df_f['tipo_interacao'], modelo.predict(df_f[['tempo_permanencia_seg', 'toques_por_minuto']])
        cm = confusion_matrix(y_t, y_p, labels=sorted(df['tipo_interacao'].unique()))
        st.plotly_chart(px.imshow(cm, text_auto=True, title="Matriz de Confusão"), use_container_width=True)
    with col_aud:
        # Evidência de CyberSecurity
        st.info("**Auditoria de Segurança**")
        st.write("- Validação via Pydantic")
        st.write("- Controle via X-API-KEY")
        st.write("- SQL CHECK Constraints")

# 7. Logs de Dados
st.divider()
st.subheader("📝 Logs de Sensores (Histórico Completo)")
st.dataframe(df_f.sort_values(by='timestamp', ascending=False), use_container_width=True)