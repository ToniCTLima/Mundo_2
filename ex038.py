# Escreva um programa que leia dois números inteiros e compare-os, mostrando na tela uma mensagem:
# O primeiro valor é maior, o segundo valor é maior, Não existe valor maior, os dois são iguais.

valor_1 = int(input('Digite um número: '))
valor_2 = int(input('Digite outro número: '))
if valor_1 > valor_2:
    print(f'O primeiro valor digitado {valor_1} é maior que  {valor_2}')
elif valor_2 > valor_1:
    print(f'O segundo valor digitado {valor_2} é maior que  {valor_1}')
elif valor_1 == valor_2:
    print(f'Não existe valor maior, os dois valores são iguais.')
