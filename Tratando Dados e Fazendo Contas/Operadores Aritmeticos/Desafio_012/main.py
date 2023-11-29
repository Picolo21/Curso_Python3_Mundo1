# Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto

discountAmount = 5 / 100
productPrice = float(input('Digite o valor do produto: R$ '))

newProductPrice = productPrice - (productPrice * discountAmount)

print(f'O produto que custava \033[31mR$ {productPrice:.2f}\033[m, com o desconto, agora custa \033[32mR$ {newProductPrice:.2f}\033[m')
