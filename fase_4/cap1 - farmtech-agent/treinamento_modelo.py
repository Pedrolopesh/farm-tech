import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
import joblib  # Biblioteca para salvar o modelo treinado

# 1. Carregar os dados
print("Carregando dados...")
df = pd.read_csv('dados_agricolas_farmtech.csv')

# 2. Tratamento de Dados (One-Hot Encoding)
# Transformando "Soja/Acai" em números
df_encoded = pd.get_dummies(df, columns=['Cultura'], drop_first=True)

# 3. Separar Variáveis e Alvo
X = df_encoded.drop('Rendimento_Colheita', axis=1)
y = df_encoded['Rendimento_Colheita']

# 4. Dividir em Treino e Teste
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42)

# 5. Treinar o Modelo
print("Treinando IA (Random Forest)...")
modelo = RandomForestRegressor(n_estimators=100, random_state=42)
modelo.fit(X_train, y_train)

# 6. Avaliar o Modelo
y_pred = modelo.predict(X_test)
mae = mean_absolute_error(y_test, y_pred)
rmse = np.sqrt(mean_squared_error(y_test, y_pred))
r2 = r2_score(y_test, y_pred)

print(f"\n--- Resultados do Treinamento ---")
print(f"R² (Precisão): {r2:.2f}")
print(f"RMSE (Erro médio): {rmse:.2f}")

# 7. SALVAR O MODELO (Parte Nova e Importante!)
# Salvamos o modelo treinado para não precisar treinar toda vez que abrir o site
joblib.dump(modelo, 'modelo_farmtech.joblib')
print("\n✅ Modelo salvo como 'modelo_farmtech.joblib'!")
