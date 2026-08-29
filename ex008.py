# Escreva um programa que leia um valor em metros e o exiba covertido em centímetros e milímetros

m = float(input('Digite o valor em metros: '))

print(f'{m} metros em: '
      f'\n Quilômetro: {m/1000}km'
      f'\n Hectômetro: {m/100}hm'
      f'\n Decâmetro: {m/10}dam'
      f'\n Decímetro: {m*10}dm'
      f'\n Centímetro: {m*100}cm'
      f'\n Milímetro: {m*1000}mm')


