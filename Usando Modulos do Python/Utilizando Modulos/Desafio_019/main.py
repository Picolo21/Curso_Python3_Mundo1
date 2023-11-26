# Um professor quer sortear um dos seus quatro alunos para apagar o quadro. Faça um programa
# que ajude ele, lendo o nome deles e escrevendo o nome do escolhido

import random

person1 = input('Primeiro(a) aluno(a): ')
person2 = input('Segundo(a) aluno(a): ')
person3 = input('Terceiro(a) aluno(a): ')
person4 = input('Quarto(a) aluno(a): ')

personList = [person1, person2, person3, person4]

selected = random.choice(personList)

print(f'O aluno(a) escolhido foi {selected}')
