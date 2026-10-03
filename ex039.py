from datetime import date

ano_atual = date.today().year
ano_nasc = int(input('Informe sua data de nascimento: '))
idade =  ano_atual - ano_nasc

print(f'Quem nasceu em {ano_nasc} tem {idade} em {date.today().year}.')

if idade == 18:
    print(f'Você tem que se alistar IMEDIATAMENTE')
elif idade < 18:
    saldo = 18 - idade
    print(f'Você ainda não tem 18 anos. Ainda faltam {saldo} anos para o alistamento')
    ano = ano_atual + saldo
    print(f'Seu alistamento será em {ano}')
else:
    saldo = idade - 18
    print(f'Você já deveria ter se alistado há {saldo} anos.')
    ano = ano_atual - saldo
    print(f'Seu alistamento foi em {ano}')

