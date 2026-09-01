# Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o último nome separadamente

nome = input('Digite seu nome completo: ')
nome_separado = nome.split()
primeiro_nome = nome_separado[0]
ultimo_nome = nome_separado[-1] # O -1 representa o primeiro elemento contando de trás para frente

print(f'Primeiro = {primeiro_nome}')
print(f'Último = {ultimo_nome}')