# Crie um programa que leia o nome de uma cidade e diga se ela começa
# ou não com o nome "SANTO"

cityName = input('Digite o nome da sua cidade: ')
cityName = cityName.upper().strip()

if cityName[0:5] == 'SANTO':
    print(f'A sua cidade começa com SANTO? \033[32m{cityName[0:5] == 'SANTO'}\033[m')
else:
    print(f'A sua cidade começa com SANTO? \033[31m{cityName[0:5] == 'SANTO'}\033[m')

