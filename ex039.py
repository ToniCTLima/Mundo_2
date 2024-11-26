# Faça um programa que leia o ano de nascimento de um jovem e informe de acordo com sua idade:
# Se ele ainda vai se alistar ao serviço militar, se é hora de se alistar, se já passou do tempo do alistamento. O programa deve também mostrar o tempo que falta ou que passou do prazo.

nascimento = int(input('Digite a seu ano de nascimento: '))
idade = 2024 - nascimento
tempo_alistamento = 18 - idade
passou_prazo = idade - 18

#hora_alistamento =
if idade == 18:
    print(f'Você tem {idade} anos, está na hora de se alistar')
elif idade < 18:
    print(f'Você têm {idade} anos e deve se apresentar para o alistamento em {tempo_alistamento} ano(s):')
elif idade > 18:
    print(f'Você têm {idade}, seu prazo para o alistamento já passou em {passou_prazo} anos.')
