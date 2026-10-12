# Desafio 057: Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores 'M' ou 'F'. Caso esteja errado, peça a digitação novamente até ter um valor correto.

sexo = input('Qual o seu sexo? [M/F]: ')

while sexo != 'M' and sexo != 'F':
    print('Opção inválida. Digite novamente!')
    sexo = input('Qual o seu sexo? [M/F]: ')
print(f'Sexo {sexo} registrado com sucesso!')
