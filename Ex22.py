# O Jogo do par ou ímpar é usado onde duas pessoas jogam geralmente para decidir um impasse,
# cada um escolhe entre par ou ímpar e mostra o seu número,
# a soma entre eles resulta em um número par ou ímpar e assim é decidido o vencedor.
# Aqui faremos com a máquina, ela escolherá um número randômico entre 0 e 10 e você escolherá o seu.

from random import randint

print("Bem vindo ao jogo do par ou ímpar!")
print("Escolha entre par ou ímpar e digite um número de 0 a 10.")

escolha = input("Digite par ou ímpar: ")
num = int(input("Digite um número de 0 a 10: "))
num_pc = randint(0, 10)

if (num + num_pc) % 2 == 0:
    resultado = "par"
else:
    resultado = "ímpar"

print(f"O número escolhido pela máquina foi: {num_pc}")
print(f"O resultado da soma foi: {num + num_pc}")

if escolha == resultado:
    print("Parabéns, você ganhou!")
else:
    print("Que pena, você perdeu!")
