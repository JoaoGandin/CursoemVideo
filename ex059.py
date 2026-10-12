# Desafio 059: Crie um programa que leia dois valores e mostre um menu na tela:
# [ 1 ] somar
# [ 2 ] multiplicar
# [ 3 ] maior
# [ 4 ] novos números
# [ 5 ] sair do programa
# Seu programa deverá realizar a operação solicitada em cada caso.

n1 = int(input('Digite um valor: '))
n2 = int(input('Digite outro valor: '))
valor_final = 0

escolha = 0

while escolha != 5:
    print('''Escolha uma operação:
    [ 1 ] somar
    [ 2 ] multiplicar
    [ 3 ] maior
    [ 4 ] novos números
    [ 5 ] sair do programa''')
    escolha = int(input())
    if escolha != 5:
        if escolha == 1:
            valor_final = n1 + n2
            print(f'{n1} + {n2} = {valor_final}')
        elif escolha == 2:
            valor_final = n1 * n2
            print(f'{n1} x {n2} = {valor_final}')
        elif escolha == 3:
            if n1 > n2:
                valor_final = n1
                print(f'O maior número entre {n1} e {n2} é {valor_final}')
            else:
                valor_final = n2
                print(f'O maior número entre {n1} e {n2} é {valor_final}')
        elif escolha == 4:
            n1 = int(input('Digite um valor: '))
            n2 = int(input('Digite outro valor: '))
        else:
            print('Insira uma opção válida!')
