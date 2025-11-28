# ============================================================
# FARMTECH SOLUTIONS – DASHBOARD FINAL (FASE 4)
# IA + Regressão Clássica + Análises Comparativas + Sugestões
# + Gráficos da Regressão Múltipla
# ============================================================

import streamlit as st
import pandas as pd
import numpy as np
import joblib
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score

from regras_negocio import processar_dados_sensor


st.set_page_config(page_title="FarmTech Solutions - Fase 4", layout="wide")
st.title("🚜 FarmTech Solutions – Agricultura Cognitiva")


# ------------------------------------------------------------
# CARREGAR DADOS E MODELO
# ------------------------------------------------------------
@st.cache_data
def carregar_dados():
    caminhos = [
        "./fase_4/cap1_farmtech_agent/dados_agricolas_farmtech.csv",
        "./dados_agricolas_farmtech.csv"
    ]
    for c in caminhos:
        try:
            return pd.read_csv(c)
        except:
            continue
    st.error("❌ Não encontrei 'dados_agricolas_farmtech.csv'.")
    return None


@st.cache_resource
def carregar_modelo():
    try:
        return joblib.load("./fase_4/cap1_farmtech_agent/modelo_farmtech.joblib")
    except:
        st.error("❌ Não encontrei 'modelo_farmtech.joblib'.")
        return None


df = carregar_dados()
modelo_ia = carregar_modelo()


# ------------------------------------------------------------
# REGRESSÃO CLÁSSICA
# ------------------------------------------------------------
def regressao_classica(df_cultura):

    features = ['Umidade_Solo', 'pH_Solo', 'Temperatura']
    target = 'Rendimento_Colheita'

    X = df_cultura[features]
    y = df_cultura[target]

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )

    model = LinearRegression()
    model.fit(X_train, y_train)
    y_pred = model.predict(X_test)

    return {
        "model": model,
        "mae": mean_absolute_error(y_test, y_pred),
        "mse": mean_squared_error(y_test, y_pred),
        "rmse": np.sqrt(mean_squared_error(y_test, y_pred)),
        "r2": r2_score(y_test, y_pred),
        "coefs": dict(zip(features, model.coef_)),
        "intercept": model.intercept_
    }


# ------------------------------------------------------------
# SIDEBAR – Inputs do usuário
# ------------------------------------------------------------
st.sidebar.header("📡 Sensores IoT (Simulação)")

cultura = st.sidebar.selectbox("Cultura", ["Soja", "Acai"])
umidade = st.sidebar.slider("💧 Umidade (%)", 0.0, 100.0, 60.0)
ph = st.sidebar.slider("🧪 pH do Solo", 0.0, 14.0, 6.5)
temperatura = st.sidebar.slider("🌡 Temperatura (°C)", 0.0, 50.0, 25.0)
nutrientes = st.sidebar.slider("🌿 Nutrientes", 0.0, 10.0, 5.0)

btn = st.sidebar.button("📊 Analisar Safra")


# ============================================================
# EXECUÇÃO DA ANÁLISE
# ============================================================
if btn:

    # Entrada p/ IA
    entrada = pd.DataFrame([{
        "Umidade_Solo": umidade,
        "pH_Solo": ph,
        "Temperatura": temperatura,
        "Nivel_Nutrientes": nutrientes,
        "Cultura_Soja": 1 if cultura == "Soja" else 0
    }])

    st.header(f"🌱 Relatório da Cultura: {cultura}")

    # ============================================================
    # PREVISÃO IA
    # ============================================================
    previsao_ia = modelo_ia.predict(entrada)[0]

    col1, col2 = st.columns(2)

    with col1:
        st.subheader("🔮 Previsão via IA (RandomForest)")
        st.metric("Rendimento Esperado (Ton/ha)", f"{previsao_ia:.2f}")
        st.progress(min(previsao_ia / 35, 1))

    alertas, acoes = processar_dados_sensor(cultura, umidade, ph, temperatura, nutrientes)

    with col2:
        st.subheader("📋 Diagnóstico & Recomendações")
        if not alertas:
            st.success("Nenhuma anomalia detectada.")
        else:
            for a in alertas:
                st.warning(a)
        for ac in acoes:
            st.info(f"👉 {ac}")

    # ============================================================
    # Análise Histórica
    # ============================================================
    st.markdown("---")
    st.subheader("📈 Histórico Real (Dataset)")

    df_c = df[df["Cultura"] == cultura]

    fig, ax = plt.subplots(1, 2, figsize=(15, 5))
    sns.scatterplot(df_c, x="Umidade_Solo", y="Rendimento_Colheita", ax=ax[0], color="green")
    ax[0].axvline(umidade, color="red", linestyle="--")

    sns.scatterplot(df_c, x="pH_Solo", y="Rendimento_Colheita", ax=ax[1], color="orange")
    ax[1].axvline(ph, color="red", linestyle="--")

    st.pyplot(fig)

    # ============================================================
    # REGRESSÃO CLÁSSICA + GRÁFICOS MULTIPLOS
    # ============================================================
    st.markdown("---")
    st.header("🔬 Regressão Linear Clássica (Comparativo Matemático)")

    resultados = regressao_classica(df_c)

    entrada_reg = entrada[['Umidade_Solo', 'pH_Solo', 'Temperatura']]
    previsao_reg = resultados["model"].predict(entrada_reg)[0]

    colA, colB = st.columns(2)
    with colA:
        st.metric("Previsão pela Regressão Linear", f"{previsao_reg:.2f}")

    with colB:
        st.metric("Diferença IA - Regressão", f"{previsao_ia - previsao_reg:.2f}")

    # Métricas
    colM1, colM2, colM3, colM4 = st.columns(4)
    colM1.metric("R²", f"{resultados['r2']:.3f}")
    colM2.metric("MAE", f"{resultados['mae']:.2f}")
    colM3.metric("MSE", f"{resultados['mse']:.2f}")
    colM4.metric("RMSE", f"{resultados['rmse']:.2f}")

    # ============================================================
    # GRÁFICOS DA REGRESSÃO MÚLTIPLA (NOVO)
    # ============================================================

    st.subheader("📉 Regressão Linear Múltipla (Gráficos Contínuos)")

    coef_u = resultados["coefs"]["Umidade_Solo"]
    coef_ph = resultados["coefs"]["pH_Solo"]
    coef_temp = resultados["coefs"]["Temperatura"]
    intercept = resultados["intercept"]

    # Geração das linhas da regressão
    um_array = np.linspace(df_c["Umidade_Solo"].min(), df_c["Umidade_Solo"].max(), 200)
    ph_array = np.linspace(df_c["pH_Solo"].min(), df_c["pH_Solo"].max(), 200)
    temp_array = np.linspace(df_c["Temperatura"].min(), df_c["Temperatura"].max(), 200)

    # Mantemos as outras variáveis fixas no valor do sensor
    y_umidade = intercept + coef_u * um_array + coef_ph * ph + coef_temp * temperatura
    y_ph = intercept + coef_u * umidade + coef_ph * ph_array + coef_temp * temperatura
    y_temp = intercept + coef_u * umidade + coef_ph * ph + coef_temp * temp_array

    fig2, ax = plt.subplots(1, 3, figsize=(22, 6))

    # Gráfico 1
    ax[0].scatter(df_c["Umidade_Solo"], df_c["Rendimento_Colheita"], color="gray", alpha=0.5)
    ax[0].plot(um_array, y_umidade, color="red")
    ax[0].set_title("Regressão Múltipla – Umidade vs Rendimento")

    # Gráfico 2
    ax[1].scatter(df_c["pH_Solo"], df_c["Rendimento_Colheita"], color="gray", alpha=0.5)
    ax[1].plot(ph_array, y_ph, color="blue")
    ax[1].set_title("Regressão Múltipla – pH vs Rendimento")

    # Gráfico 3
    ax[2].scatter(df_c["Temperatura"], df_c["Rendimento_Colheita"], color="gray", alpha=0.5)
    ax[2].plot(temp_array, y_temp, color="green")
    ax[2].set_title("Regressão Múltipla – Temperatura vs Rendimento")

    st.pyplot(fig2)


else:
    st.write("### Ajuste os sensores e clique em **Analisar Safra**.")
    st.image("https://img.freepik.com/free-photo/smart-farming-iot-concept_53876-124626.jpg")
