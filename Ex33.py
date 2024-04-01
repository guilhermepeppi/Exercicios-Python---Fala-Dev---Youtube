# A série de Fibonacci é formada pela sequência 1, 1, 2, 3, 5, 8, 13, 21, 34, ...
# Escreva um programa que apresente 8 termos da série de Fibonacci.

num1 = 1
num2 = 1
print(num1)
print(num2)
for i in range(3, 9):
    num3 = num1 + num2
    print(num3)
    num1 = num2
    num2 = num3
print("Fim do programa")
