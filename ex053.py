# Desafio 053: Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo, desconsiderando os espaços.

print(f'{"=" * 11}Palíndromo{"=" * 11}')
entrada = str(input('Digite uma frase: '))
frase = entrada.replace(' ', '').lower()
invertido = frase[::-1]

if invertido == frase:
    print(f'A frase {entrada} é um PALÍNROMO')
else:
    print(f'A frase {entrada} NÃO é um PALÍNROMO')