import numpy as np

# # Criação de uma matriz 2x2
# a = np.array([[1, 2], [3, 4]])

# b = a.T
#
# print(a)
# print(b)

a = np.array([[1, 2], [3, 4]])
b = np.array([[5, 6], [7, 8]])

# a =
# [1, 2]
# [3, 4]

# b =
# [5, 6]
# [7, 8]

# Produto matricial entre a e b
c = np.dot(a, b)
print(c)

# Ou utilizando o operador @
d = a @ b
print(d)

# Valor da matriz c é igual a matriz d
print(c == d) # Saída: [[ True  True]
              #         [ True  True]]


# === Determinante e inversa ===
a = np.array([[1, 2], [3, 4]])

# Determinante
det = np.linalg.det(a)

# Inversa
inv = np.linalg.inv(a)

print(a)
print(det)
print(inv)