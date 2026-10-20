# Desafio 060: Faça um programa que leia um número qualquer e mostre o seu fatorial.
# Ex:
# 5! = 5x4x3x2x1 = 120

num_fat = int(input('Digite um número: '))
num = num_fat
total = num_fat

while num_fat > 1:
    total = total * (num_fat - 1)
    num_fat -= 1
print(f'O fatorial de {num} é {total}.')