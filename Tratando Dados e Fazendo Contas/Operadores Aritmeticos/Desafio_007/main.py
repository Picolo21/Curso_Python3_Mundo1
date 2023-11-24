# Desenvolva um programa que leia as duas notas de um aluno, calcule e mostre a sua média

name = input('Digite seu nome: ')
numberOne = float(input('Digite o valor da 1ª nota: '))
numberTwo = float(input('Digite o valor da 2ª nota: '))

average = (numberOne + numberTwo) / 2

print(f'A média do aluno {name} é igual a {average}')
