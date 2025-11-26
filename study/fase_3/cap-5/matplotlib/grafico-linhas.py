import matplotlib.pyplot as plt

# Definindo a área de plotagem tamanho
plt.figure(figsize=(10, 6))

# Dados de exemplo
x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
y = [10, 8, 12, 11, 11, 9, 13, 15, 14, 12]

# Criando o gráfico com os eixos x e y
plt.plot(x, y, label='Ações da empresa XYZ')

# Configurando as propriedades do gráfico
plt.xlabel('Dia')
plt.ylabel('Valor')
plt.title('Gráfico de Linha com Matplotlib')
plt.legend()
plt.grid(True)
plt.xticks(x) # Definindo os valores do eixo x

# Exibindo o gráfico
plt.show()