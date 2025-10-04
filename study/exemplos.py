"""
EXEMPLO:
Fazer um algoritmo que leia a compra de um usuário.
Caso ela seja acima de 300 reais efetuar o desconto de 10% e
exibir o valor da compra atualizado

ENTRADA: 400    SAÍDA: 360
ENTRADA: 150    SAÍDA: 150

"""


# compra = float(input('Valor da Compra: '))
# desconto = 0
#
# if compra > 300:
#     desconto = compra * 10 / 100
#     compra = compra - desconto
#
# print(f'Valor da Compra: {compra:.2f}\n'
#       f'Valor da Desconto: {desconto:.2f}\n')

# # ============================ Fast Test 1 ============================
# idade = int(input('Digite sua idade: '))
# print("A sua idade é "+ str(idade) + "anos")
# # ============================ Fast Test 1 ============================


# # ============================ Fast Test 2 ============================
# num = input('Digite um número: ')
# dobro = num + num
# print(f"O Dobro de {num} é {dobro}")
# # ============================ Fast Test 2 ============================


# ============================ Fast Test 3 ============================
# n1 = 6
# n2 = 2
# n3 = 4
# n1 = n3
# n2 = n1
# n3 = n2
# print(f"n1 = {n1}, n2 = {n2} e n3 = {n3}")
# ============================ Fast Test 3 ============================

# # ============================ Exercicio Aula 7 ============================
# nota1 = float(input("Nota 1: "))
# nota2 = float(input("Nota 2: "))
# nota3 = float(input("Nota 3: "))
#
# media = (nota1 + nota2 + nota3) / 3
#
# if media >= 6:
#     print(f"Aprovado com média de {media:.1f}")
# else:
#     print(f"Reprovado com média de {media:.1f}")
#
# # ============================ Exercicio Aula 7 ============================


# # ============================ Exercicio Aula 8 - elif ============================
# num = int(input("Fala um numero: "))
#
# if num > 0:
#     print(f"Número {num} é Positivo")
# elif num < 0:
#     print(f"Número {num} é Negativo")
# else:
#     print(f"Número {num} é Nulo")
# # ============================ Exercicio Aula 8 - elif ============================


# # ============================ Exercicio Aula 10 - Negar variavel, E, OU ============================
# op1 = True
# op2 = False
#
# print("1. ",op1 and op2)
# print("2. ",op1 or op2)
# print("3. ",op1 and not op2)
# print("4. ", not (op1 or op2))
# print("5. ", not op1 and op2 or not op1 and op1)
# # ============================ Exercicio Aula 10 - exercicio com elif ============================

# # ============================ Estrutura de Repetição ============================

# # ============== pré condicional ==============
# pré condicional - laço enquanto (o,n)
# primeiro analisa a ação e depois executa

# """
# Algoritmo: Consistir duas notas dadas pelo usuário como válidas ou não.
# """
#
# nota1 = float(input("Digite a nota 1:"))
# while nota1 < 0 or nota1 > 10:
#     print(f"A Nota {nota1} inválida, digite uma nota entre 0 e 10:", end=" ")
#     nota1 = float(input())
#
# nota2 = float(input("Digite a nota 2:"))
# while nota2 < 0 or nota2 > 10:
#     print(f"A Nota {nota2} inválida, digite uma nota entre 0 e 10:", end=" ")
#     nota2 = float(input())
#
# media = (nota1 + nota2) / 2
# print("Media = ", media)
# # ============== pré condicional ==============

# # ============== pós condicional ==============
# # pós condicional - Repita (1n)
# # primeiro executa a ação e depois analisa
# count = 0
# while count < 10:
#     print("Comando 1")
#     print("Comando 2")
#     print("Comando 3")
#     print("Comando 4")
#     if count == 5:
#         count = count + 1
#         break
#         print("Comando 5")
#         print("Comando 6")
#         print("Comando 7")
#         print("Comando 8")
#         print("Comando 9")
#         print("Comando 10")
#     count = count + 1
# else:
#     print("Laço executado sem interrupção")
# # ============== pós condicional ==============

# # contador - 1,f
# # Laço com for
# # Exemplo:
# # for volta in range(inicio, fim, incremento)
#
# tab = int(input('Digite a tabuada: '))
# for volta in range(1, 11, 1):
#     mult = tab * volta
#     print(f"{tab} x {volta} = {mult}")

# # ============================ Estrutura de Repetição ============================


# x = 23
# y = 10
# z = 2
# print(x % y >= y/z)

# vendas_mes = 3000
# if vendas_mes < 3000:
#     comissao = vendas_mes * 0.2
# else:
#     comissao = vendas_mes * 0.3
# print(f"Comissão = R$ {comissao:.2f}")


# nota1 = 5.5
# nota2 = 4.5
# media = nota1 + nota2 / 2
# print("A média das notas {0} e {1} = {2}".format(nota1, nota2, media))


# b = 100
# if b != 50 * 2:
#     b = b - 300
# else:
#     b = b + 300
# b = b + 1
# if b == 301:
#     b = b + 2
# print("Resposta = {0}".format(b))


# a = 6
# b = 10
# c = 2
# if a + b > c:
#     c = b * c
# elif a != b and b != c:
#     b = a + c
# if a == b or b == c:
#     a = b - 1
# else:
#     a = b + 1
#     b = c + 1
#     c = a + 1
# print(f"a = {a} | b = {b} | c = {c}")

# # ============================ Matriz ============================

# matriz = [
#     [0,0,0],
#     [0,0,0]
# ]
#
# def exibir_matriz(m) -> None:
#     for l in range(2):
#         for c in range(3):
#             print(f'{m[l][c]}\t', end='')
#         print()
#
# exibir_matriz(matriz)


# ============================ MANIPULAÇÃO DOS ELEMENTOS DA LISTA ============================
# # C  [ 0   1    2      3    4    5      6      7 ]
# lista = [23, 5.6, True, "@", 12, 47, "Fiap", 2]
# # D  [-8  -7   -6    -5   -4   -3    -2    -1 ]
#
# print(lista[0])
# print(lista[-1])
# print(lista[2:5])
#
# l1 = [1,2,3]
# l2 = [4,5,6]
#
# l3 = l1 + l2
# print(l3)
#
# l1.extend(l2)
# print(l1)

lista = [34, "On", 45.8, False, 99]
print(lista)

# operações com listas:

# append -> adiciona um item no final da lista
lista.append("Novo")
print(lista)

# insert -> insere um elemento no meio da lista
lista.insert(2, "meio")
print(lista)

# pop -> remove um elemento da lista
lista.pop(3)
print(lista)

# clear -> apaga os elementos da lista
# lista.clear()
# print(lista)

# del -> apaga a lista
# del(lista)
del(lista[2:5])
print(lista)

# ======= TUPLA =======
tupla = ("Edson", 45, True, 76.9, 33)
print(tupla)

# não pode ser modificado

# transformando em lista para ser modificado
lista = list(tupla)
print(lista)


# transformando tupla em lista
newTupla = tuple(lista)
print(newTupla)
































