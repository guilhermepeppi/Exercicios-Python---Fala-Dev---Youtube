# Faça um programa para uma loja de tintas.
# O programa deverá pedir o tamanho em metros quadrados da área a ser pintada.
# Considere que a cobertura da tinta é de 1 litro para cada 3 metros quadrados e
# que a tinta é vendida em latas de 18 litros, que custam R$ 80,00.
# Informe ao usuário a quantidades de latas de tinta a serem compradas e o preço total.

import math

# Tamanho da área a ser pintada em metros quadrados
area_a_pintar = float(input("Digite o tamanho da área a ser pintada em metros quadrados: "))

# Calcula a quantidade de litros de tinta necessários
litros_de_tinta = area_a_pintar / 3

# Calcula a quantidade de latas de tinta necessárias
latas_de_tinta = math.ceil(litros_de_tinta / 18)

# Calcula o preço total das latas de tinta
preco_total = latas_de_tinta * 80

# Exibe o resultado para o usuário
print(f"Você precisará de {latas_de_tinta} latas de tinta.")
print(f"O preço total será de R$ {preco_total:.2f}.")
