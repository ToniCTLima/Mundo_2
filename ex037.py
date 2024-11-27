# Escreva um programa que leia um número inteiro qualquer e peça para o usuário escolher qual será a base de conversão:
# 1 para binário / 2 para octal / 3 para hexadecimal

numero = int(input('Digite um número para ser convertido: '))

print('Escolha uma das opções pata conversão do número:')
print('1 para Binário')
print('2 para Octal')
print('3 para Hexadecimal')
opcao = int(input('Digite sua opção: '))

if opcao == 1:
    print(f'Você escolheu a opção 1, o número digitado {numero}, convertido para binário é: {bin(numero)}')

elif opcao == 2:
    print(f'Você escolheur a opção 2, o número digitado {numero} convertido para octal é: {oct(numero)}')

elif opcao == 3:
    print(f'Você escolheu a opção 3, o número digitado {numero} convertido para hexadecimal é: {hex(numero)}')

else:
    print('Opção inválida! Escolha entre as opções 1, 2 e 3')
