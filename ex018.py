# Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo.
import math

angulo = float(input('Digite o valor do ângulo: '))

# As funções sin(), cos() e tan() do módulo math esperam o ângulo em radianos
# Como o usuário informa o ângulo em graus, usamos math.radians() para fazer a conversão

seno = math.sin(math.radians(angulo)) # calcula o seno do ângulo
cosseno = math.cos(math.radians(angulo)) # calcula o cosseno do ângulo
tangente = math.tan(math.radians(angulo)) # calcula a tangente do ângulo

print(f'O seno desse ângulo é igual a {round(seno, 2)}')
print(f'O cosseno desse ângulo é igual a {round(cosseno, 2)}')
print(f'A tangente desse ângulo é igual a {round(tangente, 2)}')

# round(numero, casas decimais) -> round() arredonda números de 0 a 4 para baixo e de 6 a 9 para cima. Quando o valor é exatamente 5, ele arredonda para o número par mais próximo. Ex.: round(2.5) -> 2 e round(3.5) -> 4.

