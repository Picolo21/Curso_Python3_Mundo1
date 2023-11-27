# Faça um programa que leia um número de 1000 a 9999 e mostre na tela cada um dos
# dígitos separados

# Exemplo: Digite um número: 1834

# Unidade: 4
# Dezena: 3
# Centena: 8
# Milhar: 1

value = input('Digite um valor qualquer entre 1000 e 9999: ')

print(f'Unidade: {value[3]}')
print(f'Dezena: {value[2]}')
print(f'Centena: {value[1]}')
print(f'Milhar: {value[0]}')
