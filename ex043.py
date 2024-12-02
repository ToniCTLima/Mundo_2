# Desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule seu IMC e mostre seu status, de acordo com a tabela: Abaixo de 18.5 - Abaixo do peso, Entre 18.5 e 25 - Peso ideal, 25 até 30 Sobrepeso, 30 até 40 Obesidade, Acima de 40 Obesidade mórbida.

altura = float(input('Digite sua altura: '))
peso = float(input('Digite seu peso: '))
imc = peso / (altura ** 2)

if imc <= 18.5:
    print(f'Seu IMC é de {imc:.2f}, você está ABAIXO DO PESO.')
elif 18.5 < imc <= 24.99:
    print(f'Seu IMC é de {imc:.2f}, você está com o PESO IDEAL.')
elif 25 <= imc <= 29.99:
    print(f'Seu IMC é de {imc:.2f}, você está com SOBREPESO')
elif 30 <= imc <= 40.99:
    print(f'Seu IMC é de {imc:.2f}, você está com OBESIDADE.')
else:
    print(f'Seu IMC é de {imc:.2f}, você está com OBESIDADE MÓRBIDA.')
