"""
EDUBOT - Simulador de Dados de Sensores do Totem
Sprint 2 - Challenge FlexMedia

Este script gera dados simulados das interações com o totem inteligente,
representando o comportamento dos sensores ESP32-CAM e interface de toque.
"""
import pandas as pd
import random
from datetime import datetime, timedelta
import uuid

# ==========================================
# Configurações Iniciais do Simulador EDUBOT
# ==========================================
NUM_RECORDS = 1500
START_DATE = datetime(2025, 10, 1, 8, 0, 0)
END_DATE = datetime(2026, 3, 2, 18, 0, 0)


def simular_dados_sensores(num_records, start_date, end_date):
    dados = []

    delta_total_segundos = int((end_date - start_date).total_seconds())
    segundos_aleatorios = [random.randint(0, delta_total_segundos) for _ in range(num_records)]
    timestamps = sorted([start_date + timedelta(seconds=s) for s in segundos_aleatorios])

    for ts in timestamps:
        session_id = str(uuid.uuid4())
        tipo_interacao = random.choice(['curta', 'média', 'longa'])

        if tipo_interacao == 'curta':
            tempo_permanencia = random.randint(10, 60)
        elif tipo_interacao == 'média':
            tempo_permanencia = random.randint(61, 120)
        else:  # longa
            tempo_permanencia = random.randint(121, 300)

        toques_por_minuto = random.randint(1, 120)
        velocidade_toques = random.choice(['baixa', 'alta'])
        status_ativacao = 1

        dados.append({
            'session_id': session_id,
            'timestamp': ts.strftime('%Y-%m-%d %H:%M:%S'),
            'status_ativacao': status_ativacao,
            'tipo_interacao': tipo_interacao,
            'tempo_permanencia_seg': tempo_permanencia,
            'toques_por_minuto': toques_por_minuto,
            'velocidade_toques': velocidade_toques
        })

    return pd.DataFrame(dados)


if __name__ == "__main__":
    df_sensores = simular_dados_sensores(NUM_RECORDS, START_DATE, END_DATE)

    print("Primeiros registros gerados:")
    print(df_sensores.head())
    print("\nResumo das interações geradas:")
    print(df_sensores['tipo_interacao'].value_counts())

    # Exportando o arquivo CSV
    df_sensores.to_csv('edubot_sensor_data.csv', index=False)
    print("\nArquivo 'edubot_sensor_data.csv' exportado com sucesso no mesmo diretório do script!")
