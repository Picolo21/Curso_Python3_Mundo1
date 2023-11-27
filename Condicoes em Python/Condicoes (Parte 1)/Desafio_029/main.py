# Escreva um programa que leia a velocidade de um carro

# Se ele ultrapassar 80 Km/h, mostre uma mensagem dizendo que ele foi multado

# A multa vai custar R$ 7,00 por cada Km acima do limite

speedLimit = 80

userSpeed = float(input('Informe a sua velocidade (em Km/h): '))

if userSpeed < 0:
    print('Você informou uma velocidade que não é válida')

if userSpeed > speedLimit:
    value = (userSpeed - speedLimit) * 7
    print(f'Você recebeu uma multa por ultrapassar o limite de velocidade. A multa será no valor de R$ {value:.2f}')
else:
    print(f'Você está dirigindo dentro dos limites estabelecidos. Sua velocidade é de {userSpeed:.2f} Km/h')
