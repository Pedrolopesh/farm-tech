"""
EDUBOT - Simulador de Dados de Sensores (Streaming)
Sprint 3 - Challenge FlexMedia
"""
import random
import time
import uuid
import requests
from datetime import datetime

# Configuração da API
API_URL = "http://localhost:8000/api/sensores/interacao"
HEADERS = {"X-API-KEY": "flexmidia_secreta_2025"} # Autenticação
NUM_RECORDS = 50 # Quantos registros vamos simular agora

def simular_e_enviar():
    print("🚀 Iniciando o envio em tempo real para o EDUBOT...\n")
    
    sucessos = 0
    for i in range(NUM_RECORDS):
        tipo_interacao = random.choice(['curta', 'média', 'longa'])
        if tipo_interacao == 'curta':
            tempo_permanencia = random.randint(10, 60)
        elif tipo_interacao == 'média':
            tempo_permanencia = random.randint(61, 120)
        else:
            tempo_permanencia = random.randint(121, 300)

        # Montando o pacote JSON igual o ESP32 faria
        payload = {
            'session_id': str(uuid.uuid4()),
            'timestamp': datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
            'status_ativacao': 1,
            'tipo_interacao': tipo_interacao,
            'tempo_permanencia_seg': tempo_permanencia,
            'toques_por_minuto': random.randint(1, 120),
            'velocidade_toques': random.choice(['baixa', 'alta'])
        }

        try:
            # Enviando via POST para a FastAPI
            response = requests.post(API_URL, json=payload, headers=HEADERS)
            if response.status_code == 200:
                print(f"✅ Enviado: {tipo_interacao.upper()} | {tempo_permanencia}s | {payload['toques_por_minuto']} toques/min")
                sucessos += 1
            else:
                print(f"❌ Erro na API: {response.text}")
        except Exception as e:
            print("⚠️ API não está rodando. Ligue o servidor FastAPI primeiro!")
            break
            
        # Pequena pausa para fingir que é tempo real
        time.sleep(1)

    print(f"\n🎯 Simulação concluída! {sucessos}/{NUM_RECORDS} enviados com sucesso para o banco de dados.")

if __name__ == "__main__":
    simular_e_enviar()