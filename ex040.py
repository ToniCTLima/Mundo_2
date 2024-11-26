# Crie um programa que leia duas notas de um aluno e calcule sua média, mostrando uma mensagem no final, de acordo com a média atingida:
# Média abaixo de 5.0: Reprovado, Média entre 5.0 e 6.9: Recuperação, Média 7.0 ou superior: Aprovado

nota_1 = float(input('Digite a primeira nota: '))
nota_2 = float(input('Digite a segunda nota: '))
media = (nota_1 + nota_2) / 2

if media > 7.0:
    print(f'Sua média foi {media:.2f}, você está APROVADO.')
elif media >= 5.0 and 6.9:
    print(f'Sua média foi de {media:.2f}, você está de RECUPERAÇÃO.')
else:
    print(f'Sua média foi de {media:.2f}, você foi REPROVADO.')




