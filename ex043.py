# IMC

peso = float(input('Digite seu peso: '))
altura = float(input('Digite sua altura, em metros: '))

imc = peso / altura ** 2
print(f'Seu IMC é {imc:.2f}.')

if imc < 18.5:
    print(f'Abaixo do peso!')
elif imc < 25:
    print(f'Peso ideal!')
elif imc < 30:
    print(f'Sobrepeso!')
elif imc < 40:
    print(f'Obesidade!')
else:
    print(f'Obesidade mórbida!')
