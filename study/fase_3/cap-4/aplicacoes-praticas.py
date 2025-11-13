import pandas as pd
import numpy as np


# ===== LIMPEZA E PREPARAÇÃO DOS DADOS =====

data = {
    'Nome': ['Ana', 'Bruno', 'Carlos', 'Daniela', 'Eduardo'],
    'Idade': [23, 35, 45, None, 28],
    'Salário': [50000, 60000, None, 70000, 80000]
}
#Criação de DataFrame com valores nulos (None)
df = pd.DataFrame(data)
# Removendo linhas com valores ausentes
df_cleaned = df.dropna()
# Preenchendo valores ausentes com a média
df['Idade'] = df['Idade'].fillna(df['Idade'].mean())
df['Salário'] = df['Salário'].fillna(df['Salário'].mean())



# ===== ANALISE DE DADOS =====

# Simulação de dados de vendas
data = {
    'Dia': range(1, 31),
    'Vendas': np.random.randint(100, 200, size=30)
}

df_vendas = pd.DataFrame(data)

# Estatísticas descritivas
print(df_vendas.describe())

# ===== ANALISE DE SERIESTEMPORAIS =====
# Criando uma série temporal de exemplo
datas = pd.date_range(start='2023-01-01', periods=100, freq='D')

# Série temporal acumulada com ruído
dados = np.random.randn(100).cumsum()
ts = pd.Series(dados, index=datas)

# Calculando a média móvel de 3 dias
rolling_mean_3 = ts.rolling(window=3).mean()

# Exibindo os top 10 resultados da média móvel de 3 dias
print(rolling_mean_3.head(10))

# ===== INTEGRAÇÃO NATIVA COM VISUALIZAÇÃO DE DADOS =====
# Dados de exemplo de vendas mensais
data = {
    'Mês': ['Jan', 'Fev', 'Mar', 'Abr', 'Mai', 'Jun'],
    'Vendas': [2500, 2700, 3000, 3200, 3100, 3300]
}
# Criar DataFrame e plotar um gráfico de linha
df = pd.DataFrame(data)
df.plot(x='Mês', y='Vendas', marker='o', color='b')


