# Crie um programa que faça o computador jogar jokenpô com você.

from random import randint
itens = ('Pedra', 'Papel', 'Tesoura')
computador = randint(0,2)
print('''Suas opções:
[0] PEDRA
[1] PAPEL
[2] TESOURA ''')
jogador = int(input('Qual é a sua jogada? '))
print('-=' * 11)
print(f'O COMPUTADOR jogou {itens[computador]}')
print(f'O JOGADOR jogou {itens[jogador]}')
print('-=' * 11)

if computador == 0: # computador jogou PEDRA
    if jogador == 0:

    elif jogador == 1:

    elif jogador == 2:

    else:
        print('Jogada inválida.')

elif computador == 1: # computador jogou PAPEL
    if jogador == 0:

    elif jogador == 1:

    elif jogador == 2:

    else:
        print('Jogada inválida.')

elif computador == 2: # computador jogou TESOURA
    if jogador == 0:

    elif jogador == 1:

    elif jogador == 2:

    else:
        print('Jogada inválida.')




