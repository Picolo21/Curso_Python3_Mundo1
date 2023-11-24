# Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento

amountOfSalaryIncrease = 15 / 100
name = input('Digite seu nome: ')
salaryValue = float(input('Digite o valor do seu salário: '))

newSalaryValue = salaryValue + (salaryValue * amountOfSalaryIncrease)

print(f'{name}, seu salário que era de R$ {salaryValue:.2f},com o aumento, agora passará a ser de R$ {newSalaryValue:.2f}')
