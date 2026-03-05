"""
EDUBOT - Análise e Limpeza de Dados
Sprint 3 - Challenge FlexMedia

Este script realiza a análise exploratória, limpeza e validação
dos dados coletados pelo totem, gerando visualizações e insights.
"""
import sqlite3
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

# Cria a pasta para salvar os gráficos, se não existir
os.makedirs('challenge-flexmidia/analysis/plots', exist_ok=True)


def carregar_dados():
    print("📥 Carregando dados do banco SQLite...")
    db_path = 'challenge-flexmidia/database/totem.db'

    if not os.path.exists(db_path):
        print(f"⚠️ Banco de dados não encontrado em: {db_path}")
        return pd.DataFrame()

    conn = sqlite3.connect(db_path)
    df = pd.read_sql_query("SELECT * FROM interacoes", conn)
    conn.close()
    return df


def analisar_dados(df):
    print(f"✅ {len(df)} registros carregados com sucesso!\n")

    print("📊 KPIs Principais do EDUBOT:")
    print(f"- Total de interações: {len(df)}")
    print(f"- Média de toques por minuto: {df['toques_por_minuto'].mean():.1f}")
    print(f"- Tempo médio de permanência: {df['tempo_permanencia_seg'].mean():.1f}s")

    print("\n📈 Distribuição por Tipo de Interação:")
    dist = df['tipo_interacao'].value_counts(normalize=True).mul(100).round(1)
    for tipo, pct in dist.items():
        print(f"  - {tipo}: {pct}%")


def gerar_graficos(df):
    print("\n🎨 Gerando gráficos atualizados...")
    sns.set_theme(style="whitegrid")

    # 1. Gráfico de Tipos de Interação
    plt.figure(figsize=(8, 5))
    sns.countplot(data=df, x='tipo_interacao', order=['curta', 'média', 'longa'], palette='viridis')
    plt.title('Distribuição dos Tipos de Interação do Totem')
    plt.xlabel('Tipo de Interação')
    plt.ylabel('Quantidade de Sessões')
    plt.savefig('challenge-flexmidia/analysis/plots/tipos_interacao.png')
    plt.close()

    # 2. Relação entre Tempo de Permanência e Toques por Minuto
    plt.figure(figsize=(8, 5))
    sns.scatterplot(data=df, x='tempo_permanencia_seg', y='toques_por_minuto', hue='velocidade_toques',
                    palette='coolwarm')
    plt.title('Engajamento: Tempo de Permanência vs Frequência de Toques')
    plt.xlabel('Tempo de Permanência (segundos)')
    plt.ylabel('Toques por Minuto')
    plt.savefig('challenge-flexmidia/analysis/plots/engajamento_toques.png')
    plt.close()

    print("✅ Gráficos salvos com sucesso na pasta 'challenge-flexmidia/analysis/plots/'!")


if __name__ == "__main__":
    df_totem = carregar_dados()
    if not df_totem.empty:
        analisar_dados(df_totem)
        gerar_graficos(df_totem)