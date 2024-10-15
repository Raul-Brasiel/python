import random

n1 = input('Escreva o nome de um aluno: ')
n2 = input('Escreva o nome de um aluno: ')
n3 = input('Escreva o nome de um aluno: ')
n4 = input('Escreva o nome de um aluno: ')

print(f'Aluno escolhido: {random.choice([n1, n2, n3, n4])}')

print('\nOrdem para apresentação dos trabalhos: \n1-{}\n2-{}\n3-{}\n4-{}'.format(random.choice([n1, n2, n3, n4]), n1, n2, n3, n4))