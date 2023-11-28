# Faça um programa que leia um ano qualquer e mostre se ele é BISSEXTO

import datetime

year = int(input('Que ano quer analisar? Coloque 0 para analisar o ano atual: '))

if year == 0:
    year = datetime.date.today().year

if year % 4 == 0:
    if year % 100 != 0 or year % 400 == 0:
        print(f'O ano {year} É BISSEXTO')
    else:
        print(f'O ano {year} NÃO É BISSEXTO')
else:
    print(f'O ano {year} NÃO É BISSEXTO')
