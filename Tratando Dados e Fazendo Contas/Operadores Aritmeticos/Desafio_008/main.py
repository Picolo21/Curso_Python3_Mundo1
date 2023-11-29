# Escreva um programa que leia um valor em metros e o exiba convertido em centímetros e milímetros

number = float(input('Digite um valor em metros para calcular a conversão para centímetros e milímetros: '))

print(f'\033[34m{number:.2f}\033[m m é igual a \033[32m{number * 100}\033[m cm ou \033[33m{number * 1000}\033[m mm')
