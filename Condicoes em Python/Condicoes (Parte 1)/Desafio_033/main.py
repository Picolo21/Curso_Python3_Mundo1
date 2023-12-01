# Faça um programa que leia três números e mostre qual é o MAIOR e qual é o MENOR

numberOne = float(input('Digite o 1º valor: '))
numberTwo = float(input('Digite o 2º valor: '))
numberThree = float(input('Digite o 3º valor: '))

largestNumber = 0
smallestNumber = 0

if numberOne > numberTwo:
    if numberOne > numberThree:
        largestNumber = numberOne
        if numberTwo < numberThree:
            smallestNumber = numberTwo
        else:
            smallestNumber = numberThree
    else:
        largestNumber = numberThree
        smallestNumber = numberTwo
else:
    if numberTwo > numberThree:
        largestNumber = numberTwo
        if numberOne < numberThree:
            smallestNumber = numberOne
        else:
            smallestNumber = numberThree
    else:
        largestNumber = numberThree
        smallestNumber = numberOne

print(f'Entre os números \033[34m{numberOne:.2f}\033[m, \033[31m{numberTwo:.2f}\033[m e \033[35m{numberThree:.2f}\033[m:')
print(f'\033[32mO MAIOR é o número {largestNumber:.2f}')
print(f'\033[33mO MENOR é o número {smallestNumber:.2f}')
