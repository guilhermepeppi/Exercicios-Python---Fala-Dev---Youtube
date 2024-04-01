#  Escreva o trecho de um programa que lê
# e valida a nota de um aluno (0.0 ≤ nota ≤ 10.0).

nota = float(input("Digite a nota do aluno: "))
while nota < 0 or nota > 10:
    print("Nota inválida")
    nota = float(input("Digite a nota do aluno: "))
print("Nota válida")
