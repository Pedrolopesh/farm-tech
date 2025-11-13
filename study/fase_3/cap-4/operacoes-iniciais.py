import pandas as pd
#
# # === Series ===
# # Criando uma Series a partir de uma lista
# s = pd.Series([1, 2, 3, 4, 5])
#
# print(s)
#
# # Acesso à posição de índice 4
# print(s[4]) # Saída: 5

# === Data frames ===
dados = {
'Produto': ['A', 'B', 'C'],
'Preço': [100, 200, 300],
'Quantidade': [10, 20, 30]
}
# Criando um DataFrame a partir de um dicionário
df = pd.DataFrame(dados)

# print(df.values)

# Acesso à coluna Produto
coluna = df['Produto']
print('coluna: \n', coluna, '\n')

# Acesso à múltiplas colunas
colunas = df[['Produto', 'Preço']]
print('colunas: \n', colunas, '\n')

# Acesso à primeira linha pelo rótulo
linha = df.loc[0]
print('Linha pelo rótulo: \n', linha, '\n')

# Acesso à primeira linha pela posição
linha = df.iloc[0]
print('Linha pela posição: \n', linha, '\n')

# Acesso a um intervalo de linhas pela posição
df.iloc[0:2]
print('Acesso a um intervalo de linhas pela posição: \n\n', df.iloc[0:2], '\n')

# Acesso a um único valor pela coluna e linha
a = df['Produto'][0]
print(a, '\n') # Saída: 'A'

# Acesso a um único valor pela linha e coluna
b = df.iloc[0]['Produto']
print(b, '\n') # Saída: 'A'