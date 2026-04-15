"""
EDUBOT - API de Integração Contínua (FastAPI)
Sprint 4 - Challenge FlexMedia
"""
from fastapi import FastAPI, Header, HTTPException
from pydantic import BaseModel
import sqlite3
import joblib
import pandas as pd

app = FastAPI(title="EDUBOT API - Sprint 4")

# Carregar o novo modelo v4 (sem data leakage)
model = joblib.load('ml_model/modelo_edubot_v4.pkl')

class Interacao(BaseModel):
    tempo_permanencia_seg: int
    toques_por_minuto: float
    status_visao: str  # "Focado", "Distraido", "Ausente"
    session_id: str

API_KEY_EXTERNA = "FLEXMEDIA123"

@app.post("/ingestao")
async def ingestao_dados(data: Interacao, x_api_key: str = Header(None)):
    # Validação de Segurança conforme feedback
    if x_api_key != API_KEY_EXTERNA:
        raise HTTPException(status_code=403, detail="Acesso não autorizado")

    # Predição em tempo real com a IA
    # Mapeamos o texto para o número que o modelo espera
    visao_map = {"Focado": 0, "Distraido": 1, "Ausente": 2}
    X_input = pd.DataFrame([[data.toques_por_minuto, 0, visao_map[data.status_visao]]], 
                           columns=['toques_por_minuto', 'perfil_n', 'humor_n'])
    
    predicao = model.predict(X_input)[0]

    # Salva no Banco de Dados
    conn = sqlite3.connect('database/totem.db')
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO interacoes (timestamp, session_id, tempo_permanencia_seg, toques_por_minuto, 
                                velocidade_toques, perfil_usuario, humor_estimado, tipo_interacao)
        VALUES (datetime('now'), ?, ?, ?, ?, ?, ?, ?)
    ''', (data.session_id, data.tempo_permanencia_seg, data.toques_por_minuto, 
          'alta' if data.toques_por_minuto > 20 else 'lenta', 
          'Visitante', data.status_visao, predicao))
    
    conn.commit()
    conn.close()
    
    return {"status": "sucesso", "perfil_detectado": predicao}