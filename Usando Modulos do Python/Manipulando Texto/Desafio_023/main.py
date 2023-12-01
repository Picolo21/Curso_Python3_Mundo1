# Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos
# dígitos separados

# Exemplo: Digite um número: 1834

# Unidade: 4
# Dezena: 3
# Centena: 8
# Milhar: 1

value = int(input('Digite um valor qualquer entre 0 e 9999: '))

u = value // 1 % 10
d = value // 10 % 10
c = value // 100 % 10
m = value // 1000 % 10

print(f'Unidade: \033[33m{u}\033[m')
print(f'Dezena: \033[34m{d}\033[m')
print(f'Centena: \033[32m{c}\033[m')
print(f'Milhar: \033[31m{m}\033[m')
