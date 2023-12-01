# Crie um programa que leia o nome completo de uma pessoa e diga se ela tem "SILVA" no nome

name = input('Digite seu nome completo: ')
name = name.upper()

if 'SILVA' in name:
    print(f'Seu nome possui SILVA? \033[32m{'SILVA' in name}\033[m')
else:
    print(f'Seu nome possui SILVA? \033[31m{'SILVA' in name}\033[m')

