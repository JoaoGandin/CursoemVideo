# Um professor quer sortear um dos seus quatro alunos para apagar o quadro. Faça um programa que ajude ele, lendo o nome deles e escrevendo o nome do escolhido

import random
aluno1 = input('Digite o primeiro aluno: ')
aluno2 = input('Digite o segundo aluno: ')
aluno3 = input('Digite o terceiro aluno: ')
aluno4 = input('Digite o quarto aluno: ')

print(random.choice([aluno1, aluno2, aluno3, aluno4]))
# o .choice() escolhe aleatoriamente um único elemento de uma sequência
# você pode ter uma lista já e colocar apenas a lista no choice ou fazer uma lista diretamente dentro do choice, que foi o  que eu fiz a cima
# exemplo de se você já tiver uma lista:
# alunos = ['João', 'Ludisvaldo', 'Ana', 'Pablo']
# random.choice(alunos)
