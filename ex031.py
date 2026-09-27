# Esse programa pergunta a distânica em Km e calcula o preço da passagem, se for até 200km a passagem custa 0,50/Km se for maior 0,45/km

distancia = float(input("Qual é a distância da viagem: "))

if distancia <= 200:
    passagem = distancia * 0.50
    print(f"A passagem dessa viagem custa R$ {passagem:.2f}")
else:
    passagem = distancia * 0.45
    print(f"A passagem dessa viagem custa R$ {passagem:.2f}")
