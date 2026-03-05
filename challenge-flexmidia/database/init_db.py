"""
EDUBOT - Inicialização do Banco de Dados SQLite
Sprint 3 - Challenge FlexMedia

Este script cria o banco de dados SQLite e a tabela de interações,
além de popular com os dados do CSV simulado.
"""
import sqlite3
import pandas as pd
import os

os.makedirs('challenge-flexmidia/database', exist_ok=True)
conn = sqlite3.connect('challenge-flexmidia/database/totem.db')
cursor = conn.cursor()

cursor.execute('DROP TABLE IF EXISTS interacoes')

cursor.execute('''
CREATE TABLE interacoes (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    session_id TEXT NOT NULL UNIQUE,
    timestamp DATETIME NOT NULL,
    status_ativacao INTEGER NOT NULL CHECK(status_ativacao IN (0, 1)),
    tipo_interacao TEXT NOT NULL CHECK(tipo_interacao IN ('curta', 'média', 'longa')),
    tempo_permanencia_seg INTEGER NOT NULL CHECK(tempo_permanencia_seg >= 0),
    toques_por_minuto INTEGER NOT NULL,
    velocidade_toques TEXT NOT NULL CHECK(velocidade_toques IN ('baixa', 'alta')),
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP
)
''')

# Lista de lugares onde o CSV pode ter se escondido
caminhos = [
    'challenge-flexmidia/sensors_simulation/edubot_sensor_data.csv',
    'edubot_sensor_data.csv',
    'sensors_simulation/edubot_sensor_data.csv'
]

# Tenta achar o arquivo em algum dos caminhos
csv_path = next((c for c in caminhos if os.path.exists(c)), None)

if csv_path:
    df = pd.read_csv(csv_path)
    df.to_sql('interacoes', conn, if_exists='append', index=False)
    print("============================================================")
    print("EDUBOT - Nova Inicialização do Banco de Dados")
    print("============================================================")
    print(f"✅ Banco de dados recriado com sucesso!")
    print(f"✅ {len(df)} registros inseridos a partir de: {csv_path}")
    print("\n📊 Resumo do que foi para o banco:")
    print(df['tipo_interacao'].value_counts())
    print("============================================================")
else:
    print("⚠️ CSV não encontrado em lugar nenhum! Tem certeza que o simulador rodou?")

conn.commit()
conn.close()