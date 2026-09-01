# Faça um programa que leia uma frase pelo teclado e mostre:
# Quantas vezes aparece a letra "A"
# em que posição ela aparece a primeira vez
# em que posição ela aparece a última vez

frase = input('Digite uma frase: ')
frase_lower = frase.lower().replace(' ', '')
quantidade_a = frase.lower().count('a')


print(f'Na frase {frase} a letra "A" apareceu {quantidade_a} vezes')
print(f'Na frase {frase} a primeira letra "A" apareceu no {frase_lower.find("a")+1} caractere')
print(f'Na frase {frase} a primeira letra "A" apareceu no {frase_lower.rfind("a")+1} caractere')