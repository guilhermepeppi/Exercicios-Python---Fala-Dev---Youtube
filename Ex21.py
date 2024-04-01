# Esse é o jogo dos dados, muito usado em Las Vegas nos cassinos,
# aposte em um número que seja o resultado da soma deles e ganhe o seu dinheiro.
# Crie duas variáveis para representar os dados e uma para sua aposta,
# crie uma para armazenar o resultado e faça a verificação.

from random import randint

print("Bem vindo ao jogo dos dados!")

aposta = int(input("Digite o número da sua aposta: "))

num1 = randint(1, 6)
num2 = randint(1, 6)

print(f"Os números sorteados foram: {num1} e {num2}")
print(f"O resultado da soma foi: {num1 + num2}")

if aposta == num1 + num2:
    print("Parabéns, você ganhou!")
else:
    print("Que pena, você perdeu!")
