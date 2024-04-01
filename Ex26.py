# Escreva um programa para exibir todos os números pares de 0 até o número informado pelo usuário,
# sem a utilização do if para avaliar se o número é par.

print("Bem vindo ao programa de números pares!")
num = int(input("Digite um número: "))
for i in range(0, num + 1, 2):
    print(i)
