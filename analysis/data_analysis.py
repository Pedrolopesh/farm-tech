"""
EDUBOT - Análise e Limpeza de Dados
Sprint 4 - Challenge FlexMedia

Este script realiza a análise exploratória, limpeza e validação
dos dados coletados pelo totem, gerando visualizações e insights.
"""
import pandas as pd
import sqlite3
import seaborn as sns
import matplotlib.pyplot as plt

def run_analysis():
    conn = sqlite3.connect('database/totem.db')
    df = pd.read_sql("SELECT * FROM interacoes", conn)
    conn.close()

    # Heatmap: Perfil vs Humor (Objetivo 5)
    plt.figure(figsize=(10, 6))
    heatmap_data = pd.crosstab(df['perfil_usuario'], df['humor_estimado'])
    sns.heatmap(heatmap_data, annot=True, fmt="d", cmap="YlGnBu")
    plt.title("Mapa de Calor: Frequência de Perfil vs Humor")
    plt.show()

if __name__ == "__main__":
    run_analysis()