# Faça um programa que leia o comprimento de cateto oposto e do cateto adjacente de um triângulo
# retângulo, calcule e mostre o comprimento da hipotenusa

import math

co = float(input('Digite o comprimento do cateto oposto: '))
ca = float(input('Digite o comprimento do cateto adjacente: '))

hi1 = ((co ** 2) + (ca ** 2)) ** (1 / 2)
hi2 = math.sqrt((math.pow(co, 2) + math.pow(ca, 2)))
hi3 = math.hypot(co, ca)

print('\n-> 1ª Resolução (sem IMPORT):')
print(f'O valor da hipotenusa é igual a {hi1:.2f}')

print('\n-> 2ª Resolução (com IMPORT usando métodos SQRT e POW):')
print(f'O valor da hipotenusa é igual a {hi2:.2f}')

print('\n-> 3ª Resolução (com IMPORT usando o método HYPOT):')
print(f'O valor da hipotenusa é igual a {hi3:.2f}')
