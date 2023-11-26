# Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno
# e tangente desse ângulo

import math

angle = float(input('Digite o valor do ângulo que deseja calcular: '))

sin = math.sin(math.radians(angle))
cos = math.cos(math.radians(angle))
tan = math.tan(math.radians(angle))

print(f'\nO ângulo {angle:.2f}° tem:')
print(f'SENO = {sin:.2f}')
print(f'COSSENO = {cos:.2f}')
print(f'TANGENTE = {tan:.2f}')
