import numpy as np

# === Salvando e carregando arrays em arquivos binários

a = np.array([1, 2, 3, 4, 5])

# Salvando um array em um arquivo binário
np.save('meu_array.npy', a)

# Carregando um array de um arquivo binário
b = np.load('meu_array.npy')

print(b) # Saída: [1 2 3 4 5]

# === Salvando e carregando em formato de texto

a = np.array([9, 8, 7, 6, 5, 4, 3, 2, 1])

# Salvando um array em um arquivo de texto
np.savetxt('meu_array.txt', a)

# Carregando um array de um arquivo de texto
b = np.loadtxt('meu_array.txt')

print(b) # Saída: [9. 8. 7. 6. 5. 4. 3. 2. 1.]