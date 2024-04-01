# Escreva o trecho de um programa que lê e
# valida a resposta da seguinte pergunta: “Deseja continuar (s/n)?

resposta = input("Deseja continuar (s/n)? ")
while resposta not in "sn":
    resposta = input("Deseja continuar (s/n)? ")
print("Resposta válida!")
