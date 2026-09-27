# calculo de aumento no salário, se for maior que 1250, aumenta 10%, se não, 15%.

salario = float(input("Digite o salário atual do funcionário: "))

if salario > 1250:
    salario = salario + (salario * 0.10)
else:
    salario = salario + (salario * 0.15)

print(f"O salário do funcionário foi reajustado para R$ {salario:.2f}")
