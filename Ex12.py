# Leia as coordenadas (x,y) de dois pontos no plano cartesiano,
# calcule e mostre a distância entre os dois pontos.
import math


def calcular_distancia(x1, y1, x2, y2):
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)


# Solicitar as coordenadas dos pontos ao usuário
x1 = float(input("Digite a coordenada x do primeiro ponto: "))
y1 = float(input("Digite a coordenada y do primeiro ponto: "))
x2 = float(input("Digite a coordenada x do segundo ponto: "))
y2 = float(input("Digite a coordenada y do segundo ponto: "))

# Calcular a distância entre os dois pontos
distancia = calcular_distancia(x1, y1, x2, y2)

# Mostrar a distância
print("A distância entre os pontos ({}, {}) e ({}, {}) é: {:.2f}".format(x1, y1, x2, y2, distancia))
