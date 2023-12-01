# Faça um programa que leia uma frase pelo teclado e mostre:

# 1º Quantas vezes aparece a letra "A"
# 2º Em que posição ela aparece pela primeira vez
# 3º Em que posição ela aparece pela última vez

phrase = input('Digite uma frase qualquer: ').strip()
phrase = phrase.upper()

print(f'A letra "A" aparece \033[33m{phrase.count('A')}\033[m vezes')
print(f'A letra "A" aparece pela 1ª vez na posição \033[34m{phrase.find('A') + 1}\033[m')
print(f'A letra "A" aparece pela última vez na posição \033[32m{phrase.rfind('A') + 1}\033[m')
