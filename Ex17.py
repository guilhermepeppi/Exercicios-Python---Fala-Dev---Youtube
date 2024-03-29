# Elabore um programa que calcule e mostre o valor que deve ser pago por um produto,
# considerando que o usuário irá fornecer o preço normal de etiqueta e o código da  condição de pagamento.
# Utilize os códigos da tabela seguinte para ler qual a condição de pagamento escolhida e efetuar o cálculo adequado.
# Código
# Condições de pagamento
# 1 - À vista em dinheiro ou débito, recebe 10% de desconto
# 2 - À vista no cartão de crédito, recebe 5% de desconto
# 3 - Em 2 vezes, preço normal de etiqueta sem juros
# 4 - Em 3 vezes, preço normal de etiqueta mais juros de 10%

valor_final = 0

preco = float(input('Valor R$'))

print('=' * 30)
print('Condições de pagamento')
print('1 - À vista em dinheiro ou débito, recebe 10% de desconto')
print('2 - À vista no cartão de crédito, recebe 5% de desconto')
print('3 - Em 2 vezes, preço normal de etiqueta sem juros')
print('4 - Em 3 vezes, preço normal de etiqueta mais juros de 10%')

escolha = int(input('Digite a opcão da condição de pagamento: '))

if escolha == 1:
    valor_final = preco * 0.90
elif escolha == 2:
    valor_final = preco * 0.95
elif escolha == 3:
    valor_final = preco
else:
    valor_final = preco + (preco * 0.10)


print(f'Valor para pagamento: R${valor_final:.2f}')
