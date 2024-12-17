# Refaça o exercício 009, mostrando a tabuada de um número que o usuário escolher, só que agora usando um laço for.

n = int(input('Digite um número para ver sua tabuada: '))
print(f'Tabuada do {n}:')
for c in range(1, 11):
    print(f'{n} x {c} = {n * c}')


# Solução do professor

num = int(input('Digite um número para ver sua tabuada: '))
for c in range(1, 11):
    print(f'{num} x {c} = {n * c}')
