import sqlite3
import pandas as pd
import uuid
import random
from datetime import datetime, timedelta
import os

def reset_and_load():
    db_path = 'database/totem.db'
    
    # 1. Garante que a pasta database existe
    if not os.path.exists('database'):
        os.makedirs('database')

    # 2. Conecta e Reinicia o Banco
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    cursor.execute('DROP TABLE IF EXISTS interacoes')
    
    # Criando a tabela com as colunas da Sprint 4 (IA Visual e Interacao)
    cursor.execute('''
    CREATE TABLE interacoes (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        timestamp DATETIME,
        session_id TEXT UNIQUE,
        tempo_permanencia_seg INTEGER,
        toques_por_minuto FLOAT,
        velocidade_toques TEXT,
        perfil_usuario TEXT,
        humor_estimado TEXT,
        presenca_detectada INTEGER,
        tipo_interacao TEXT
    )
    ''')

    # 3. Geracao de 1500 registros com ruido (Objetivo 2 e 5)
    perfis = ['Estudante', 'Professor', 'Visitante']
    humores = ['Focado', 'Distraido', 'Ausente']
    data = []
    base_time = datetime(2025, 1, 1)

    for i in range(1500):
        tpm = round(random.uniform(5, 50), 2)
        humor = random.choice(humores)
        perfil = random.choice(perfis)
        
        # Logica com ruido para evitar 100% de acuracia no ML (Objetivo 3)
        if random.random() < 0.15:
            tipo = random.choice(['curta', 'media', 'longa'])
        else:
            if humor == "Focado" and tpm > 25: tipo = "longa"
            elif humor == "Distraido": tipo = "curta"
            else: tipo = "media"

        data.append({
            'timestamp': (base_time + timedelta(minutes=i*10)).strftime('%Y-%m-%d %H:%M:%S'),
            'session_id': str(uuid.uuid4()),
            'tempo_permanencia_seg': random.randint(10, 300),
            'toques_por_minuto': tpm,
            'velocidade_toques': 'alta' if tpm > 20 else 'lenta',
            'perfil_usuario': perfil,
            'humor_estimado': humor,
            'presenca_detectada': 1,
            'tipo_interacao': tipo
        })

    # 4. Salvando e confirmando
    df = pd.DataFrame(data)
    df.to_sql('interacoes', conn, if_exists='append', index=False)
    conn.commit()
    
    cursor.execute('SELECT COUNT(*) FROM interacoes')
    total = cursor.fetchone()[0]
    conn.close()
    
    print(f"SUCESSO: Banco populado com {total} registros.")

if __name__ == "__main__":
    reset_and_load()