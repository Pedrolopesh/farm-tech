"""
EDUBOT - Inicialização do Banco de Dados SQLite
Sprint 2 - Challenge FlexMedia

Este script cria o banco de dados SQLite e a tabela de interações,
além de popular com os dados do CSV simulado.
"""

import sqlite3
import pandas as pd
import os
from datetime import datetime


# Caminhos dos arquivos
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
DB_PATH = os.path.join(SCRIPT_DIR, "totem.db")
CSV_PATH = os.path.join(SCRIPT_DIR, "..", "sensors_simulation", "simulated_sensors.csv")


def create_database():
    """
    Cria o banco de dados SQLite e a tabela de interações.
    """
    print("🗃️  Criando banco de dados SQLite...")
    
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    
    # Criar tabela de interações
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS interacoes (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            timestamp DATETIME NOT NULL,
            ativacao INTEGER NOT NULL CHECK(ativacao IN (0, 1)),
            tipo_interacao TEXT NOT NULL CHECK(tipo_interacao IN ('curto', 'longo', 'nenhuma')),
            tempo_permanencia INTEGER NOT NULL CHECK(tempo_permanencia >= 0),
            sessao_id TEXT NOT NULL UNIQUE,
            created_at DATETIME DEFAULT CURRENT_TIMESTAMP
        )
    """)
    
    # Criar índices para otimização de consultas
    cursor.execute("""
        CREATE INDEX IF NOT EXISTS idx_timestamp ON interacoes(timestamp)
    """)
    
    cursor.execute("""
        CREATE INDEX IF NOT EXISTS idx_tipo_interacao ON interacoes(tipo_interacao)
    """)
    
    cursor.execute("""
        CREATE INDEX IF NOT EXISTS idx_ativacao ON interacoes(ativacao)
    """)
    
    conn.commit()
    conn.close()
    
    print(f"✅ Banco de dados criado em: {DB_PATH}")


def load_csv_to_database():
    """
    Carrega os dados do CSV simulado para o banco de dados.
    """
    print("\n📥 Carregando dados do CSV para o banco...")
    
    # Verificar se o CSV existe
    if not os.path.exists(CSV_PATH):
        print(f"❌ Arquivo CSV não encontrado: {CSV_PATH}")
        print("   Execute primeiro: python sensors_simulation/simulated_sensors.py")
        return False
    
    # Ler CSV
    df = pd.read_csv(CSV_PATH)
    print(f"   - {len(df)} registros encontrados no CSV")
    
    # Conectar ao banco
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    
    # Limpar dados existentes (para permitir re-execução)
    cursor.execute("DELETE FROM interacoes")
    
    # Inserir dados
    inserted = 0
    errors = 0
    
    for _, row in df.iterrows():
        try:
            cursor.execute("""
                INSERT INTO interacoes (timestamp, ativacao, tipo_interacao, tempo_permanencia, sessao_id)
                VALUES (?, ?, ?, ?, ?)
            """, (
                row['timestamp'],
                int(row['ativacao']),
                row['tipo_interacao'],
                int(row['tempo_permanencia']),
                row['sessao_id']
            ))
            inserted += 1
        except sqlite3.IntegrityError as e:
            errors += 1
            print(f"   ⚠️  Erro ao inserir registro: {e}")
    
    conn.commit()
    conn.close()
    
    print(f"✅ {inserted} registros inseridos com sucesso!")
    if errors > 0:
        print(f"⚠️  {errors} registros com erro (duplicados)")
    
    return True


def verify_database():
    """
    Verifica e exibe estatísticas do banco de dados.
    """
    print("\n🔍 Verificando banco de dados...")
    
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    
    # Total de registros
    cursor.execute("SELECT COUNT(*) FROM interacoes")
    total = cursor.fetchone()[0]
    
    # Estatísticas por tipo de interação
    cursor.execute("""
        SELECT tipo_interacao, COUNT(*) as qtd, AVG(tempo_permanencia) as tempo_medio
        FROM interacoes
        GROUP BY tipo_interacao
    """)
    stats = cursor.fetchall()
    
    # Taxa de ativação
    cursor.execute("SELECT AVG(ativacao) * 100 FROM interacoes")
    taxa_ativacao = cursor.fetchone()[0]
    
    # Período dos dados
    cursor.execute("SELECT MIN(timestamp), MAX(timestamp) FROM interacoes")
    periodo = cursor.fetchone()
    
    conn.close()
    
    print(f"\n📊 Estatísticas do Banco de Dados:")
    print(f"   - Total de registros: {total}")
    print(f"   - Taxa de ativação: {taxa_ativacao:.1f}%")
    print(f"   - Período: {periodo[0]} a {periodo[1]}")
    print(f"\n   Por tipo de interação:")
    for tipo, qtd, tempo_medio in stats:
        print(f"   - {tipo}: {qtd} registros, tempo médio: {tempo_medio:.1f}s")


def get_connection():
    """
    Retorna uma conexão com o banco de dados.
    Útil para uso em outros módulos.
    """
    return sqlite3.connect(DB_PATH)


if __name__ == "__main__":
    print("=" * 60)
    print("EDUBOT - Inicialização do Banco de Dados")
    print("=" * 60)
    
    # Criar banco de dados
    create_database()
    
    # Carregar dados do CSV
    success = load_csv_to_database()
    
    if success:
        # Verificar dados
        verify_database()
    
    print("\n" + "=" * 60)
    print("✅ Inicialização concluída!")
    print("=" * 60)
