import streamlit as st
import pandas as pd
import numpy as np
import joblib
import seaborn as sns
import matplotlib.pyplot as plt

# Importar nossa lógica de negócio (o arquivo regras_negocio.py)
# Isso mostra "Modularização" e organização de código
from regras_negocio import processar_dados_sensor

# Configuração da página (título e layout)
st.set_page_config(page_title="FarmTech Solutions - Fase 4", layout="wide")

# --- 1. CARREGAR O CÉREBRO DA IA ---


@st.cache_resource  # Isso faz o carregamento ser rápido
def carregar_modelo():
    try:
        return joblib.load('modelo_farmtech.joblib')
    except:
        st.error(
            "Erro: Arquivo 'modelo_farmtech.joblib' não encontrado. Rode a Etapa 2 primeiro.")
        return None


modelo = carregar_modelo()

# --- 2. BARRA LATERAL (SIMULAÇÃO DE SENSORES) ---
st.sidebar.header("📡 Painel de Controle (Sensores IoT)")
st.sidebar.markdown("Simule as condições do campo abaixo:")

# Inputs do usuário
cultura_selecionada = st.sidebar.selectbox("Cultura:", ["Soja", "Acai"])
umidade = st.sidebar.slider("💧 Umidade do Solo (%)", 0.0, 100.0, 60.0)
ph = st.sidebar.slider("🧪 pH do Solo", 0.0, 14.0, 6.5)
temperatura = st.sidebar.slider("🌡️ Temperatura (°C)", 0.0, 50.0, 25.0)
nutrientes = st.sidebar.slider("🌿 Nível de Nutrientes (0-10)", 0.0, 10.0, 5.0)

# Botão para processar
if st.sidebar.button("📊 Analisar Safra"):

    # --- 3. PREPARAÇÃO DOS DADOS PARA A IA ---
    # A IA precisa dos dados na mesma ordem que aprendeu:
    # ['Umidade_Solo', 'pH_Solo', 'Temperatura', 'Nivel_Nutrientes', 'Cultura_Soja']

    # Converter Cultura para número (Lógica do One-Hot Encoding)
    is_soja = 1 if cultura_selecionada == "Soja" else 0

    # Criar o DataFrame com UMA linha (os dados atuais)
    dados_entrada = pd.DataFrame({
        'Umidade_Solo': [umidade],
        'pH_Solo': [ph],
        'Temperatura': [temperatura],
        'Nivel_Nutrientes': [nutrientes],
        'Cultura_Soja': [is_soja]
    })

    # --- 4. PREVISÃO DA IA ---
    if modelo:
        previsao_rendimento = modelo.predict(dados_entrada)[0]
    else:
        previsao_rendimento = 0

    # --- 5. CONSULTAR O AGRÔNOMO DIGITAL (Regras de Negócio) ---
    alertas, acoes = processar_dados_sensor(
        cultura_selecionada, umidade, ph, temperatura, nutrientes)

    # --- 6. EXIBIÇÃO NA TELA PRINCIPAL ---

    # Cabeçalho
    st.title(f"🌱 Relatório de Análise: {cultura_selecionada}")
    st.markdown("---")

    # Colunas para organizar o visual
    col1, col2 = st.columns(2)

    with col1:
        st.subheader("🔮 Previsão de Produtividade")
        # Mostra o número grande (Métrica)
        st.metric(
            label="Rendimento Esperado (Ton/ha)",
            value=f"{previsao_rendimento:.2f}",
            delta="Baseado em IA"
        )

        # Barra de progresso visual para o rendimento
        # Assumindo que 35 ton/ha é um máximo teórico excelente para nosso exemplo
        progresso = min(previsao_rendimento / 35, 1.0)
        st.progress(progresso)

    with col2:
        st.subheader("📋 Diagnóstico & Recomendações")

        # Se não houver alertas, mostra sucesso
        if not alertas:
            st.success("✅ Tudo certo! Nenhuma ação crítica necessária.")
            for acao in acoes:
                st.info(acao)
        else:
            # Mostra alertas e ações corretivas
            for alerta in alertas:
                st.warning(alerta)
            for acao in acoes:
                st.error(f"🛠️ AÇÃO RECOMENDADA: {acao}")

    st.markdown("---")

    # --- 7. GRÁFICOS E INSIGHTS ---
    st.subheader("📈 Análise Comparativa (Base Histórica)")

    # Carregar os dados originais para mostrar gráficos
    try:
        df = pd.read_csv('dados_agricolas_farmtech.csv')

        # Filtrar apenas a cultura selecionada para o gráfico fazer sentido
        df_filtrado = df[df['Cultura'] == cultura_selecionada]

        fig, ax = plt.subplots(1, 2, figsize=(15, 5))

        # Gráfico 1: Dispersão (Umidade vs Rendimento)
        sns.scatterplot(data=df_filtrado, x='Umidade_Solo',
                        y='Rendimento_Colheita', ax=ax[0], color='green')
        ax[0].set_title(
            f"Impacto da Umidade no Rendimento ({cultura_selecionada})")
        # Desenhar uma linha vermelha onde está o sensor ATUAL
        ax[0].axvline(umidade, color='red', linestyle='--',
                      label='Sua Leitura Atual')
        ax[0].legend()

        # Gráfico 2: Dispersão (pH vs Rendimento)
        sns.scatterplot(data=df_filtrado, x='pH_Solo',
                        y='Rendimento_Colheita', ax=ax[1], color='orange')
        ax[1].set_title(f"Impacto do pH no Rendimento ({cultura_selecionada})")
        ax[1].axvline(ph, color='red', linestyle='--',
                      label='Sua Leitura Atual')
        ax[1].legend()

        st.pyplot(fig)

        st.caption(
            f"Os gráficos mostram 500 amostras históricas de {cultura_selecionada}. A linha vermelha indica a posição atual dos seus sensores.")

    except Exception as e:
        st.warning(
            "Não foi possível carregar os gráficos históricos. Verifique o arquivo CSV.")

else:
    # Tela inicial antes de clicar no botão
    st.title("🚜 FarmTech Solutions")
    st.markdown("""
    ### Bem-vindo ao Sistema de Apoio à Decisão
    
    Este dashboard utiliza **Inteligência Artificial** para prever a produtividade da sua lavoura 
    e sugerir ações de manejo em tempo real.
    
    **Como usar:**
    1. Ajuste os parâmetros dos sensores na barra lateral à esquerda.
    2. Clique em **'Analisar Safra'**.
    3. Receba previsões de rendimento e sugestões de correção de solo/irrigação.
    """)
    st.image("https://img.freepik.com/free-photo/smart-farming-with-iot-futuristic-agriculture-concept_53876-124626.jpg?w=1380", caption="Agricultura 4.0")
