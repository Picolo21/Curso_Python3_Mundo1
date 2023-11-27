# Crie um programa que leia o nome de uma cidade e diga se ela começa
# ou não com o nome "SANTO"

cityName = input('Digite o nome da sua cidade: ')
cityName = cityName.upper().strip()

print(f'{cityName[0:5] == 'SANTO'}')
