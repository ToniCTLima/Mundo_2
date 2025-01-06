# Desenvolva um programa que leia o primeiro termo e a razão de uma PA (Progressão Aritmética). No final, mostre os 10 primeiro termos dessa progressão.

# Solução do professor

primeiro = int(input('Primeiro termo: '))
razao = int(input('Razão: '))
decimo = primeiro + (10 - 1) * razao
for c in range(primeiro, decimo + razao, razao):
    print(f'{c}', end = '> ')
print('Acabou')


