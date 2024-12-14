# Faça um programa que mostre na tela uma contagem regressiva para o estouro de fogos de artifício, indo de 10 até 0, com uma pausa de 1 segundo entre eles.

from time import sleep

for c in range(10, -1, -1):
    print(c)
    sleep(1)
print('BOOOOM \U0001F4A5 \U0001F4A5 \U0001F4A5')

# Solução do professor:

from time import sleep

for count in range(10, -1, -1):
    print(count)
    sleep(1)
print('BUM!  BUM!  POOOW! \U0001F4A5 \U0001F4A5 \U0001F4A5')



