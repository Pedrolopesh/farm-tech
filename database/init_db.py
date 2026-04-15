"""
EDUBOT - Inicialização do Banco Híbrido (Seed Data)
Sprint 4 - Challenge FlexMedia
"""
import sqlite3

def init_db():
    # Conecta ao banco de dados (será criado se não existir)
    conn = sqlite3.connect('database/totem.db')
    cursor = conn.cursor()
    
    # Resetando a tabela para a nova estrutura da Sprint 4 (Limpamos os dados antigos)
    cursor.execute('DROP TABLE IF EXISTS interacoes')
    
    # Criando a tabela interacoes (v4.0)
    # Esta estrutura permite consultas posteriores sobre comportamento e engajamento
    cursor.execute('''
    CREATE TABLE interacoes (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        timestamp DATETIME NOT NULL,
        session_id TEXT NOT NULL UNIQUE,
        
        -- Dados de Interação Física (Base da Sprint 3)
        tempo_permanencia_seg INTEGER NOT NULL,
        toques_por_minuto FLOAT NOT NULL,
        velocidade_toques TEXT NOT NULL,
        
        -- Dados de Visão Computacional Simulada (Objetivo 2 - Sprint 4)
        perfil_usuario TEXT NOT NULL,      -- Estudante, Professor, Visitante
        humor_estimado TEXT NOT NULL,      -- Focado, Distraído, Ausente
        presenca_detectada INTEGER DEFAULT 1,
        
        -- Mecanismos de Interação Digital (Objetivo 4 - Sprint 4)
        feedback_bot TEXT,                 -- Resposta automatizada gerada pelo sistema
        
        -- Controle e Classificação
        status_ativacao INTEGER DEFAULT 1,
        tipo_interacao TEXT NOT NULL       -- Target: Curta, Média, Longa (Previsto pela IA)
    )
    ''')
    
    conn.commit()
    conn.close()
    print("🚀 Banco de Dados configurado com sucesso para a Sprint 4!")

if __name__ == "__main__":
    init_db()