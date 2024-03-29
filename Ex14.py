# As maçãs custam R$ 1,30 cada se forem compradas menos de uma dúzia,
# e R$ 1,00 se forem compradas pelo menos 12.
# Escreva um programa que leia o número de maçãs compradas,
# calcule e escreva o custo total da compra.

preco_maca = 0

qtde_macas = int(input('Número de maças compradas: '))

if qtde_macas > 12:
    preco_maca = 1
else:
    preco_maca = 1.30

valor_total = qtde_macas * preco_maca

print(f'Valor total: R${valor_total}')
