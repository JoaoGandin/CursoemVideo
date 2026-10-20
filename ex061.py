# Desafio 061: Refaça o DESAFIO 051, lendo o primeiro termo e a razão de uma PA, mostrando os 10 primeiros termos da progressão usando a estrutura while.

primeiro_termo = int(input('Digite o primeiro termo da PA: '))
razao = int(input('Digite a razão dessa PA: '))
decimo_termo = primeiro_termo + (10 - 1) * razao
termo = primeiro_termo

while primeiro_termo <= decimo_termo:
    print(f'{primeiro_termo}', end=' -> ')
    primeiro_termo += razao
print('ACABOU')