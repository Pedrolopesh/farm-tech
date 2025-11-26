import matplotlib.pyplot as plt

# Definindo a área de plotagem
plt.figure(figsize=(4, 4))

# Dados de exemplo
ids = ['A', 'B', 'C', 'D']
valores = [15, 30, 45, 10]
cores = ['gold', 'yellowgreen', 'lightcoral', 'lightskyblue']

# Criar o gráfico de pizza
plt.pie(valores, labels=ids, colors=cores, autopct='%1.1f%%')

# Adicionar título
plt.title('Gráfico de Pizza')

# Mostrar o gráfico
plt.show()