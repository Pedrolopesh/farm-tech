import seaborn as sns
import matplotlib.pyplot as plt

# Carregar o conjunto de dados Iris
iris = sns.load_dataset('iris')

# Criar o gráfico de pares
plt.figure(figsize=(6, 5))
sns.pairplot(iris, hue='species', diag_kind='kde')

# Adicionar título
plt.suptitle('Gráfico de Pares da Base Iris', y=1.02)

# Mostrar o gráfico
plt.show()