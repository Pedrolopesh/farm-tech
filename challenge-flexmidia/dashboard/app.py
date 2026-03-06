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

st.set_page_config(page_title="EDUBOT Pro", layout="wide")

def carregar_dados():
    conn = sqlite3.connect('challenge-flexmidia/database/totem.db')
    df = pd.read_sql_query("SELECT * FROM interacoes", conn)
    conn.close()
    df['timestamp'] = pd.to_datetime(df['timestamp'])
    return df

def carregar_modelo():
    return joblib.load('challenge-flexmidia/ml_model/modelo_edubot.pkl')

df = carregar_dados()
modelo = carregar_modelo()

# --- SIDEBAR COM FILTROS AVANÇADOS ---
st.sidebar.header("⚙️ Filtros Avançados")

# 1. Filtro de Data
min_date = df['timestamp'].min().date()
max_date = df['timestamp'].max().date()
data_selecionada = st.sidebar.date_input("Período de Análise", [min_date, max_date])

# 2. Filtro de Tipo de Interação
tipos = st.sidebar.multiselect("Tipo de Interação", options=df['tipo_interacao'].unique(), default=df['tipo_interacao'].unique())

# 3. Filtro de Velocidade de Toque
velocidades = st.sidebar.multiselect("Velocidade de Toques", options=df['velocidade_toques'].unique(), default=df['velocidade_toques'].unique())

# 4. Filtro de Status (Ativado/Desativado)
status = st.sidebar.radio("Status do Totem", ["Todos", "Ativado (1)", "Desativado (0)"])

# --- APLICANDO OS FILTROS ---
mask = (df['timestamp'].dt.date >= data_selecionada[0]) & (df['timestamp'].dt.date <= data_selecionada[1])
mask &= (df['tipo_interacao'].isin(tipos))
mask &= (df['velocidade_toques'].isin(velocidades))

if status != "Todos":
    val_status = 1 if "Ativado" in status else 0
    mask &= (df['status_ativacao'] == val_status)

df_filtrado = df[mask]

# --- DASHBOARD ---
st.title("🚜 EDUBOT")
st.markdown(f"Exibindo **{len(df_filtrado)}** de {len(df)} registros totais.")

# KPIs
c1, c2, c3, c4 = st.columns(4)
c1.metric("Sessões Filtradas", len(df_filtrado))
c2.metric("Tempo Médio", f"{df_filtrado['tempo_permanencia_seg'].mean():.1f}s")
c3.metric("Toques Médios", f"{df_filtrado['toques_por_minuto'].mean():.1f}")
c4.metric("Engajamento Alto (%)", f"{(len(df_filtrado[df_filtrado['velocidade_toques']=='alta'])/len(df_filtrado)*100 if len(df_filtrado)>0 else 0):.1f}%")

st.divider()

col_esq, col_dir = st.columns(2)

with col_esq:
    st.subheader("📅 Interações ao longo do tempo")
    # Agrupa por dia para ver o volume
    df_timeline = df_filtrado.set_index('timestamp').resample('D').size().reset_index(name='contagem')
    fig_time = px.line(df_timeline, x='timestamp', y='contagem', title="Volume Diário de Interações", line_shape="spline")
    st.plotly_chart(fig_time, use_container_width=True)

with col_dir:
    st.subheader("🎯 Perfil de Engajamento")
    fig_sun = px.sunburst(df_filtrado, path=['tipo_interacao', 'velocidade_toques'], values='tempo_permanencia_seg',
                          color='tipo_interacao', color_discrete_map={'curta':'#FF9999', 'média':'#FFFF99', 'longa':'#99FF99'})
    st.plotly_chart(fig_sun, use_container_width=True)

# --- MACHINE LEARNING ---
st.divider()
st.subheader("🧠 Predição de Comportamento com IA")

with st.expander("🤖 Testar Inteligência Artificial do EDUBOT", expanded=True):
    st.write("Ajuste os valores abaixo para ver como a IA classifica o engajamento do produtor:")

    ml_c1, ml_c2 = st.columns(2)

    with ml_c1:
        # Criamos sliders para facilitar o teste no vídeo
        t_input = st.slider("Tempo de Permanência (segundos)", 10, 300, 120)
    with ml_c2:
        toq_input = st.slider("Toques por Minuto", 1, 150, 60)

    # O botão que aciona o modelo .pkl
    if st.button("Executar Predição do Modelo"):
        # Preparamos os dados no formato que o Random Forest espera
        entrada = pd.DataFrame([[t_input, toq_input]],
                               columns=['tempo_permanencia_seg', 'toques_por_minuto'])

        # Fazemos a predição
        predicao = modelo.predict(entrada)[0]

        # Mostramos o resultado com cores diferentes para cada tipo
        cores = {"curta": "orange", "média": "blue", "longa": "green"}
        cor_resultado = cores.get(predicao, "gray")

        st.markdown(f"### Resultado da IA: :{cor_resultado}[Interação {predicao.upper()}]")
        st.info("O modelo analisou os padrões de tempo e frequência de toques para chegar a este veredito.")

# --- TABELA DE DADOS ---
st.divider()
st.subheader("📝 Dados Brutos (Logs de Sensores)")
st.dataframe(df_filtrado.sort_values(by='timestamp', ascending=False), use_container_width=True)