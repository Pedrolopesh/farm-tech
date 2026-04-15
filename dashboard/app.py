"""
EDUBOT - Dashboard Interativo
Sprint 4 - Challenge FlexMedia

Dashboard Streamlit para visualização e análise
dos dados de interação do totem inteligente.
"""
import streamlit as st
import pandas as pd
import sqlite3
import joblib
import plotly.express as px
import os

st.set_page_config(page_title="EDUBOT - Dashboard Final", layout="wide")

@st.cache_resource
def load_assets():
    model = joblib.load('ml_model/modelo_edubot_v4.pkl') if os.path.exists('ml_model/modelo_edubot_v4.pkl') else None
    conn = sqlite3.connect('database/totem.db')
    df = pd.read_sql("SELECT * FROM interacoes", conn)
    conn.close()
    return model, df

model, df_hist = load_assets()

# --- SIDEBAR: SIMULAÇÃO IA ---
with st.sidebar:
    st.header("📸 IA Visual (Simulada)")
    perf = st.selectbox("Perfil:", ["Estudante", "Professor", "Visitante"])
    humo = st.selectbox("Humor:", ["Focado", "Distraido", "Ausente"])
    toq = st.slider("Intensidade (TPM):", 0, 60, 25)
    
    if model:
        p_n, h_n = {"Estudante":0,"Professor":1,"Visitante":2}[perf], {"Focado":0,"Distraido":1,"Ausente":2}[humo]
        pred = model.predict([[toq, p_n, h_n]])[0]
        st.success(f"Engajamento Previsto: {pred.upper()}")

st.title("🤖 EDUBOT: Inteligência & Big Data")
t1, t2 = st.tabs(["💬 Interação Digital", "📈 Métricas & Padrões (KPIs)"])

# TAB 1: CHATBOT (Objetivos 1 e 4)
with t1:
    if "messages" not in st.session_state: st.session_state.messages = []
    for m in st.session_state.messages:
        with st.chat_message(m["role"]): st.markdown(m["content"])

    prompt = st.chat_input("Fale com o totem...")
    if prompt:
        st.session_state.messages.append({"role": "user", "content": prompt})
        with st.chat_message("user"): st.markdown(prompt)
        
        with st.chat_message("assistant"):
            resp = f"Olá {perf}! Identifiquei seu humor como {humo}. "
            resp += "Estou preparando um conteúdo denso para você!" if pred == "longa" else "Aqui está um resumo rápido!"
            st.markdown(resp)
            st.session_state.messages.append({"role": "assistant", "content": resp})

# TAB 2: MÉTRICAS E BIG DATA (Objetivo 5)
with t2:
    # 1. KPIs de Uso
    c1, c2, c3 = st.columns(3)
    total = len(df_hist)
    sucesso = (len(df_hist[df_hist['tipo_interacao'] != 'curta']) / total) * 100
    c1.metric("Total de Sessões", total)
    c2.metric("Público mais Frequente", df_hist['perfil_usuario'].mode()[0])
    c3.metric("Taxa de Sucesso (IA)", f"{sucesso:.1f}%")

    # 2. Frequência de Acesso (Timeline)
    st.subheader("📅 Volume de Dados Tratados (Timeline)")
    df_hist['timestamp'] = pd.to_datetime(df_hist['timestamp'])
    df_timeline = df_hist.resample('D', on='timestamp').count()['session_id'].reset_index()
    fig_line = px.line(df_timeline, x='timestamp', y='session_id', title="Acessos por Dia (Big Data Simulation)")
    st.plotly_chart(fig_line, use_container_width=True)

    # 3. Visualização de Padrões (Sunburst)
    st.subheader("🌀 Padrões de Comportamento")
    fig_sun = px.sunburst(df_hist, path=['perfil_usuario', 'humor_estimado', 'tipo_interacao'], color='tipo_interacao')
    st.plotly_chart(fig_sun, use_container_width=True)