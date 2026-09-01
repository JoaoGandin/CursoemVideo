# Crie um programa que leia o nome de uma cidade e diga se ela começa ou não com o nome "SANTO"

cid = input("Digite o nome da cidade: ")
cid_separado = cid.split()
primeiro_nome_cid = cid_separado[0]

contem_santo = 'santo' in primeiro_nome_cid.lower()

print(f'A cidade {cid} começa com "SANTO": {contem_santo}')