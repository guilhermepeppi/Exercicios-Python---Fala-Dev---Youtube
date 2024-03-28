# Leia um número de 3 dígitos, determine e apresente o número invertido
# (exemplo: número informado = 123, número apresentado = 321).

numero = int(input('Digite o número de três dígitos: '))

# Separando os dígitos:
# Obtendo o primeiro dígito dividindo o número por 100
digito1 = numero // 100

# Obtendo o segundo dígito:
# Usando o operador de módulo (%) para obter os dois últimos dígitos
# e depois dividindo por 10 para extrair o segundo dígito
digito2 = (numero % 100) // 10

# Obtendo o terceiro dígito:
# Usando o operador de módulo (%) para obter o último dígito
digito3 = numero % 10

# Reorganizando os dígitos na ordem inversa
# e formando o número invertido
numero_invertido = digito3 * 100 + digito2 * 10 + digito1

# Exibindo o número invertido
print('Número invertido:', numero_invertido)
