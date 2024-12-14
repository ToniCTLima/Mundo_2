# Faça um programa que calcule a soma entre todos os números ímpares que são múltiplos de 3 e que se encontram no intervalo de 1 até 500.


soma = 0
for numero in range(1, 501):
    if numero % 2 != 0 and numero % 3 == 0:
        soma += numero
print(f'A soma de todos os números ímpares múltiplos de 3, de 1 até 500 é: {soma}')


# Solução do Professor:

soma = 0 # Acumulador
cont = 0 # Contador
for c in range(1, 501, 2):
    if c % 3 == 0:
        soma = soma + c
        cont = cont + 1
print(f'A soma de todos os {cont} valores solicitados é: {soma}')
