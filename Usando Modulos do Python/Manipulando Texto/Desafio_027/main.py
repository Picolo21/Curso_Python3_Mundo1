# Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida
# o primeiro e o último nome separadamente

# Exemplo: Ana Maria de Souza
# Primeiro = Ana
# Último = Souza

name = input('Digite seu nome completo: ').strip()
name = name.split()

print(f'Primeiro = \033[34m{name[0]}\033[m')
print(f'Último = \033[32m{name[(len(name) - 1)]}\033[m')
