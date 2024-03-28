# Escreva um programa em Python que o usuário digita dois números inteiros
# e armazena em duas variáveis n1 e n2, o seu programa deve trocar em memória
# os valores dessas variáveis, de maneira que o valor de n1 seja igual ao de n2 e vice-versa,
# e depois deve exibir os números lidos com valores trocados.

# Recebendo os números do usuário
n1 = int(input('Digite o primeiro número inteiro: '))
n2 = int(input('Digite o segundo número inteiro: '))

# Trocando os valores das variáveis
temp = n1
n1 = n2
n2 = temp

# Exibindo os números com os valores trocados
print('Números com os valores trocados:')
print('Primeiro número:', n1)
print('Segundo número:', n2)
