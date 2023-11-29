# Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos Dólares
# ela pode comprar

# Considere: US$ 1,00 = R$ 3,27

quotationDollar = 3.27
valueInWallet = float(input('Informe o valor que você possui na sua carteira: '))

print(f'Com \033[34mR$ {valueInWallet:.2f}\033[m você pode comprar \033[32mUS$ {(valueInWallet / quotationDollar):.2f}\033[m')
