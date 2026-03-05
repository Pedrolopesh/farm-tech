"""
EDUBOT - Modelo de Machine Learning
Sprint 3 - Challenge FlexMedia

Este script treina um modelo de classificação para prever
o tipo de interação (curto/longo) com base nos dados do totem.
"""
import sqlite3
import pandas as pd
import os
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report
import joblib

# Cria a pasta para salvar o modelo, se não existir
os.makedirs('challenge-flexmidia/ml_model', exist_ok=True)

print("📥 Carregando dados do banco SQLite para o ML...")
conn = sqlite3.connect('challenge-flexmidia/database/totem.db')
df = pd.read_sql_query("SELECT * FROM interacoes", conn)
conn.close()

# 1. Preparar os dados (Features e Target)
# Usaremos o tempo e a quantidade de toques para prever o tipo de interação
X = df[['tempo_permanencia_seg', 'toques_por_minuto']]
y = df['tipo_interacao']

# 2. Dividir os dados: 80% para treinar a IA, 20% para testar se ela aprendeu
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 3. Criar e treinar o modelo Random Forest
print("🤖 Treinando o modelo Random Forest...")
modelo = RandomForestClassifier(n_estimators=100, random_state=42)
modelo.fit(X_train, y_train)

# 4. Fazer previsões com os dados de teste e avaliar
y_pred = modelo.predict(X_test)
acuracia = accuracy_score(y_test, y_pred)

print(f"\n✅ Treinamento concluído!")
print(f"🎯 Acurácia do modelo: {acuracia * 100:.2f}%")
print("\n📊 Relatório de Classificação (Performance por categoria):")
print(classification_report(y_test, y_pred))

# 5. Salvar o modelo treinado para ser usado no Dashboard depois
caminho_modelo = 'challenge-flexmidia/ml_model/modelo_edubot.pkl'
joblib.dump(modelo, caminho_modelo)
print(f"\n💾 Modelo salvo com sucesso em: {caminho_modelo}")