# Crie um programa que leia o nome de uma pessoa e diga se ela tem "SILVA" no nome

nome = input("Digite o nome completo da pessoa: ")
contem_silva = 'silva' in nome.lower()

print(f'O nome {nome} contém Silva? {contem_silva}')