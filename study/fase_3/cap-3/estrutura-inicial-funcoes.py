import numpy as np

# # Array unidimensional a partir de uma lista
# a = np.array([1, 4, 3, 7, 2, 0, 7, 3, 5])
# # Array bidimensional a partir de uma lista
# b = np.array([[1, 4, 3], [7, 2, 0], [7, 3, 5]])
#
# # Array com 3 linhas e 4 colunas
# # Preenchido com números zero
# c = np.zeros((3, 4))
# # Array com 2 linhas e 3 colunas
# # Preenchido com números um
# d = np.ones((2, 3))
# # Array com 2 linhas e 2 colunas
# # Preenchido com valores aleatórios entre 0 e 1
# e = np.random.random((2, 2))
#
# a = np.array([1, 4, 3, 7, 2, 0, 7, 3, 5])
# b = np.array([[1, 4, 3], [7, 2, 0], [7, 3, 5]])
#
# # Verifica o formato das matrizes
# print(a.shape, b.shape)
#
# # Acesso a elementos únicos e sequenciais
# print("a[0] => ", a[0]) # Saída: 1 - Pega o primeiro elemento
# print("a[1:3] => ", a[1:3]) # Saída: [4 3]
#
# # Acesso à arrays bidimensionais
# print("b[0] => ", b[0]) # Saída: [1 4 3]
# print("b[1, 1] => ", b[1, 1]) # Saída: 2
#
# # Modificação do elemento na posição 0
# a[0] = 10
# print(a) # Saída: [10 4 3 7 2 0 7 3 5]
#
# # Modificação do elemento na posição central da matriz 3x3
# b[1][1] = 10
# print(b) # Saída: [[ 1  4  3]
#          #         [ 7 10  0]
#          #         [ 7  3  5]]

# ===

a = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9])

# Seleção entre a posição 1 e 7, pulando a de 2 em 2.
# Ou seja, nesse caso todos os pares menores que 7.
print(a[1:7:2]) # Saída: [2 4 6]

# Seleção com indexador negativo
# Passo invertido, pulando de 3 em 3.
print(a[::-3]) # Saída: [9 6 3]
b = np.array([
    [1, 2, 3, 4, 5],
    [2, 3, 4, 5, 6],
    [3, 4, 5, 6, 7],
    [4, 5, 6, 7, 8],
    [5, 6, 7, 8, 9]
])
# Seleciona as linhas e colunas pulando de 2 em 2.
# Ou seja, a primeira, segunda e terceira de cada eixo.
print(b[::2, ::2]) # Saída [[1 3 5]
                   #        [3 5 7]
                   #        [5 7 9]]
