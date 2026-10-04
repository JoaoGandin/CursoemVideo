# Jokenpô
from random import randint

# Vai usar o índice para esolher
itens = ('Pedra', 'Papel', 'Tesoura')

npc_escolha = randint(0, 2)

player_escolha = int(input('''Faça uma escolha:
0 - Pedra
1 - Papel
2 - Tesoura
Escolha: '''))

if npc_escolha == player_escolha:
    print(f'{itens[npc_escolha]} X {itens[player_escolha]}')
    print(f'\033[1;33mEmpate')
elif npc_escolha == 1 and player_escolha == 2:
    print(f'{itens[npc_escolha]} X {itens[player_escolha]}')
    print(f'\033[1;32mVocê ganhou!')
elif npc_escolha == 2 and player_escolha == 3:
    print(f'{itens[npc_escolha]} X {itens[player_escolha]}')
    print(f'\033[1;32mVocê ganhou!')
elif npc_escolha == 3 and player_escolha == 1:
    print(f'{itens[npc_escolha]} X {itens[player_escolha]}')
    print(f'\033[1;32mVocê ganhou!')
else:
    print(f'{itens[npc_escolha]} X {itens[player_escolha]}')
    print(f'\033[1;31mVocê perdeu!')
