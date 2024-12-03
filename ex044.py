# Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e condição de pagamento: A vista dinheiro / cheque 10% de desconto. Em até 2x no cartão - preço normal. 3x ou mais no cartão 20% juros.

preco = float(input('Digite o preço do produto: '))

# condição de pgto
print('Escolha a forma de pagamento:')
print('1 A vista com 10% de desconto.')
print('2 Em 2x no cartão sem juros.')
print('3 Em 3x ou mais no cartão com juros de 20%')

forma_pgto = int(input('Escolha a forma de pagamento: '))

a_vista = preco - (preco * 10 / 100)
cartao_sem_juros = preco
dividido_3 = preco + (preco * 20 / 100)

if forma_pgto == 1:
    print(f'Você selecionou pagamento a vista com 10% de desconto, o valor do produto passa a ser: R$ {a_vista:.2f}')
elif forma_pgto == 2:
    print('Você selecionou pagamento em 2x no cartão sem juros. O preço não sofre alteração.')
elif forma_pgto == 3:
    print(f'Você selecionou o pagamento em 3x ou mais no cartão com juros de 20%. O valor do produto passa a ser: R$ {dividido_3:.2f}')
else:
    print('Opção inválida. Tente novamente.')

# Solução do professor:

preco = float(input('Preço das compras: R$ '))
print("""Formas de Pagamento
[1] à vista dinheiro/cheque 10% desconto
[2] à vista no cartão 5% desconto
[3] 2x no cartão
[4] 3x ou mais no cartão""")
opcao = int(input('Qual é a Forma de Pagamento? '))

if opcao == 1:
    total = preco - (preco * 10 / 100)
    print(f'Sua compra de R$ {preco:.2f}, com desconto de 10% vai custar R$ {total:.2f}')
elif opcao == 2:
    total = preco - (preco * 5 / 100)
    print(f'Sua compra de R$ {preco:.2f}, com desconto de 5% vai custar R$ {total:.2f}')
elif opcao == 3:
    total = preco
    parcela = total / 2
    print(f'Sua compra de R$ {preco:.2f} será parcelada em 2x SEM JUROS de R$ {parcela:.2f} ')
elif opcao == 4:
    total = preco + (preco * 20 / 100)
    tot_parc = int(input('Quantas parcelas? '))
    parcela = total / tot_parc
    print(f'Sua compra de R$ {preco} foi dividida COM JUROS em {tot_parc} parcelas de R$ {parcela:.2f} e o preço final será de R$ {total:.2f}')  
else:
    total = 0
    print('Opção inválida de pagamento. Tente novamente.')
