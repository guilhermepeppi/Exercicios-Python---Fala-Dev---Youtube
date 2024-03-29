# Elabore um programa que leia notas de três avaliações de um aluno.
# A primeira avaliação tem peso 2, a segunda tem peso 3 e, a terceira, peso 5.
# Calcule a média do aluno. Se a média do aluno for maior ou igual a 6,
# o aluno está aprovado; caso contrário, o aluno está reprovado. Mostre o resultado da decisão.

nota1 = float(input('Digite a primeira nota: '))
nota2 = float(input('Digite a segunda nota: '))
nota3 = float(input('Digite a terceira nota: '))

media = ((nota1 * 2) + (nota2 * 3) + (nota3 * 5)) / 10

print(f'{media:.2f}')

if media >= 6:
    print('APROVADO')
else:
    print('REPROVADO')
