# Receba a quantidade de dinheiro, em reais, que uma pessoa tem
# para fazer uma viagem ao exterior. Receba, também, o valor da cotação do dólar do dia.
# Calcule e apresente o valor convertido em dólares.

valor_reais = float(input('Valor em reais: '))
cotacao_dolar = float(input('Cotação do dólar: '))

valor_convertido = valor_reais / cotacao_dolar

print(f'O valor convertido em dólares é: {valor_convertido:.2f} USD')
