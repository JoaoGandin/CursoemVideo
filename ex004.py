valor = input('Digite algo: ')
print(f'O tipo primitivo desse valor é {type(valor)}')
print(f'Só tem espaços? {valor.isspace()}') # mostra se só tem espaço
print(f'É um número? {valor.isnumeric()}') # retorna true se for número
print(f'É alfabético {valor.isalpha()}') # retorna true se for letra
print(f'É alfanúmerico? {valor.isalnum()}') # retorna true se for letra, número ou os dois
print(f'Está em maiúsculas? {valor.isupper()}') # retorna true se tudo estiver em caixa alta
print(f'Está em minúsculas? {valor.islower()}') # retorna true se tudo estiver em caixa baixa
print(f'Está capitalizada? {valor.istitle()}') # retorna true se a primeira letra estiver em maiúsucula e as demais em minúsculas