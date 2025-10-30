try:
    n1 = float(input("N1: "))
    n2 = float(input("N2: "))

    divisao = n1 / n2
    print(divisao)

except ValueError:
    print("Opa, você digitou um valor não numérico!")

except ZeroDivisionError:
    print("Não existe divisão por zero!")

except Exception as erro:
    print(f"Erro inesperado: {erro}")
    print("Chame o administrador do sistema!")

else:
    print("Programa executado normalmente!")

finally:
    print("Obrigado por utilizar o nosso sistema!")
