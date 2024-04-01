# Escreva um programa usando FOR que exiba todos os números
# pares de 0 até o número informado pelo usuário.

num = int(input("Digite um número: "))
for i in range(0, num + 1, 2):
    print(i)
print("Fim do programa")
