# Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos Dólares
# ela pode comprar

# Considere: US$ 1,00 = R$ 3,27

quotationDollar = 3.27
valueInWallet = float(input('Informe o valor que você possui na sua carteira: '))

print(f'Com R$ {valueInWallet:.2f} você pode comprar US$ {(valueInWallet / quotationDollar):.2f}')
