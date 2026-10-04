# Calcule a média de um aluno somando as duas notas.

n1 = float(input('Digite a nota 1: '))
n2 = float(input('Digite a nota 2: '))
media = (n1 + n2) / 2

if media < 5:
    print(f'Sua média foi {media}, você está \033[31mREPROVADO!')
elif media >= 7:
    print(f'Sua média foi {media}, você está \033[32mAPROVADO!')
else:
    print(f'Sua média foi {media}, você está \033[33mRECUPERAÇÃO!')