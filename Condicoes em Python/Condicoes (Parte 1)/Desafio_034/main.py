# Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento

# Para salários superiores a R$ 1.250,00, calcule um aumento de 10%

# Para salários inferiores ou iguais, o aumento é de 15%

parameterSalary = 1250

salary = float(input('Digite o valor do seu salário: R$ '))

if salary <= parameterSalary:
    salary = salary + (salary * (15 / 100))
else:
    salary = salary + (salary * (10 / 100))

print(f'\nSeu salário passará a ser de R$ {salary:.2f}')
