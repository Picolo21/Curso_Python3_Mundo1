# Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida
# o primeiro e o último nome separadamente

# Exemplo: Ana Maria de Souza
# Primeiro = Ana
# Último = Souza

name = input('Digite seu nome completo: ')
name = name.split()

print(f'Primeiro = {name[0]}')
print(f'Último = {name[(len(name) - 1)]}')
