# arq = open('arquivo.txt', 'w') # w = write
# arq.write("Estamos na fase de leitura e gravação \n")
# arq.write("Nesta Turma da FIAP \n")
# arq.write("Todos alunos voam! \n")
#
# arq.close()
#
# arq = open('arquivo.txt', 'r') # r = read
#
# print(arq.read())
# arq.close()

# ======= Opção com o "w" se o arquivo existir, sobrepoem
# modos: +, a, e, x
# arq = open("arquivo.txt", "w+")
#
# arq.writelines(
#     [
#         "linha 1\n",
#         "linha 2\n",
#         "linha 3\n"
#     ]
# )
#
# arq.seek(0)
# print(arq.read())
# arq.close()

# # ======= Opção com o "a"
# arq = open("arquivo.txt", "a+")
# arq.write("Nova linha")
#
# arq.seek(0)
# print(arq.read())
# arq.close()

# # ======= Opção com o "x"
# arq = open("arquivo2.txt", "x")
# arq.write("Nova linha \n")
#
# arq.seek(0)
# print(arq.read())
# arq.close()


# # ======== Formas de ler o arquivo gravado
# # Utilizando o método readline()
#
# arq = open("arquivo.txt", "r")
#
# arq.readline()
# arq.readline()
# arq.seek(10)
# print(arq.readline(), end="")
#
# arq.close()


# # Utilizando o método readlines()
#
# arq = open("arquivo.txt", "r")
#
# lista = arq.readlines()
# for i in range(0, len(lista)):
#     print(lista[i], end="")
#
# arq.close()

# ======= manipulação de arquivos JSON e o with

# pet = {
#     'pet1': {
#         'tipo': 'Cachorro',
#         'nome': 'Bob',
#         'idade': 12
#     },
#     'pet2': {
#         'tipo': 'Gato',
#         'nome': 'Lua',
#         'idade': 2
#     }
# }
#
# print(pet)
#
# import json
#
# pet_json = json.dumps(pet, indent=4)
# print(pet_json)
#
# with open("arquivo.json", "w+") as file:
#     file.write(pet_json)



# ===== Leitura de arquivos
# # Lendo e formatando arquivos no formato JSON
# import json
#
# with open("arquivo.json", "r+") as file:
#     # Lê todo o conteúdo do arquivo JSON
#     pet_json = file.read()
#     print("Conteúdo bruto do arquivo:")
#     print(pet_json)
#
#     # Converte o conteúdo de texto para dicionário Python
#     pet_json = json.loads(pet_json)
#     print("\nConteúdo convertido em dicionário:")
#     print(pet_json)
#
# # Percorre o dicionário externo
# for k, v in pet_json.items():
#     print(f"\n{k}:")
#     # Percorre o dicionário interno (chave e valor)
#     for k1, v1 in v.items():
#         print(f"\t{k1}: {v1}")
#
#
