import matplotlib.pyplot as plt

# Definindo a área de plotagem
plt.figure(figsize=(12, 6))

# Dados de exemplo
anos = [2015, 2016, 2017, 2018, 2019, 2020]
c1 = [3, 4, 6, 8, 7, 9]
c2 = [2, 3, 4, 5, 4, 6]
c3 = [1, 2, 2, 3, 3, 4]

rotulos = ['Categoria 1', 'Categoria 2', 'Categoria 3']

# Criar o gráfico de área
plt.stackplot(anos, c1, c2, c3, labels=rotulos, alpha=0.8)

# Adicionar título e rótulos aos eixos
plt.title('Gráfico de Área Exemplo')
plt.xlabel('Ano')
plt.ylabel('Valores')
plt.legend()

# Mostrar o gráfico
plt.show()