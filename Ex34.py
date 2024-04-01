#  Um dos jogos sugeridos para crianças acima de 6 anos é o PEDRA, PAPEL E TESOURA

# Como jogar:
# Dois participantes ficam um de frente para o outro e, ao mesmo tempo, jogam uma
# das mãos para frente representando um dos três símbolos: pedra (mão fechada), papel
# (mão aberta) ou tesoura (dedos indicador e médio estendidos).
# Para definir o vencedor segue-se a seguinte regra: pedra ‘quebra’ a tesoura; tesoura
# ‘corta’ o papel e papel ‘embrulha’ a pedra. Se ambas escolhem a mesma, há empate.
# Este jogo também chama-se Joquempô, jo-quem-pô.
# Sabendo como funciona o jogo crie uma variável para cada jogador que deve
# armazenar a opção escolhida pela criança (Pedra, Papel ou Tesoura) e apresente o
# resultado da jogada.

from random import randint

jogador = input("Jogador, escolha entre Pedra[1], Papel[2] ou Tesoura[3]: ")

computador = randint(1, 3)

if (jogador == "1" and computador == 1) or (jogador == "2" and computador == 2) or (jogador == "3" and computador == 3):
    print(f"Empate, o computador escolheu {computador}")
elif (jogador == "1" and computador == 3) or (jogador == "2" and computador == 1) or (jogador == "3" and computador == 2):
    print(f"Você venceu, o computador escolheu {computador}")
else:
    print(f"O computador venceu, o computador escolheu {computador}")
