# Crie um programa que leia o nome completo de uma pessoa e mostre:
# - O nome com todas as letras maiúsculas
# - O nome com todas minúsculas
# - Quantas letras ao todo (sem considerar espaços)
# - Quantas letra tem o primeiro nome.

nome = input('Digite seu nome completo: ').strip()

print(nome.upper())
print(nome.lower())
print('O seu nome tem ao todo', len(nome.replace(' ', '')))

nomeSeparado = nome.split()
primeiro_nome = nomeSeparado[0]
print(f'Seu primeiro nome é {primeiro_nome} e ele tem {len(primeiro_nome)} letras')
