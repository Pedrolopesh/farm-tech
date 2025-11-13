import matplotlib.pyplot as plt
# Definindo a área de plotagem
plt.figure(figsize=(12, 6))
# Dados de exemplo
categorias = ['A', 'B', 'C', 'D', 'E', 'F']
valores = [10, 20, 15, 30, 25, 22]
# Gráfico de barras
plt.bar(categorias, valores, color='orange')
# Configurando as propriedades do gráfico
plt.xlabel('Categoria')
plt.ylabel('Valor')
plt.title('Gráfico de Barras')
# Exibindo o gráfico
plt.show()