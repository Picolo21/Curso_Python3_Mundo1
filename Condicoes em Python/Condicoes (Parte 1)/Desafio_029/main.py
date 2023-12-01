# Escreva um programa que leia a velocidade de um carro

# Se ele ultrapassar 80 Km/h, mostre uma mensagem dizendo que ele foi multado

# A multa vai custar R$ 7,00 por cada Km acima do limite

speedLimit = 80

userSpeed = float(input('Informe a sua velocidade (em Km/h): '))

if userSpeed < 0:
    print('\033[31mVocê informou uma velocidade que não é válida\033[m')

if userSpeed > speedLimit:
    value = (userSpeed - speedLimit) * 7
    print(f'\033[31mVocê recebeu uma multa por ultrapassar o limite de velocidade\033[m. A multa será no valor de \033[31mR$ {value:.2f}\033[m')
else:
    print(f'\033[34mVocê está dirigindo dentro dos limites estabelecidos\033[m. Sua velocidade é de \033[32m{userSpeed:.2f} Km/h\033[m')
