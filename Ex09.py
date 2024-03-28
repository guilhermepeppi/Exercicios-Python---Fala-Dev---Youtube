# Faça um programa que coloque dois nomes em ordem alfabética.

palavra1 = input('Digite um nome: ').capitalize()
palavra2 = input('Digite outro nome: ').capitalize()
if palavra1 < palavra2:
    print(palavra1, ',', palavra2)
else:
    print(palavra2, ',', palavra1)
