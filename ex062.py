# Desafio 062: Melhore o DESAFIO 061, perguntando para o usuário se ele quer mostrar mais alguns termos. O programa encerra quando ele disser que quer mostrar 0 termos.
primeiro_termo = int(input('Digite o primeiro termo da PA: '))
razao = int(input('Digite a razão dessa PA: '))
termo = primeiro_termo
count = 1
total = 0
mais = 10

while mais != 0:
    total = total + mais
    while count <= total:
        print(f'{termo}', end=' -> ')
        termo += razao
        count += 1
    print('PAUSA')
    mais = int(input('Quandos termos você quer mostrar a mais? '))
print('FIM')