# Crie um programa que leia um número real qualquer pelo teclado e mostre na tela a sua porção inteira

# Exemplo:

# Digite um número: 6.127
# O número 6.127 tem a parte inteira 6

import math

number = float(input('Digite um número real qualquer: '))

print('\n-> Calculando com o IMPORT:')
print(f'O número {number} tem a parte inteira {math.trunc(number)}')

print('\n-> Calculando sem o IMPORT:')
print(f'O número {number} tem a parte inteira {int(number)}')
