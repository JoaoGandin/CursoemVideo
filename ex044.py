# calculo do valor pago por um produto, considerando seu preço e a condição de pagamento.

preco_prod = float(input('Digite o valor do produto: '))
cond_pag = int(input('''1 - Dinheiro/Cheque
2 - Cartão
Qual a condição de pagamento: '''))
if cond_pag == 1:
    preco_prod = preco_prod - (0.1 * preco_prod)
    print(f'O valor a ser pago no produto é R$ {preco_prod:.2f}.')
elif cond_pag == 2:
    parcela = int(input('Parcela: '))
    if parcela >= 3:
        preco_prod = preco_prod + (0.2 * preco_prod)
        print(f'O valor a ser pago no produto é R$ {preco_prod:.2f}.')
    elif parcela == 1:
        preco_prod = preco_prod - (0.05 * preco_prod)
        print(f'O valor a ser pago no produto é R$ {preco_prod:.2f}.')
    else:
        print(f'O valor a ser pago no produto é R$ {preco_prod:.2f}.')
else:
    print('Informe uma condição de pagamento correta!')