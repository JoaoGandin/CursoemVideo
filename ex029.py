# Esse programa lê a velocidade de um carro. Se ele ultrapassar 80km/h ele toma multa. A multa custa R$7,00 por cada Km acima do limite.

vel = float(input("Qual a velocidade do carro em km/h? "))

if vel > 80:
    multa = (vel - 80) * 7
    print(f"Carro multado por excesso de velocidade!")
    print(f"Multa de R${multa:.2f}")
else:
    print("Velocidade permitida!")
