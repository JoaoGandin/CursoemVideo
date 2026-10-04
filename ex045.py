# Jokenpô
from random import randint

npc_escolha = randint(1, 3)

npc = ''
if npc_escolha == 1:
    npc = 'Pedra'
elif npc_escolha == 2:
    npc = 'Papel'
elif npc_escolha == 3:
    npc = 'Tesoura'

player_escolha = int(input('''Faça uma escolha:
1 - Pedra
2 - Papel
3 - Tesoura
Escolha: '''))

player = ''
if player_escolha == 1:
    player = 'Pedra'
elif player_escolha == 2:
    player = 'Papel'
elif player_escolha == 3:
    player = 'Tesoura'
else:
    print('Opção inválida, tente novamente.')


if npc_escolha == player_escolha:
    print(f'{npc} X {player}')
    print(f'\033[1;33mEmpate')
elif npc_escolha == 1 and player_escolha == 2:
    print(f'{npc} X {player}')
    print(f'\033[1;32mVocê ganhou!')
elif npc_escolha == 2 and player_escolha == 3:
    print(f'{npc} X {player}')
    print(f'\033[1;32mVocê ganhou!')
elif npc_escolha == 3 and player_escolha == 1:
    print(f'{npc} X {player}')
    print(f'\033[1;32mVocê ganhou!')
else:
    print(f'{npc} X {player}')
    print(f'\033[1;31mVocê perdeu!')
