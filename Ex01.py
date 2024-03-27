# Faça um programa que receba o custo de um espetáculo teatral
# e o preço do convite desse espetáculo.
# Esse programa deve calcular e mostrar:
# a) A quantidade de convites que devem ser vendidos
# para que pelo menos o custo do espetáculo seja alcançado.
# b) A quantidade de convites que devem ser vendidos
# para que se tenha um lucro de 23%.

custo_espetaculo = float(input('Custo do espetáculo: '))
preco_convite = float(input('Preço do convite: '))

cobrir_Valor = custo_espetaculo / preco_convite

lucro = 1.23 * (custo_espetaculo / preco_convite)

texto_cobrir = f'B) A quantidade de convites que devem ser vendidos para que se tenha um lucro de 23%: {lucro:_.2f}'
texto_lucro = f'A) A quantidade de convites necessários para cobrir os custos do espetáculo: {cobrir_Valor:_.2f}'
texto_cobrir = texto_cobrir.replace('.', ',').replace('_', '.')
texto_lucro = texto_lucro.replace('.', ',').replace('_', '.')
print(f'O lucro foi de {texto_cobrir}')
print(f'O lucro foi de {texto_lucro}')
