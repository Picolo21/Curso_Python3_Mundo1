# Crie um programa que leia o nome completo de uma pessoa e diga se ela tem "SILVA" no nome

name = input('Digite seu nome completo: ')
name = name.upper()

silvaStart = name.find('SILVA')

print(f'{name[silvaStart:(silvaStart + 5)] == 'SILVA'}')
