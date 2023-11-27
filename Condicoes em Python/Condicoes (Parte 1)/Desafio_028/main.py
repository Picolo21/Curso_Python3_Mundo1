# Escreva um programa que faça o computador "pensar" em um número inteiro entre 0 e 5 e peça
# para o usuário tentar descobrir qual foi o número escolhido pelo computador

# O programa deverá escrever na tela se o usuário venceu ou perdeu

import random

computerNumber = random.randint(0, 5)
userNumber = int(input('Escolha um número entre 0 e 5: '))

if userNumber < 0 or userNumber > 5:
    print(f'Você escolheu o número {userNumber}, e por ser um número fora do intervalo solicitado, você perdeu :(')
else:
    if computerNumber == userNumber:
        print(f'Você ganhou do computador. Vocês escolheram o número {userNumber}')
    else:
        print(f'Você perdeu do computador. Você escolheu {userNumber} e o computador escolheu {computerNumber}')
