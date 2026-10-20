# Desafio 065: Crie um programa que leia vários números inteiros pelo teclado. No final da execução, mostre a média entre todos os valores e qual foi o maior e o menor valores lidos. O programa deve perguntar ao usuário se ele quer ou não continuar a digitar valores.


total = count = media = maior = menor = 0 # todas essas variáveis recebem 0
escolha = 'S'

while escolha != 'N':
    n = int(input('Digite um número: '))
    total += n
    count += 1
    if count == 1:
        maior = menor = n
    else:
        if n > maior:
            maior = n
        if n < menor:
            menor = n

    escolha = input('Quer continuar [S/N]?').upper()

media = total / count

print(f'Você digitou {count} números e a média foi {media:.2f}')
print(f'O maior número foi {maior} e o menor foi {menor} ')
