# Desafio 049: Refaça o DESAFIO 009, mostrando a tabuada de um número que o usuário escolher, só que agora utilizando um laço for.

# Eu já tinha feito com o for...
num = int(input('Digite um número: '))

for i in range(1, 11):
    print(f'{num} x {i} = {num * i}')

