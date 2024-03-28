# Escreva um programa que pergunte a quantidade de km percorridos
# por um carro alugado pelo usuário, assim como a quantidade de dias
# pelos quais o carro foi alugado. Calcule o preço a pagar, sabendo que o carro
# custa R$ 60,00 por dia e R$ 0,15 por km rodado.

qtde_km_percorridos = float(input('Quantidade de km percorridos: '))
qtde_dias_alugados = float(input('Quantidade de dias alugados: '))

valor_total_percorrido = qtde_km_percorridos * 0.15
valor_total_dias = qtde_dias_alugados * 60
valor_total = valor_total_percorrido + valor_total_dias

print(f'Valor total a pagar: R${valor_total:.2f}')
