# A confederação nacional de natação precisa de um programa que leia o ano de nascimento de um atleta e mostre sua categoria de acordo com a idade: Até 9 anos: Mirim, até 14 anos Infantil, até 19 anos Junior, até 20 anos: Sênior, acima: Master.

ano_nascimento = int(input('Digite seu ano de nascimento: '))
idade = 2024 - ano_nascimento

if idade <= 9:
    print(f'De acordo com sua idade {idade} anos, sua categoria é Mirim.')
elif idade >= 10 and idade <= 14:
    print(f'De acordo com sua idade {idade} anos, sua categoria é Infantil.')
elif idade >= 15 and idade < 19:
    print(f'De acordo com sua idade {idade} anos, sua categoria é Junior.')
elif idade <= 20:
    print(f'De acordo com sua idade {idade} anos, sua categoria é Sênior.')
else:
    print(f'De acordo com sua idade {idade} anos, sua categoria é Master.')

# Solução do professor:

from datetime import date
atual = date.today().year
nascimento = int(input('Ano de nascimento: '))
idade = atual - nascimento
print(f'O atleta tem {idade} anos.')
if idade <= 9:
    print('Classificação: MIRIM')
elif idade <= 14:
    print('Classificação: INFANTIL')
elif idade <= 19:
    print('Classidicação: JUNIOR')
elif idade <= 20:
    print('Classificação: SÊNIOR')
else:
    print('Classificação: MASTER')

