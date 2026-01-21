from random import randint
from time import sleep
import os

elementos = ['Pedra', 'Papel', 'Tesoura']
com = randint(0, 2)

print('''JOGADAS DISPONÍVEIS:
[0] PEDRA
[1] PAPEL
[2] TESOURA''')

jogador = int(input("ESCOLHA SUA JOGADA: "))
print('+=' * 10)

if 0 <= jogador <= 2:
    os.system('cls')

    print('+=' * 10)
    print("JO")
    sleep(0.7)
    print("KEN")
    sleep(0.7)
    print("PÔ!")
    sleep(0.7)
    
    print('+=' * 10)
    print("A COM JOGOU {}".format(elementos[com]))
    print("E O JOGADOR JOGOU {}".format(elementos[jogador]))
    print('+=' * 10)

    if jogador == com:
        print("EMPATOU!")
    elif (jogador == 0 and com == 1) or (jogador == 2 and com == 0) or (jogador == 1 and com == 2):
        print("A COM GANHOU JOGANDO {}!".format(elementos[com]))
    else:
        print("O JOGADOR GANHOU JOGANDO {}!".format(elementos[jogador]))
else:
    print("JOGADA INVÁLIDA! Escolha 0, 1 ou 2.")
