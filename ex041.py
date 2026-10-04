# De acordo com a idade do atleta, mostre sua categoria.

from datetime import date

ano_atual = date.today().year
ano_nasc = int(input('Informe sua data de nascimento: '))
idade =  ano_atual - ano_nasc

if idade <= 9:
    print(f'Você tem {idade} anos, sua categoria é MIRIM.')
elif idade <= 14:
    print(f'Você tem {idade} anos, sua categoria é INFANTIL.')
elif idade <= 19:
    print(f'Você tem {idade} anos, sua categoria é JUNIOR.')
elif idade == 25:
    print(f'Você tem {idade} anos, sua categoria é SÊNIOR.')
else:
    print(f'Você tem {idade} anos, sua categoria é MASTER.')
