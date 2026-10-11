# Desafio 054: Crie um programa que leia o ano de nascimento de sete pessoas. No final, mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores.
from datetime import date
maior = 0
menor = 0
for i in range(0,7):
    ano = int(input('Digite o ano de nascimento: '))
    idade = date.today().year - ano
    if idade >= 18:
        maior += 1
    else:
        menor += 1
print(f'{maior} já são de maior e {menor} ainda é de menor.')
