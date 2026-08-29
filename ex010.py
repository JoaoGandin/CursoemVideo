# Crie um programa que leia quanto dinheiro uma pessa tem na carteira e mostre quantos dólares ela pode comprar

real = float(input('Digite quantos reais você tem: '))
dolar = real / 3.27

print(f'Você pode comprar U${dolar:.2f} dólares!')