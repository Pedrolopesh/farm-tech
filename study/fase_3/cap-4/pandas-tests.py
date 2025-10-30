import pandas as pd

# === Series ===
# Criando uma Series a partir de uma lista
s = pd.Series([1, 2, 3, 4, 5])

# Acesso à posição de índice 4
print(s[4]) # Saída: 5

# === Data frames ===
dados = {
'Produto': ['A', 'B', 'C'],
'Preço': [100, 200, 300],
'Quantidade': [10, 20, 30]
}
# Criando um DataFrame a partir de um dicionário
df = pd.DataFrame(dados)

# Acesso à coluna Produto
coluna = df['Produto']
# Acesso à múltiplas colunas
colunas = df[['Produto', 'Preço']]
# Acesso à primeira linha pelo rótulo
linha = df.loc[0]
# Acesso à primeira linha pela posição
linha = df.iloc[0]
# Acesso a um intervalo de linhas pela posição
df.iloc[0:2]
# Acesso a um único valor pela coluna e linha
a = df['Produto'][0]
print(a) # Saída: 'A'
# Acesso a um único valor pela linha e coluna
b = df.iloc[0]['Produto']
print(b) # Saída: 'A'