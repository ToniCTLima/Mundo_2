# Refaça o Desafio 35 dos triângulos, acrescentando o recurso de mostrar que tipo de triângulo será formado: Equilátero - todos os lados são iguais, Isóceles - dois lados são iguais, Escaleno - todos os lados diferentes.

s1 = float(input('Digite o valor do primeiro segmento: '))
s2 = float(input('Digite o valor do segundo segmento: '))
s3 = float(input('Digite o valor do terceiro segmento: '))
if s1 < s2 + s3 and s2 < s1 + s3 and s3 < s1 + s2:
    print('Os segmentos informados podem formar um triângulo ', end='')
    if s1 == s2 == s3:
        print('EQUILÁTERO')
    elif s1 != s2 != s3 != s1:
        print('ESCALENO')
    else:
        print('ISÓSCELES')
else:
    print('Os segmentos informados não podem formar um triângulo.')

