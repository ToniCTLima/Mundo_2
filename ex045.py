# Crie um programa que faça o computador jogar jokenpô com você.

from random import randint
from time import sleep
itens = ('Pedra', 'Papel', 'Tesoura')
computador = randint(0,2)
print('''Suas opções:
[0] PEDRA
[1] PAPEL
[2] TESOURA ''')
jogador = int(input('Qual é a sua jogada? '))

if jogador not in [0, 1, 2]:
    print('Jogada inválida.')
    
else:

    print('JO')
    sleep(1)
    print('KEN')
    sleep(1)
    print('PO')
    print('-=' * 12)
    print(f'O COMPUTADOR jogou {itens[computador]}')
    print(f'O JOGADOR jogou {itens[jogador]}')
    print('-=' * 12)

if computador == 0: # computador jogou PEDRA
    if jogador == 0:
        print('EMPATE')
    elif jogador == 1:
        print('JOGADOR VENCE')
    elif jogador == 2:
        print('COMPUTADOR VENCE')
    else:
        print('Jogada inválida.')

elif computador == 1: # computador jogou PAPEL
    if jogador == 0:
        print('COMPUTADOR VENCE')
    elif jogador == 1:
        print('EMPATE')
    elif jogador == 2:
        print('JOGADOR VENCE')
    else:
        print('Jogada inválida.')

elif computador == 2: # computador jogou TESOURA
    if jogador == 0:
        print('JOGADOR VENCE')
    elif jogador == 1:
        print('COMPUTADOR VENCE')
    elif jogador == 2:
        print('EMPATE')
    else:
        print('Jogada inválida.')
