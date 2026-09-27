# programa lê 3 números e mostra qual é o maior e o menor entre eles

num1 = int(input("Digite um número: "))
num2 = int(input("Digite outro número: "))
num3 = int(input("Digite outro número: "))
maior = num1
menor = num1

if num2 > maior:
    maior = num2
if num2 < menor:
    menor = num2

if num3 > maior:
    maior = num3
if num3 < menor:
    menor = num3


print(f"Maior: {maior}")
print(f"Menor: {menor}")