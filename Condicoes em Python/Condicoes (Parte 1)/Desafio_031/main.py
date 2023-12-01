# Desenvolva um programa que pergunte a distância de uma viagem em Km. Calcule o preço da
# passagem, cobrando R$ 0,50 por Km para viagens de até 200 Km e R$ 0,45 para viagens
# mais longas

parameterDistance = 200

distance = float(input('Informe a distância da sua viagem (em Km): '))

if distance < 0:
    print('\033[31mVocê informou uma distância que não é válida')
elif distance <= parameterDistance:
    value = distance * 0.50
    print(f'O valor da sua passagem será de \033[34mR$ {value:.2f}')
else:
    value = distance * 0.45
    print(f'O valor da sua passagem será de \033[35mR$ {value:.2f}')
