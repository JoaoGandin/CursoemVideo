# Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de uim triângulo retângulo, calcuile e mostre o comprimento da hipotenusa: h² = cop² + cadj²

import math
catAdj = int(input('Digite o cateto adjacente: '))
catOp = int(input('Digite o cateto oposto: '))
catTotal = math.pow(catAdj, 2) + math.pow(catOp, 2)
hipot = math.sqrt(catTotal)

print(f'A hipotenusa do triângulo retângulo, com o cateto adjacente de {catAdj} e o cateto oposto de {catOp} é igual a {hipot:.2f}')

# A IDE me deu essa sugestão de fazer assim para achar a hipotenusa com a função hypot, mas eu não sabia que isso existia:
# print(math.hypot(catAdj, catOp))


