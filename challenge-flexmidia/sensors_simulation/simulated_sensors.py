"""
EDUBOT - Simulador de Dados de Sensores do Totem
Sprint 2 - Challenge FlexMedia

Este script gera dados simulados das interações com o totem inteligente,
representando o comportamento dos sensores ESP32-CAM e interface de toque.
"""

import pandas as pd
import numpy as np
from datetime import datetime, timedelta
import uuid
import os

# Configurações da simulação
NUM_RECORDS = 200
START_DATE = datetime(2025, 10, 1, 8, 0, 0)  # Início do semestre letivo
END_DATE = datetime(2025, 11, 28, 18, 0, 0)   # Data atual

# Seed para reprodutibilidade
np.random.seed(42)


def generate_timestamp(start: datetime, end: datetime, n: int) -> list:
    """
    Gera timestamps aleatórios dentro do período especificado.
    Considera horários de funcionamento típicos (8h às 22h).
    """
    timestamps = []
    delta = end - start
    
    for _ in range(n):
        # Gera data aleatória
        random_days = np.random.randint(0, delta.days)
        base_date = start + timedelta(days=random_days)
        
        # Horário de funcionamento (8h às 22h)
        random_hour = np.random.randint(8, 22)
        random_minute = np.random.randint(0, 60)
        random_second = np.random.randint(0, 60)
        
        timestamp = base_date.replace(
            hour=random_hour,
            minute=random_minute,
            second=random_second
        )
        timestamps.append(timestamp)
    
    return sorted(timestamps)


def generate_interaction_type() -> str:
    """
    Gera tipo de interação com distribuição realista.
    - curto: consultas rápidas (60%)
    - longo: interações detalhadas (40%)
    """
    return np.random.choice(['curto', 'longo'], p=[0.6, 0.4])


def generate_permanence_time(interaction_type: str) -> int:
    """
    Gera tempo de permanência em segundos baseado no tipo de interação.
    - curto: 10-60 segundos
    - longo: 60-300 segundos
    """
    if interaction_type == 'curto':
        return np.random.randint(10, 61)
    else:
        return np.random.randint(60, 301)


def generate_session_id() -> str:
    """
    Gera ID único de sessão.
    """
    return str(uuid.uuid4())[:8]


def generate_activation() -> int:
    """
    Gera status de ativação do sensor.
    95% das detecções resultam em ativação (interação efetiva).
    """
    return np.random.choice([0, 1], p=[0.05, 0.95])


def simulate_sensor_data() -> pd.DataFrame:
    """
    Função principal que gera o dataset completo de sensores simulados.
    """
    print("🚀 Iniciando simulação de dados do EDUBOT...")
    
    # Gerar timestamps
    timestamps = generate_timestamp(START_DATE, END_DATE, NUM_RECORDS)
    
    data = []
    
    for ts in timestamps:
        ativacao = generate_activation()
        
        if ativacao == 1:
            tipo_interacao = generate_interaction_type()
            tempo_permanencia = generate_permanence_time(tipo_interacao)
        else:
            # Se não houve ativação, registra como detecção sem interação
            tipo_interacao = 'nenhuma'
            tempo_permanencia = 0
        
        sessao_id = generate_session_id()
        
        data.append({
            'timestamp': ts,
            'ativacao': ativacao,
            'tipo_interacao': tipo_interacao,
            'tempo_permanencia': tempo_permanencia,
            'sessao_id': sessao_id
        })
    
    df = pd.DataFrame(data)
    
    print(f"✅ {len(df)} registros gerados com sucesso!")
    print(f"\n📊 Estatísticas do Dataset:")
    print(f"   - Total de ativações: {df['ativacao'].sum()}")
    print(f"   - Taxa de ativação: {df['ativacao'].mean()*100:.1f}%")
    print(f"   - Interações curtas: {len(df[df['tipo_interacao'] == 'curto'])}")
    print(f"   - Interações longas: {len(df[df['tipo_interacao'] == 'longo'])}")
    print(f"   - Tempo médio de permanência: {df[df['ativacao'] == 1]['tempo_permanencia'].mean():.1f}s")
    
    return df


def save_to_csv(df: pd.DataFrame, filepath: str):
    """
    Salva o DataFrame em arquivo CSV.
    """
    df.to_csv(filepath, index=False)
    print(f"\n💾 Dataset salvo em: {filepath}")


if __name__ == "__main__":
    # Gerar dados
    df = simulate_sensor_data()
    
    # Definir caminho do arquivo
    script_dir = os.path.dirname(os.path.abspath(__file__))
    csv_path = os.path.join(script_dir, "simulated_sensors.csv")
    
    # Salvar CSV
    save_to_csv(df, csv_path)
    
    # Mostrar amostra dos dados
    print("\n📋 Amostra dos dados gerados:")
    print(df.head(10).to_string(index=False))
