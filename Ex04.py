# Faça um programa para uma loja de tintas.
# O programa deverá pedir o tamanho em metros quadrados da área a ser pintada.
# Considere que a cobertura da tinta é de 1 litro para cada 3 metros quadrados e
# que a tinta é vendida em latas de 18 litros, que custam R$ 80,00.
# Informe ao usuário a quantidades de latas de tinta a serem compradas e o preço total.

import math

# Solicitar o tamanho em metros quadrados da área a ser pintada
tamanho = float(input('Tamanho (em m²): '))

# Calcular a quantidade de litros de tinta necessários
litros = tamanho / 3

# Arredondar para cima para garantir que seja adquirido o número correto de latas
latas = math.ceil(litros / 18)

# Calcular o preço total da compra
preco_total = latas * 80

# Exibir a quantidade de latas de tinta necessárias e o preço total
print(f"Você precisará de {latas} latas de tinta.")
print(f"O preço total da compra será de R$ {preco_total:.2f}.")
