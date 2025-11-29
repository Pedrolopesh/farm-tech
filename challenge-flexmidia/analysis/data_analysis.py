"""
EDUBOT - Análise e Limpeza de Dados
Sprint 2 - Challenge FlexMedia

Este script realiza a análise exploratória, limpeza e validação
dos dados coletados pelo totem, gerando visualizações e insights.
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import sqlite3
import os
from datetime import datetime

# Configurações de estilo
plt.style.use('seaborn-v0_8-whitegrid')
sns.set_palette("husl")
plt.rcParams['figure.figsize'] = (12, 6)
plt.rcParams['font.size'] = 12
plt.rcParams['axes.titlesize'] = 14
plt.rcParams['axes.labelsize'] = 12

# Caminhos
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
DB_PATH = os.path.join(SCRIPT_DIR, "..", "database", "totem.db")
PLOTS_DIR = os.path.join(SCRIPT_DIR, "plots")

# Criar diretório de plots se não existir
os.makedirs(PLOTS_DIR, exist_ok=True)


def load_data_from_db() -> pd.DataFrame:
    """
    Carrega dados do banco SQLite.
    """
    print("📥 Carregando dados do banco de dados...")
    
    conn = sqlite3.connect(DB_PATH)
    df = pd.read_sql_query("SELECT * FROM interacoes", conn)
    conn.close()
    
    # Converter timestamp para datetime
    df['timestamp'] = pd.to_datetime(df['timestamp'])
    
    print(f"✅ {len(df)} registros carregados")
    return df


def check_data_quality(df: pd.DataFrame) -> dict:
    """
    Verifica a qualidade dos dados e retorna métricas.
    """
    print("\n🔍 Verificando qualidade dos dados...")
    
    quality_report = {
        'total_registros': len(df),
        'duplicados': df.duplicated(subset=['sessao_id']).sum(),
        'valores_nulos': df.isnull().sum().to_dict(),
        'ativacao_valida': df['ativacao'].isin([0, 1]).all(),
        'tipo_interacao_valido': df['tipo_interacao'].isin(['curto', 'longo', 'nenhuma']).all(),
        'tempo_negativo': (df['tempo_permanencia'] < 0).sum()
    }
    
    print(f"   - Total de registros: {quality_report['total_registros']}")
    print(f"   - Duplicados (sessao_id): {quality_report['duplicados']}")
    print(f"   - Valores nulos: {sum(quality_report['valores_nulos'].values())}")
    print(f"   - Ativação válida (0/1): {'✅' if quality_report['ativacao_valida'] else '❌'}")
    print(f"   - Tipo interação válido: {'✅' if quality_report['tipo_interacao_valido'] else '❌'}")
    print(f"   - Tempos negativos: {quality_report['tempo_negativo']}")
    
    return quality_report


def clean_data(df: pd.DataFrame) -> pd.DataFrame:
    """
    Realiza limpeza e normalização dos dados.
    """
    print("\n🧹 Limpando e normalizando dados...")
    
    df_clean = df.copy()
    
    # Remover duplicados por sessao_id
    initial_count = len(df_clean)
    df_clean = df_clean.drop_duplicates(subset=['sessao_id'], keep='first')
    removed = initial_count - len(df_clean)
    if removed > 0:
        print(f"   - Removidos {removed} registros duplicados")
    
    # Normalizar tipo_interacao para minúsculo
    df_clean['tipo_interacao'] = df_clean['tipo_interacao'].str.lower().str.strip()
    
    # Garantir que tempo_permanencia seja positivo
    df_clean['tempo_permanencia'] = df_clean['tempo_permanencia'].clip(lower=0)
    
    # Adicionar colunas derivadas para análise
    df_clean['data'] = df_clean['timestamp'].dt.date
    df_clean['hora'] = df_clean['timestamp'].dt.hour
    df_clean['dia_semana'] = df_clean['timestamp'].dt.day_name()
    df_clean['periodo'] = df_clean['hora'].apply(lambda x: 
        'Manhã' if 6 <= x < 12 else 
        'Tarde' if 12 <= x < 18 else 
        'Noite'
    )
    
    print(f"✅ Dados limpos: {len(df_clean)} registros válidos")
    
    return df_clean


def generate_statistics(df: pd.DataFrame) -> dict:
    """
    Gera estatísticas descritivas dos dados.
    """
    print("\n📊 Gerando estatísticas descritivas...")
    
    # Filtrar apenas interações efetivas
    df_ativo = df[df['ativacao'] == 1]
    
    stats = {
        'total_interacoes': len(df),
        'total_ativacoes': len(df_ativo),
        'taxa_ativacao': len(df_ativo) / len(df) * 100,
        'interacoes_curtas': len(df_ativo[df_ativo['tipo_interacao'] == 'curto']),
        'interacoes_longas': len(df_ativo[df_ativo['tipo_interacao'] == 'longo']),
        'tempo_medio': df_ativo['tempo_permanencia'].mean(),
        'tempo_mediano': df_ativo['tempo_permanencia'].median(),
        'tempo_std': df_ativo['tempo_permanencia'].std(),
        'tempo_min': df_ativo['tempo_permanencia'].min(),
        'tempo_max': df_ativo['tempo_permanencia'].max()
    }
    
    print(f"   📈 KPIs Principais:")
    print(f"   - Total de detecções: {stats['total_interacoes']}")
    print(f"   - Total de ativações: {stats['total_ativacoes']}")
    print(f"   - Taxa de ativação: {stats['taxa_ativacao']:.1f}%")
    print(f"   - Interações curtas: {stats['interacoes_curtas']} ({stats['interacoes_curtas']/stats['total_ativacoes']*100:.1f}%)")
    print(f"   - Interações longas: {stats['interacoes_longas']} ({stats['interacoes_longas']/stats['total_ativacoes']*100:.1f}%)")
    print(f"   - Tempo médio de permanência: {stats['tempo_medio']:.1f}s")
    print(f"   - Tempo mediano: {stats['tempo_mediano']:.1f}s")
    
    return stats


def plot_interactions_per_day(df: pd.DataFrame):
    """
    Gera gráfico de interações por dia.
    """
    print("\n📈 Gerando gráfico: Interações por Dia...")
    
    daily_counts = df.groupby('data').size().reset_index(name='interacoes')
    daily_counts['data'] = pd.to_datetime(daily_counts['data'])
    
    fig, ax = plt.subplots(figsize=(14, 6))
    
    ax.bar(daily_counts['data'], daily_counts['interacoes'], 
           color='#2196F3', alpha=0.8, edgecolor='white')
    
    ax.set_xlabel('Data')
    ax.set_ylabel('Número de Interações')
    ax.set_title('EDUBOT - Interações por Dia', fontsize=16, fontweight='bold')
    
    # Linha de tendência (média móvel)
    if len(daily_counts) > 5:
        daily_counts['media_movel'] = daily_counts['interacoes'].rolling(window=5, center=True).mean()
        ax.plot(daily_counts['data'], daily_counts['media_movel'], 
               color='#FF5722', linewidth=2, label='Média Móvel (5 dias)')
        ax.legend()
    
    plt.xticks(rotation=45, ha='right')
    plt.tight_layout()
    
    filepath = os.path.join(PLOTS_DIR, 'interacoes_por_dia.png')
    plt.savefig(filepath, dpi=150, bbox_inches='tight')
    plt.close()
    
    print(f"   ✅ Salvo em: {filepath}")


def plot_interaction_types(df: pd.DataFrame):
    """
    Gera gráfico de pizza dos tipos de interação.
    """
    print("📈 Gerando gráfico: Tipos de Interação...")
    
    # Filtrar apenas ativações efetivas
    df_ativo = df[df['ativacao'] == 1]
    
    type_counts = df_ativo['tipo_interacao'].value_counts()
    
    colors = ['#4CAF50', '#2196F3', '#FF9800']
    explode = (0.05, 0.05)
    
    fig, ax = plt.subplots(figsize=(10, 8))
    
    wedges, texts, autotexts = ax.pie(
        type_counts.values, 
        labels=type_counts.index.str.capitalize(),
        autopct='%1.1f%%',
        colors=colors[:len(type_counts)],
        explode=explode[:len(type_counts)],
        shadow=True,
        startangle=90
    )
    
    # Estilizar texto
    for autotext in autotexts:
        autotext.set_color('white')
        autotext.set_fontweight('bold')
        autotext.set_fontsize(14)
    
    ax.set_title('EDUBOT - Distribuição de Tipos de Interação', 
                fontsize=16, fontweight='bold')
    
    # Adicionar legenda com contagem
    legend_labels = [f'{idx.capitalize()}: {val} interações' 
                    for idx, val in type_counts.items()]
    ax.legend(wedges, legend_labels, loc='lower right')
    
    plt.tight_layout()
    
    filepath = os.path.join(PLOTS_DIR, 'tipos_interacao.png')
    plt.savefig(filepath, dpi=150, bbox_inches='tight')
    plt.close()
    
    print(f"   ✅ Salvo em: {filepath}")


def plot_permanence_time(df: pd.DataFrame):
    """
    Gera gráfico de tempo médio de permanência.
    """
    print("📈 Gerando gráfico: Tempo de Permanência...")
    
    # Filtrar apenas ativações com tempo > 0
    df_tempo = df[(df['ativacao'] == 1) & (df['tempo_permanencia'] > 0)]
    
    fig, axes = plt.subplots(1, 2, figsize=(14, 6))
    
    # Histograma de tempo de permanência
    axes[0].hist(df_tempo['tempo_permanencia'], bins=30, 
                color='#9C27B0', alpha=0.7, edgecolor='white')
    axes[0].axvline(df_tempo['tempo_permanencia'].mean(), color='#FF5722', 
                   linestyle='--', linewidth=2, label=f'Média: {df_tempo["tempo_permanencia"].mean():.1f}s')
    axes[0].axvline(df_tempo['tempo_permanencia'].median(), color='#4CAF50', 
                   linestyle='--', linewidth=2, label=f'Mediana: {df_tempo["tempo_permanencia"].median():.1f}s')
    axes[0].set_xlabel('Tempo de Permanência (segundos)')
    axes[0].set_ylabel('Frequência')
    axes[0].set_title('Distribuição do Tempo de Permanência')
    axes[0].legend()
    
    # Boxplot por tipo de interação
    df_plot = df_tempo[df_tempo['tipo_interacao'].isin(['curto', 'longo'])]
    sns.boxplot(data=df_plot, x='tipo_interacao', y='tempo_permanencia', 
               ax=axes[1], palette=['#4CAF50', '#2196F3'])
    axes[1].set_xlabel('Tipo de Interação')
    axes[1].set_ylabel('Tempo de Permanência (segundos)')
    axes[1].set_title('Tempo de Permanência por Tipo')
    
    plt.suptitle('EDUBOT - Análise de Tempo de Permanência', 
                fontsize=16, fontweight='bold', y=1.02)
    plt.tight_layout()
    
    filepath = os.path.join(PLOTS_DIR, 'tempo_permanencia.png')
    plt.savefig(filepath, dpi=150, bbox_inches='tight')
    plt.close()
    
    print(f"   ✅ Salvo em: {filepath}")


def plot_hourly_distribution(df: pd.DataFrame):
    """
    Gera gráfico de distribuição por hora do dia.
    """
    print("📈 Gerando gráfico: Distribuição por Hora...")
    
    hourly_counts = df.groupby('hora').size().reset_index(name='interacoes')
    
    fig, ax = plt.subplots(figsize=(12, 6))
    
    bars = ax.bar(hourly_counts['hora'], hourly_counts['interacoes'],
                 color='#00BCD4', alpha=0.8, edgecolor='white')
    
    # Destacar horários de pico
    max_val = hourly_counts['interacoes'].max()
    for bar, val in zip(bars, hourly_counts['interacoes']):
        if val >= max_val * 0.8:
            bar.set_color('#FF5722')
    
    ax.set_xlabel('Hora do Dia')
    ax.set_ylabel('Número de Interações')
    ax.set_title('EDUBOT - Distribuição de Uso por Hora', fontsize=16, fontweight='bold')
    ax.set_xticks(range(8, 23))
    ax.set_xticklabels([f'{h}:00' for h in range(8, 23)])
    
    plt.xticks(rotation=45, ha='right')
    plt.tight_layout()
    
    filepath = os.path.join(PLOTS_DIR, 'distribuicao_horaria.png')
    plt.savefig(filepath, dpi=150, bbox_inches='tight')
    plt.close()
    
    print(f"   ✅ Salvo em: {filepath}")


def plot_heatmap(df: pd.DataFrame):
    """
    Gera heatmap de uso por dia da semana e hora.
    """
    print("📈 Gerando gráfico: Heatmap de Uso...")
    
    # Criar tabela de contagem
    pivot = df.groupby(['dia_semana', 'hora']).size().unstack(fill_value=0)
    
    # Ordenar dias da semana
    dias_ordem = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    dias_pt = ['Segunda', 'Terça', 'Quarta', 'Quinta', 'Sexta', 'Sábado', 'Domingo']
    
    pivot = pivot.reindex([d for d in dias_ordem if d in pivot.index])
    pivot.index = [dias_pt[dias_ordem.index(d)] for d in pivot.index]
    
    fig, ax = plt.subplots(figsize=(14, 6))
    
    sns.heatmap(pivot, cmap='YlOrRd', annot=True, fmt='d', 
               ax=ax, cbar_kws={'label': 'Interações'})
    
    ax.set_xlabel('Hora do Dia')
    ax.set_ylabel('Dia da Semana')
    ax.set_title('EDUBOT - Mapa de Calor de Uso', fontsize=16, fontweight='bold')
    
    plt.tight_layout()
    
    filepath = os.path.join(PLOTS_DIR, 'heatmap_uso.png')
    plt.savefig(filepath, dpi=150, bbox_inches='tight')
    plt.close()
    
    print(f"   ✅ Salvo em: {filepath}")


def save_cleaned_data(df: pd.DataFrame):
    """
    Salva os dados limpos em CSV para uso posterior.
    """
    filepath = os.path.join(SCRIPT_DIR, 'cleaned_data.csv')
    df.to_csv(filepath, index=False)
    print(f"\n💾 Dados limpos salvos em: {filepath}")


def main():
    """
    Função principal que executa toda a análise.
    """
    print("=" * 60)
    print("EDUBOT - Análise e Limpeza de Dados")
    print("Sprint 2 - Challenge FlexMedia")
    print("=" * 60)
    
    # Carregar dados
    df = load_data_from_db()
    
    # Verificar qualidade
    quality = check_data_quality(df)
    
    # Limpar dados
    df_clean = clean_data(df)
    
    # Gerar estatísticas
    stats = generate_statistics(df_clean)
    
    # Gerar gráficos
    print("\n" + "=" * 60)
    print("GERANDO VISUALIZAÇÕES")
    print("=" * 60)
    
    plot_interactions_per_day(df_clean)
    plot_interaction_types(df_clean)
    plot_permanence_time(df_clean)
    plot_hourly_distribution(df_clean)
    plot_heatmap(df_clean)
    
    # Salvar dados limpos
    save_cleaned_data(df_clean)
    
    print("\n" + "=" * 60)
    print("✅ Análise concluída!")
    print(f"📊 Gráficos salvos em: {PLOTS_DIR}")
    print("=" * 60)
    
    return df_clean, stats


if __name__ == "__main__":
    df_clean, stats = main()
