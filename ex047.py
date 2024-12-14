# Crie um programa que mostre na tela todos os números pares que estão no intervalo entre um 1 e 50.

print('Os números pares entre 0 e 50 são: ')
for c in range(0, 51, 2): # para não mostrar o zero (0), poderia ter começado o laço com 2
    print(c, end=', ')


# Solução do Professor:
for n in range(2, 51, 2):
    print('.', end='')
    print(n, end=' ')

# Fazendo dessa forma aumentamos o número de iterações
# for n in range(1, 51):
#     print('.', end='') # mostrando o número de laços realizados
#     if n % 2 == 0:
#         print(n, end=' ')