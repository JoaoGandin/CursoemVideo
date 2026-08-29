# Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento

salario = float(input('Digite o salário do funcionário: '))
novoSalario = salario + (salario * 0.15)

print(f'O novo salário do funcionário, depois de 15% de aumento, é {novoSalario:.2f}')