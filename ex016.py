# Crie um programa que leia um número Real qualquer pelo teclado e mostre a sua porção Inteira.

from math import trunc
num = float(input('Digite um valor real: '))
numTrunc = trunc(num)

print(f'A porção inteira do valor {num} é {numTrunc}')
