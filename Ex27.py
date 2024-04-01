# Escreva um programa que leia duas notas de n alunos.
# Calcule e apresente:
#    - a média de cada aluno (aritmética);
#    - a quantidade de alunos aprovados (média superior ou igual a 6.0);
#    - a quantidade de alunos reprovados (média inferior a 6.0).
# Obs:
#  n será um número informado pelo usuário que representa a quantidade de alunos da turma.
#  Validar:
#       - quantidade de alunos(n): só aceitar de 1 a 200;
#       - nota: só aceitar de 0.0 a 10.0

while True:
    try:
        n = int(input("Informe a quantidade de alunos: "))
        if n < 1 or n > 200:
            raise ValueError("A quantidade de alunos deve ser entre 1 e 200.")
        break
    except ValueError as e:
        print(e)

aprovados = 0
reprovados = 0

for i in range(1, n+1):
    while True:
        try:
            nota1 = float(input(f"Informe a primeira nota do aluno {i}: "))
            if nota1 < 0.0 or nota1 > 10.0:
                raise ValueError("A nota deve ser entre 0.0 e 10.0.")
            break
        except ValueError as e:
            print(e)

    while True:
        try:
            nota2 = float(input(f"Informe a segunda nota do aluno {i}: "))
            if nota2 < 0.0 or nota2 > 10.0:
                raise ValueError("A nota deve ser entre 0.0 e 10.0.")
            break
        except ValueError as e:
            print(e)

    media = (nota1 + nota2) / 2
    print(f"A média do aluno {i} é {media:.2f}")
    if media >= 6.0:
        aprovados += 1
    else:
        reprovados += 1
