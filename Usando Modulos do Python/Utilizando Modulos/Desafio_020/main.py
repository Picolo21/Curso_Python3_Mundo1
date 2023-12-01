# Um professor quer sortear a ordem de apresentação dos trabalhos dos alunos. Faça um programa
# que leia o nome dos quatro alunos e mostre a ordem sorteada

import random

person1 = input('Primeiro(a) aluno(a): ')
person2 = input('Segundo(a) aluno(a): ')
person3 = input('Terceiro(a) aluno(a): ')
person4 = input('Quarto(a) aluno(a): ')

personList = [person1, person2, person3, person4]
random.shuffle(personList)

print('A ordem de apresentação dos alunos será:')
print(f'\033[34m{personList}\033[m')
