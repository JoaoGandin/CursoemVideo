# Lê o comprimento de três retas e diga ao usuário se é possível ou não formar um triângulo.

a = int(input("Digite o comprimento da primeira reta: "))
b = int(input("Digite o comprimento da segunda reta: "))
c = int(input("Digite o comprimento da terceira reta: "))

if a + b > c and a + c > b and b + c > a:
    print(f"É possível formar um triângulo com as retas {a}, {b} e {c}")
else:
    print(f"Não é possível formar um triângulo com as retas {a}, {b} e {c}")