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

print(f'Entre os números {numberOne:.2f}, {numberTwo:.2f} e {numberThree:.2f}:')
print(f'O MAIOR é o número {largestNumber}')
print(f'O MENOR é o número {smallestNumber}')
