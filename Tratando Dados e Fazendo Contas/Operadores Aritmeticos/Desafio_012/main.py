# Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto

discountAmount = 5 / 100
productPrice = float(input('Digite o valor do produto: '))

newProductPrice = productPrice - (productPrice * discountAmount)

print(f'O produto que custava R$ {productPrice:.2f}, com o desconto, agora custa R$ {newProductPrice:.2f}')
