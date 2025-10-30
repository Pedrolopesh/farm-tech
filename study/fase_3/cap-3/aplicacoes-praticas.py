import numpy as np
from PIL import Image

# # === ANALISE DE DADOS ===
#
# # Simulação de dados de vendas com dados aleatórios
# # Os resultados deverão mudar a cada execução
# vendas = np.random.randint(100, 200, size=(30, 4))
# print(vendas)
#
# # Média de vendas por semana
# media_semanal = np.mean(vendas, axis=0)
#
# # Menores vendas por semana
# menor_semanal = np.min(vendas, axis=0)
#
# # Total de vendas por mês
# total_mensal = np.sum(vendas)
#
# # Maior venda do mês
# maior_mensal = np.max(vendas)
# print("media_semanal: ", media_semanal) # Saída: [149.76 154.03 161.26 148.8]
# print("menor_semanal: ",menor_semanal) # Saída: [101 100 112 105]
# print("total_mensal: ",total_mensal) # Saída: 18416
# print("maior_mensal: ",maior_mensal) # Saída: 199
#
# # === RESOLUÇÃO DE SISTEMAS LINEARES ===
#
# # Coeficientes do sistema linear
# a = np.array([[3, 2], [1, 2]])
# b = np.array([5, 5])
#
# # Resolvendo o sistema
# solucao = np.linalg.solve(a, b)
# print(solucao) # Saída: [0. 2.5]

# === PROCESSAMENTO DE IMAGENS DIGITAIS ===

# Carregando uma imagem e transformação em array
imagem = Image.open('imagem.png')
img_array = np.array(imagem)

# Convertendo para escala de cinza
img_cinza = np.dot(img_array[..., :3], [0.29, 0.58, 0.11])

# Salvando a imagem em escala de cinza
img_final = Image.fromarray(img_cinza.astype('uint8'))
img_final.save('imagem_cinza.png')