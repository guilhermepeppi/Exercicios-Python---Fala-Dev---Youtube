# Escreva um programa em Python que leia dois números distintos e apresente o quadrado do maior número.

numero1 = float(input('Digite o primeiro numero: '))
numero2 = float(input('Digite o segundo numero: '))

if numero1 > numero2:
    calculo = numero1**2
else:
    calculo = numero2**2

print(calculo)
