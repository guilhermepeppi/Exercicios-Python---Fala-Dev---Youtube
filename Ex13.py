# Escreva um programa que leia um número inteiro
# de 3 dígitos e imprima se o algarismo da dezena é par ou ímpar.

numero = int(input('Digite um número: '))

dezena = numero % 100 // 10
if dezena % 2 == 0:
    print(f'O algorismo da dezena {dezena} é par')
else:
    print(f'O algorismo da dezena {dezena} é ímpar')
