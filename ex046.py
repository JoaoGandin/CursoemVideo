# Desafio 046: Faça um programa que mostre na tela uma contagem regressiva para o estouro de fogos de artifício, indo de 10 até 0, com uma pausa de 1 segundo entre eles.
from time import sleep

print(f'\33[36m{"=" * 11}Contagem Regressiva{"=" * 11}')
for i in range(0, 10):
    print(i+1)
    sleep(1)
print(f'\33[34mBOOM!')