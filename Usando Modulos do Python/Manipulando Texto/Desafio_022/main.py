# Crie um programa que leia o nome de uma pessoa e mostre:

# 1º O nome com todas as letras maiúsculas
# 2º O nome com todas as letras minúsculas
# 3º Quantas letras ao tem o nome completo (sem considerar espaços)
# 4º Quantas letras tem o primeiro nome

name = input('Informe seu nome completo: ')
nameWithoutSpace = name.replace(' ', '')

print(f'1º: {name.upper()}')
print(f'2º: {name.lower()}')
print(f'3º: O nome completo tem {len(nameWithoutSpace)} letras sem contar os espaços')
print(f'4°: O primeiro nome tem {len(name.split()[0])} letras')
