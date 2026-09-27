# Programa que o algoritmo escolhe um número entre 0 e 5
from random import randint

num = randint(0, 5)

print(f'Vou pensar em um numero entre 0 e 5')
escolha = int(input("Escolha um número de 0 a 5: "))

if escolha == num:
    print(f"Parabéns, você acertou!")
else:
    print(f"Você errou, o número era {num}.")
