import seaborn as sns
import matplotlib.pyplot as plt

# Dados de exemplo
tips = sns.load_dataset('tips')

# Definindo a área de plotagem
plt.figure(figsize=(12, 6))

# Criar o gráfico de regressão
sns.regplot(data=tips, x='total_bill', y='tip', ci=95)

# Adicionar título e rótulos aos eixos
plt.title('Gráfico de Regressão do Total da Conta vs. Gorjeta')
plt.xlabel('Total da Conta')
plt.ylabel('Gorjeta')

# Mostrar o gráfico
plt.show()