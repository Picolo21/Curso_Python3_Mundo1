# Crie um programa que leia um número inteir e mostre na tela se ele é PAR ou ÍMPAR

number = int(input('Informe um número inteiro qualquer: '))

if number % 2 == 0:
    print(f'O número {number} é \033[34mPAR')
else:
    print(f'O número {number} é \033[35mÍMPAR')
