"""
EDUBOT - Simulador de Dados de Sensores (Streaming)
Sprint 3 - Challenge FlexMedia
"""
import random

def generate_sprint4_data(n=1500):
    status_opcoes = ["Focado", "Distraido", "Ausente"]
    data = []
    
    for _ in range(n):
        status_v = random.choice(status_opcoes)
        toques = round(random.uniform(5, 50), 2)
        
        # A lógica do "alvo" (tipo_interacao) agora é influenciada pela visão
        if status_v == "Focado" and toques > 20:
            tipo = "Longa (Alta Imersão)"
        elif status_v == "Distraido":
            tipo = "Curta (Superficial)"
        else:
            tipo = "Média"

        data.append({
            "toques_por_minuto": toques,
            "status_visao": status_v,
            "tipo_interacao": tipo
        })
    return data