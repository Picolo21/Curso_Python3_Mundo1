# Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se elas podem ou
# não formar um triângulo

lineOne = float(input('Informe o valor da 1ª reta: '))
lineTwo = float(input('Informe o valor da 2ª reta: '))
lineThree = float(input('Informe o valor da 3ª reta: '))

if (lineOne < (lineTwo + lineThree)) and (lineTwo < (lineOne + lineThree)) and (lineThree < (lineOne + lineTwo)):
    print(f'As retas com comprimento {lineOne:.2f}, {lineTwo:.2f} e {lineThree:.2f} PODEM FORMAR um triângulo')
else:
    print(f'As retas com comprimento {lineOne:.2f}, {lineTwo:.2f} e {lineThree:.2f} NÃO PODEM FORMAR um triângulo')
