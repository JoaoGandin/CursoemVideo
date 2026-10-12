# Desafio 058: Melhore o jogo do DESAFIO 028 onde o computador vai "pensar" em um número entre 0 e 10. Só que agora o jogador vai tentar adivinhar até acertar, mostrando no final quantos palpites foram necessários para vencer.

from random import randint

num = randint(0, 5)

print(f'Vou pensar em um número entre 0 e 5. Tende adivinhar...')

escolha = int(input('Tente adivinhas o número que eu escolhi: '))

while escolha != num:
    print('Errou!')
    escolha = int(input('Tente outro número: '))
print('Parabéns, você acertou!')