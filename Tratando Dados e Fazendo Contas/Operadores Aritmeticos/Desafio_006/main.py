# Crie um algoritmo que leia um número e mostre o seu dobro, triplo e raiz quadrada

number = float(input('Digite um número qualquer: '))

print(f'O dobro de \033[33m{number:.2f}\033[m é igual a \033[32m{(number * 2):.2f}\033[m')
print(f'O triplo de \033[33m{number:.2f}\033[m é igual a \033[34m{(number * 3):.2f}\033[m')
print(f'A raiz quadrada de \033[33m{number:.2f}\033[m é igual a \033[35m{number ** (1 / 2):.2f}\033[m')
