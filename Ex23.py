# Escreva um programa para escrever na tela a contagem regressiva
# do lançamento de um foguete. O programa deve exibir 10, 9, 8, ..., 1,0 e Fogo!

from time import sleep

print("Contagem regressiva para o lançamento do foguete!")
for i in range(10, -1, -1):
    print(i)
    sleep(1)
print("Fogo!")
