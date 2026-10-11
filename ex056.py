# Desafio 056: Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. No final do programa, mostre:
# - A média de idade do grupo.
# - Qual é o nome do homem mais velho.
# - Quantas mulheres têm menos de 20 anos.

soma_idade = 0
maior_idade_homem = 0
nome_homem_mais_velho = ''
tot_mulher_sub20 = 0

for i in range(1,5):
    print(f'----- {i}ª PESSOA -----')
    nome = str(input('Nome: ')).strip()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: ')).strip().upper()

    soma_idade += idade

    # Lógica para o Homem Mais Velho
    if i == 1 and sexo == 'M':
        maior_idade_homem = idade
        nome_homem_mais_velho = nome
    if sexo == 'M' and idade > maior_idade_homem:
        maior_idade_homem = idade
        nome_homem_mais_velho = nome

    # Lógica para Mulheres com menos de 20 anos
    if sexo == 'F' and idade < 20:
        tot_mulher_sub20 += 1

media_idade = soma_idade / 4

print(f'A média de idade do grupo {media_idade:.1f}.')

if nome_homem_mais_velho != '':
    print(f'O homem mais velho tem {maior_idade_homem} anos e se chama {nome_homem_mais_velho}.')
else:
    print('Não há homens no grupo.')

print(f'Quantidade de mulheres que têm menos de 20 anos: {tot_mulher_sub20}')