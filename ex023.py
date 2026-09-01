#Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos dígitos separados
# Ex.: Digite um número: 1834
# unidade: 4
# dezena: 3
# centena: 8
# milhar: 1

num = int(input("Digite um número de 0 a 9999: "))
# 1834 // 1 = 1834 O resto da divisão de 1834 por 10 é 4
un = num // 1 % 10

# 1834 // 10 = 183 O resto da divisão de 183 por 10 é 3
dez = num // 10 % 10

# 1834 // 100 = 18 O resto da divisão de 18 por 10 é 8
cent = num // 100 % 10

# 1834 // 1000 = 1 O resto da divisão de 1 por 10 é 1
mil = num // 1000 % 10
print(f'Unidade: {un}')
print(f'Dezena: {dez}')
print(f'Centena: {cent}')
print(f'Milhar: {mil}')