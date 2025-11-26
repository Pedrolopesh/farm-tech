import matplotlib.pyplot as plt
import numpy as np

# Definindo a área de plotagem
plt.figure(figsize=(12, 6))

# Fixando a inicialização dos números aleatórios
np.random.seed(0)

# Amostras aleatórias com distribuição normal
data = np.random.randn(1000)

# Criando o histograma
plt.hist(data, bins=30, color='cyan')
plt.xlabel('Valor')
plt.ylabel('Frequência')
plt.title('Histograma')
plt.grid(True)

# Exibindo o gráfico
plt.show()