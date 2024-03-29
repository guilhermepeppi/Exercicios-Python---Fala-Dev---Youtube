# Escreva um programa que faz a leitura de três valores reais (A, B e C),
# representando os coeficientes de uma equação do 2o. grau,
# calcula o valor do delta e os valores das raízes reais, caso existam.

import math

A = float(input("Digite o coeficiente A da equação: "))
B = float(input("Digite o coeficiente B da equação: "))
C = float(input("Digite o coeficiente C da equação: "))

delta = B**2 - 4*A*C

if delta >= 0:
    raiz_delta = math.sqrt(delta)
    x1 = (-B + raiz_delta) / (2*A)
    x2 = (-B - raiz_delta) / (2*A)

    # Exibição das raízes
    print("As raízes da equação são:")
    print("x1 =", x1)
    print("x2 =", x2)
else:
    print("A equação não possui raízes reais.")
