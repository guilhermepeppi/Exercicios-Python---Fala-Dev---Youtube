# Sabe-se que o valor de cada 1000 litros de água
# corresponde a 2% do salário mínimo. Elabore um programa que
# receba o valor do salário mínimo e a quantidade
# de água consumida em uma residência por mês. Calcule e mostre:
# a) O valor da conta de água.
# b) O valor a ser pago com desconto de 15%.

# Recebendo os valores do usuário
salario_minimo = float(input('Valor do salário mínimo: '))
qtde_agua_consumida = float(input('Quantidade de água consumida: '))

# Calculando o valor por litro de água
valor_por_litro = (salario_minimo * 0.02) / 1000

# Calculando o valor total da conta de água
valor_total = valor_por_litro * qtde_agua_consumida

# Calculando o valor com desconto de 15%
valor_com_desconto = valor_total * 0.85

# Exibindo os resultados
print('A)------')
print(f'Valor da conta de água: R${valor_total:.2f}')

print('B)------')
print(f'Valor da conta de água COM DESCONTO: R${valor_com_desconto:.2f}')
