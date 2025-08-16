def soma(a, b):
    return a + b

def multi (a, b):
    return a * b

def sub (a, b):
    return a - b

def div(a, b):
    if b == 0:
        return "Erro: divisão por zero!"
    return a / b



def menu():
    print('Olá, bem-vindo à calculadora em Python!\n')

    while True:
        print("\nEscolha a operação:")
        print("1 - Soma")
        print("2 - Subtração")
        print("3 - Multiplicação")
        print("4 - Divisão")
        print("0 - Sair")

        try:
            opcao = int(input("Digite a opção: "))
        except ValueError:
            print("Entrada inválida. Digite um número de 0 a 4.")
            continue

        if opcao == 0:
            print("Encerrando a calculadora. Até mais!")
            break

        if opcao not in [1, 2, 3, 4]:
            print("Opção inválida. Tente novamente.")
            continue

        try:
            a = float(input("Digite o primeiro número: "))
            b = float(input("Digite o segundo número: "))
        except ValueError:
            print("Entrada inválida. Digite números válidos.")
            continue

        if opcao == 1:
            resultado = soma(a, b)
        elif opcao == 2:
            resultado = sub(a, b)
        elif opcao == 3:
            resultado = multi(a, b)
        elif opcao == 4:
            resultado = div(a, b)

        print(f"Resultado: {resultado}")


menu()