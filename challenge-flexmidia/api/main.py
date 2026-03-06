"""
EDUBOT - API de Integração Contínua (FastAPI)
Sprint 3 - Challenge FlexMedia
"""
from fastapi import FastAPI, HTTPException, Header, Depends
from pydantic import BaseModel, Field
from datetime import datetime
import sqlite3
import os

app = FastAPI(title="EDUBOT API", description="API para recebimento de dados dos sensores")

# Chave de segurança simulada (Requisito de Cognitive CyberSecurity)
API_KEY_SECRETA = "flexmidia_secreta_2025"

# Validando os dados recebidos (Pydantic garante a integridade)
class InteracaoSensor(BaseModel):
    session_id: str
    timestamp: str
    status_ativacao: int = Field(..., ge=0, le=1)
    tipo_interacao: str
    tempo_permanencia_seg: int = Field(..., ge=0)
    toques_por_minuto: int = Field(..., ge=0)
    velocidade_toques: str

def verificar_api_key(x_api_key: str = Header(None)):
    if x_api_key != API_KEY_SECRETA:
        raise HTTPException(status_code=401, detail="Acesso Negado. API Key inválida.")
    return x_api_key

@app.post("/api/sensores/interacao")
def registrar_interacao(dados: InteracaoSensor, api_key: str = Depends(verificar_api_key)):
    """Recebe dados do ESP32/Simulador e injeta direto no SQLite"""
    try:
        db_path = 'challenge-flexmidia/database/totem.db'
        conn = sqlite3.connect(db_path)
        cursor = conn.cursor()
        
        # Inserindo no banco em tempo real
        cursor.execute('''
            INSERT INTO interacoes 
            (session_id, timestamp, status_ativacao, tipo_interacao, tempo_permanencia_seg, toques_por_minuto, velocidade_toques)
            VALUES (?, ?, ?, ?, ?, ?, ?)
        ''', (
            dados.session_id, dados.timestamp, dados.status_ativacao, dados.tipo_interacao,
            dados.tempo_permanencia_seg, dados.toques_por_minuto, dados.velocidade_toques
        ))
        conn.commit()
        conn.close()
        return {"status": "sucesso", "mensagem": "Dados gravados no banco!", "session_id": dados.session_id}
        
    except sqlite3.IntegrityError:
        raise HTTPException(status_code=400, detail="Erro de integridade: session_id duplicado.")
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Erro interno: {str(e)}")