# Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento

amountOfSalaryIncrease = 15 / 100
name = input('Digite seu nome: ').strip()
salaryValue = float(input('Digite o valor do seu salário: R$ '))

newSalaryValue = salaryValue + (salaryValue * amountOfSalaryIncrease)

print(f'\033[34m{name}\033[m, seu salário que era de \033[31mR$ {salaryValue:.2f}\033[m,com o aumento, agora passará a ser de \033[32mR$ {newSalaryValue:.2f}\033[m')
