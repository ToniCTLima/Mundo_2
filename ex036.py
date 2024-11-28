# Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa. O programa vai perguntar o valor da casa, o salário do comprador e em quantos anos ele vai pagar.
# Calcule o valor da prestação mensal, sabendo que ela não pode exceder 30% do salário ou então o empréstimo será negado.

# valor da casa
valor_casa = float(input('Digite o valor da casa: '))

# valor do Salário com desconto de 30%
salario = float(input('Digite o valor do seu salário: '))
desconto_30 = salario * 30 / 100


# tempo da prestação
anos = int(input('Digite em quantos anos quer pagar a casa? '))
# convertendo o número de anos para meses
anos_meses = anos * 12
# valor da prestação
prest_mensal = valor_casa / anos_meses

print(f'O valor da casa é: R$ {valor_casa:.2f}')
print(f'Seu salário é de R${salario:.2f}')
print(f'O valor da prestação mensal será de: R$ {prest_mensal:.2f}')
print(f'O limite que pode ser descontado do seu salário é R${desconto_30:.2f}')

if prest_mensal > desconto_30:
    print('Seu financiamento não pode ser aprovado.')
else:
    print('Seu financiamento foi aprovado')

# Solução do professor:

casa = float(input('Valor da casa: R$ '))
salário = float(input('Salário do comprador: R$'))
anos = int(input('Quantos anos de financiamento? '))
prestacao = casa / (anos * 12)
minimo = salario * 30 /100
print('Para pagar uma casa de R$ {:.2f} em {} anos'.format(casa, anos), end='')
print(' a prestação será de R$ {:.2f}'.format(prestacao))
if prestacao <= minimo:
    print('Empréstimo concedido!')
else:
    print('Empréstimo negado!')









