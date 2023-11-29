# Faça um programa que leia um número inteiro e mostre na tela o seu sucessor e o seu antecessor

number = int(input('Digite um número inteiro qualquer: '))
print(f'O sucessor de \033[34m{number}\033[m é \033[31m{number + 1}\033[m')
print(f'O antecessor de \033[34m{number}\033[m é \033[32m{number + 1}\033[m')
