# Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa. O programa vai perguntar o valor da casa, o salário do comprador e em quantos anos ele vai pagar.
# Calcule o valor da prestação mensal, sabendo que ela não pode exceder 30% do salário ou então o empréstimo será negado.

valor_casa = float(input('Digite o valor da casa: '))
salario_comprador = float(input('Digite o seu salário: '))
anos = int(input('Digite em quantos anos vai pagar: '))

total_meses = anos * 12
prestacao_mensal = valor_casa / total_meses
limite_salario = salario_comprador * 0.30

print(f'Para pagar uma casa de R$ {valor_casa:.2f} em {anos} anos')
print(f'a prestação será de R${prestacao_mensal:.2f} por mês')
print(f'O limite máximo permitido para o seu salário é R$ {limite_salario:.2f}.')

if prestacao_mensal > limite_salario:
    print('\033[1;31mEmpréstimo negado!')
else:
    print('\033[1;32mEmpréstimo aprovado!')