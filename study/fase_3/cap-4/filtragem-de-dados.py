import pandas as pd

# === Data frames ===
dados = {
'Produto': ['A', 'B', 'C'],
'Preço': [100, 200, 300],
'Quantidade': [10, 20, 30]
}

# Criando um DataFrame a partir de um dicionário
df = pd.DataFrame(dados)

# Filtragem de dados com base em uma condição
produtos_caros = df[df['Preço'] > 150]
print('produtos_caros: \n', produtos_caros, '\n')

produto_especifico = df[df['Produto'] == 'B']
print('produto_especifico: \n', produto_especifico, '\n')


# Filtragem com múltiplas condições
produtos_caros_quantidade_alta = df[(df['Preço'] > 150) & (df['Quantidade'] > 20)]
print('produtos_caros_quantidade_alta: \n', produtos_caros_quantidade_alta, '\n')

# Agregação de dados - soma total
total_vendas = df['Preço'].sum()
print('total_vendas: \n', total_vendas, '\n')

# Agregação de dados - média
media_precos = df['Preço'].mean()
print('media_precos: \n', media_precos, '\n')

# Agregação de dados por grupo – gera uma tabela sumarizada
vendas_por_produto = df.groupby('Produto').sum()
print('vendas_por_produto: \n\n', vendas_por_produto, '\n')

# Ordenação de dados em ordem crescente
df_ordenado = df.sort_values(by='Preço')
print('df_ordenado: \n', df_ordenado, '\n')

# Ordenação de dados em ordem decrescente
df_ordenado_desc = df.sort_values(by='Preço',ascending=False)
print('df_ordenado_desc: \n', df_ordenado_desc, '\n')

# Ordenação de dados por múltiplas colunas
df_ordenado_mult = df.sort_values(by=['Preço', 'Quantidade'])
print('df_ordenado_mult: \n', df_ordenado_mult, '\n')