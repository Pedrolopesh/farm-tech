import seaborn as sns
import matplotlib.pyplot as plt

# Carregar o conjunto de dados Tips
tips = sns.load_dataset('tips')

# Criar o gráfico de enxame
plt.figure(figsize=(10, 6))
sns.swarmplot(data=tips, x='day', y='total_bill', hue='time')

# Adicionar título e rótulos aos eixos
plt.title('Gráfico de Enxame do Total da Conta por Dia')
plt.xlabel('Dia da Semana')
plt.ylabel('Total da Conta')

# Mostrar o gráfico
plt.show()