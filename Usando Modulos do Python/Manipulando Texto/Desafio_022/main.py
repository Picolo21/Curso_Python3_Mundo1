# Crie um programa que leia o nome de uma pessoa e mostre:

# 1º O nome com todas as letras maiúsculas
# 2º O nome com todas as letras minúsculas
# 3º Quantas letras ao tem o nome completo (sem considerar espaços)
# 4º Quantas letras tem o primeiro nome

name = input('Informe seu nome completo: ')
nameWithoutSpace = name.replace(' ', '')

print(f'1º: \033[33m{name.upper()}\033[m')
print(f'2º: \033[34m{name.lower()}\033[m')
print(f'3º: O nome completo tem \033[31m{len(nameWithoutSpace)}\033[m letras sem contar os espaços')
print(f'4°: O primeiro nome tem \033[35m{len(name.split()[0])}\033[m letras')
