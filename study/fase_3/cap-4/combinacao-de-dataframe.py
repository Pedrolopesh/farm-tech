import pandas as pd

# === Junção (Join) ===

# DataFrame de produtos com 'ProdutoID' como índice
df_produtos = pd.DataFrame({
    'ProdutoID': [1, 2, 3, 4],
    'NomeProduto': ['Prod A', 'Prod B', 'Prod C', 'Prod D']
}).set_index('ProdutoID')
print('df_produtos: \n', df_produtos, '\n')

# DataFrame de vendas com 'ProdutoID' como índice
df_vendas = pd.DataFrame({
    'VendaID': [101, 102, 103, 104],
    'ProdutoID': [1, 2, 2, 4],
    'Quantidade': [10, 5, 15, 7]
}).set_index('ProdutoID')
print('df_vendas: \n', df_vendas, '\n')

# Realizar o join com base no índice 'ProdutoID'
df_combinado = df_vendas.join(df_produtos, how='inner')
print('df_combinado: \n', df_combinado, '\n')


# === Mesclagem (MERGE) ===
# DataFrame de produtos
df_produtos = pd.DataFrame({
    'ProdutoID': [1, 2, 3, 4],
    'NomeProduto': ['Prod A', 'Prod B', 'Prod C', 'Prod D']
})

# DataFrame de vendas
df_vendas = pd.DataFrame({
    'VendaID': [101, 102, 103, 104],
    'ProdutoID': [1, 2, 2, 4],
    'Quantidade': [10, 5, 15, 7]
})

# Realizar o merge com base na coluna 'ProdutoID'
df_combinado = pd.merge(df_vendas, df_produtos, on='ProdutoID', how='inner')
print('df_combinado: \n', df_combinado, '\n')

# === Concatenação (Concat) ===

# DataFrame de vendas no primeiro semestre
df_vendas1 = pd.DataFrame({
    'Mês': ['Jan', 'Fev', 'Mar', 'Abr', 'Mai', 'Jun'],
    'Vendas': [2000, 2200, 2500, 2700, 2600, 2900]
})

# DataFrame de vendas no segundo semestre
df_vendas2 = pd.DataFrame({
    'Mês': ['Jul', 'Ago', 'Set', 'Out', 'Nov', 'Dez'],
    'Vendas': [3100, 3300, 3200, 3400, 3500, 3600]
})

# Concatenar DataFrames verticalmente
df_vendas_completo = pd.concat([df_vendas1, df_vendas2], ignore_index=True)