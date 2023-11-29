# Desenvolva um programa que leia as duas notas de um aluno, calcule e mostre a sua média

name = input('Digite seu nome: ').strip()
numberOne = float(input('Digite o valor da 1ª nota: '))
numberTwo = float(input('Digite o valor da 2ª nota: '))

average = (numberOne + numberTwo) / 2

if average > 7:
    print(f'A média do aluno \033[36m{name}\033[m é igual a \033[32m{average}\033[m')
else:
    print(f'A média do aluno \033[36m{name}\033[m é igual a \033[31m{average}\033[m')
