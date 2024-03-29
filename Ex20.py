# Um comerciante comprou um produto e quer vendê-lo com um lucro de 45%
# se o valor da compra for menor que R$ 20,00; caso contrário, o lucro será de 30%.
# Escreva um programa em Python que receba o valor do produto e exiba o valor da venda.
# Recebendo o valor do produto

valor_compra = float(input("Digite o valor de compra do produto: "))

if valor_compra < 20:
    percentual_lucro = 0.45  # 45%
else:
    percentual_lucro = 0.30  # 30%

valor_venda = valor_compra * (1 + percentual_lucro)

print("O valor de venda do produto é: R$", valor_venda)
