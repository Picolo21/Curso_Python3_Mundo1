# Faça um programa que leia uma frase pelo teclado e mostre:

# 1º Quantas vezes aparece a letra "A"
# 2º Em que posição ela aparece pela primeira vez
# 3º Em que posição ela aparece pela última vez

phrase = input('Digite uma frase qualquer: ')
phrase = phrase.upper()

print(f'A letra "A" aparece {phrase.count('A')} vezes')
print(f'A letra "A" aparece pela 1ª vez na posição {phrase.find('A')}')
print(f'A letra "A" aparece pela última vez na posição {phrase.rfind('A')}')
