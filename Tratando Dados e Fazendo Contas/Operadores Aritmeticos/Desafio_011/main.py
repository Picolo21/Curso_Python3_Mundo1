# Faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua área
# e a quantidade de tinta necessária para pintá-la, sabendo que cada litro de tinta, pinta uma
# área de 2,00 m²

height = float(input('Digite o valor da altura da parede: '))
width = float(input('Digite o valor da largura da parede: '))

area = height * width

print(f'A área da parede = \033[34m{area:.2f} m²\033[m e a quantidade de tinta necessaria para pintá-la será de \033[33m{(area / 2):.2f} L\033[m')
