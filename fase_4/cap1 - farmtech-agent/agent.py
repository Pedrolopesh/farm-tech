import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LinearRegression
from sklearn.pipeline import Pipeline
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
import numpy as np

# ==============================
# 1. Carregar o CSV
# ==============================
df = pd.read_csv("dados_agricolas.csv")

# Exemplo de features e targets
features = ["sensor_temp", "sensor_umidade", "sensor_ph", "irrigacao_ml", "fertilizacao_g"]

target_umidade = "sensor_umidade"
target_ph = "sensor_ph"
target_produtividade = "produtividade_kg"

# ==============================
# 2. Função genérica para treinar modelos
# ==============================
def treinando_modelo(target):
    X = df[features]
    y = df[target]

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )

    pipeline = Pipeline([
        ("scaler", StandardScaler()),
        ("model", LinearRegression())
    ])

    pipeline.fit(X_train, y_train)

    # Avaliação
    y_pred = pipeline.predict(X_test)

    mae = mean_absolute_error(y_test, y_pred)
    mse = mean_squared_error(y_test, y_pred)
    rmse = np.sqrt(mse)
    r2 = r2_score(y_test, y_pred)

    return pipeline, mae, mse, rmse, r2

# ==============================
# 3. Treinar modelos individuais
# ==============================
modelo_umidade, mae_u, mse_u, rmse_u, r2_u = treinando_modelo(target_umidade)
modelo_ph, mae_ph, mse_ph, rmse_ph, r2_ph = treinando_modelo(target_ph)
modelo_prod, mae_p, mse_p, rmse_p, r2_p = treinando_modelo(target_produtividade)

# ==============================
# 4. Exibir métricas
# ==============================
print("=== MODELO PARA UMIDADE DO SOLO ===")
print("MAE:", mae_u)
print("MSE:", mse_u)
print("RMSE:", rmse_u)
print("R²:", r2_u)

print("\n=== MODELO PARA pH ===")
print("MAE:", mae_ph)
print("MSE:", mse_ph)
print("RMSE:", rmse_ph)
print("R²:", r2_ph)

print("\n=== MODELO PARA PRODUTIVIDADE ===")
print("MAE:", mae_p)
print("MSE:", mse_p)
print("RMSE:", rmse_p)
print("R²:", r2_p)

# ==============================
# 5. Exemplo de previsão
# ==============================
novo_registro = pd.DataFrame([{
    "sensor_temp": 28,
    "sensor_umidade": 42,
    "sensor_ph": 6.2,
    "irrigacao_ml": 120,
    "fertilizacao_g": 15
}])

print("\nPrevisão Umidade:", modelo_umidade.predict(novo_registro)[0])
print("Previsão pH:", modelo_ph.predict(novo_registro)[0])
print("Previsão Produtividade:", modelo_prod.predict(novo_registro)[0])
