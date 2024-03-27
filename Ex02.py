# Escreva um programa que receba três números quaisquer e apresente:
# a) a soma dos quadrados dos três números;
# b) o quadrado da soma dos três números.

soma_quadrados = 0
contador = 0
soma_total = 0

print('A)')
while contador < 3:
    numero = int(input(f'Digite o {contador+1}º número: '))
    soma_quadrados += numero ** 2
    contador += 1
print("A soma dos quadrados dos três números é:", soma_quadrados)

print('=' * 20)

contador = 0
soma_total = 0  # Reinicialize a variável soma_total para evitar resultados incorretos.

print('B)')
while contador < 3:
    numero = int(input(f'Digite o {contador+1}º número: '))
    soma_total += numero
    contador += 1

quadrado_soma = soma_total ** 2  # Calcula o quadrado da soma dos três números.
print("O quadrado da soma dos três números é:", quadrado_soma)
