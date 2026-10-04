# Lê o comprimento de três retas e diga ao usuário se é possível ou não formar um triângulo.

a = int(input("Digite o comprimento da primeira reta: "))
b = int(input("Digite o comprimento da segunda reta: "))
c = int(input("Digite o comprimento da terceira reta: "))

if a + b > c and a + c > b and b + c > a:
    print(f"É possível formar um triângulo com as retas {a}, {b} e {c}")
    if a == b and a == c:
        print(f'Tipo desse triângulo: Equilátero.')
    elif a == b or a == c or b == c:
        print(f'Tipo desse triângulo: Isóceles.')
    else:
        print(f'Tipo desse triângulo: Escaleno.')
else:
    print(f"Não é possível formar um triângulo com as retas {a}, {b} e {c}")
