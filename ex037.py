# Escreva um programa que leia um número inteiro qualquer e peça para o usuário escolher qual será a base de conversão: binário, octal ou hexadecimal

num = int(input('Digite um número inteiro: '))

print('''Escolha uma base de conversão:')
– 1 para binário
- 2 para octal
- 3 para hexadecimal''')
opcao = int(input('Sua opção: '))

if opcao == 1:
    print(f'{num} convertido para \033[32mBINÁRIO\033[m é igual a {bin(num)[2:]}') #bin aparece 0b, como eu não quero que apareça, eu vou começar no terceiro índice até o final.
elif opcao == 2:
    print(f'{num} convertido para \033[32mOCTAL\033[m é igual a {oct(num)[2:]}')#octal aparece 0o, como eu não quero que apareça, eu vou começar no terceiro índice até o final.
elif opcao == 3:
    print(f'{num} convertido para \033[32mHEXADECIMAL\033[m é igual a {hex(num)[2:]}')#hex aparece 0x, como eu não quero que apareça, eu vou começar no terceiro índice até o final.
else:
    print('\033[31mOpção inválida, tente novamente!\033[m')
