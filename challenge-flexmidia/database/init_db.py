"""
EDUBOT - Inicialização do Banco Híbrido (Seed Data)
Sprint 3 - Challenge FlexMedia
"""
import sqlite3
import pandas as pd
import os

os.makedirs('challenge-flexmidia/database', exist_ok=True)
conn = sqlite3.connect('challenge-flexmidia/database/totem.db')
cursor = conn.cursor()

print("🗃️ Resetando e criando tabela estruturada...")
cursor.execute('DROP TABLE IF EXISTS interacoes')

# Criação da tabela com tipagem forte (Requisito da Sprint 3)
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

# --- CARGA INICIAL (SEED DATA) ---
print("📥 Buscando histórico de dados (CSV) para carga inicial...")
caminhos = [
    'challenge-flexmidia/sensors_simulation/edubot_sensor_data.csv',
    'edubot_sensor_data.csv',
    'sensors_simulation/edubot_sensor_data.csv'
]

csv_path = next((c for c in caminhos if os.path.exists(c)), None)

if csv_path:
    df = pd.read_csv(csv_path)
    df.to_sql('interacoes', conn, if_exists='append', index=False)
    print(f"✅ Sucesso! {len(df)} registros históricos inseridos do CSV.")
else:
    print("⚠️ CSV não encontrado. O banco começará vazio.")

conn.commit()
conn.close()
print("🚀 Banco de dados pronto! Agora inicie a API (main.py).")