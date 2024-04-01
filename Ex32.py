# Leia um número n, inteiro e positivo,
# calcule e apresente: 𝐻 = 1 + 1/ 2 + 1/3 + 1/4 + ⋯ + 1/𝑛

num = int(input("Digite um número: "))
H = 0
for i in range(1, num + 1):
    H += 1 / i
print("H =", H)
print("Fim do programa")
