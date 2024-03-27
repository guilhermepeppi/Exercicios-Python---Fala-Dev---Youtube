# Calcule e apresente o volume de uma lata de óleo (cilindro).

import math

raio_base = float(input("Digite o raio da base da lata de óleo (em centímetros): "))

altura = float(input("Digite a altura da lata de óleo (em centímetros): "))

volume = math.pi * raio_base**2 * altura

print("O volume da lata de óleo é:", volume, "cm³")
