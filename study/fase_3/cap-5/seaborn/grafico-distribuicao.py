import seaborn as sns
import matplotlib.pyplot as plt

# Dados de exemplo
iris = sns.load_dataset('iris')
plt.figure(figsize=(10, 6))

# Criar o gráfico de dispersão
sns.scatterplot(data=iris, x='sepal_length', y='sepal_width', hue='species', style='species', palette='deep')

# Adicionar título e rótulos aos eixos
plt.title('Gráfico de Dispersão do Conjunto de Dados Iris')
plt.xlabel('Comprimento da Sépala')
plt.ylabel('Largura da Sépala')

# Mostrar o gráfico
plt.show()