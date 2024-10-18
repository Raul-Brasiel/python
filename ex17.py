aluno = dict()
aluno['nome'] = str(input('Digite o nome do aluno: '))
aluno['média'] = float(input(f'Digite a média do {aluno["nome"]}: '))

print(f'O nome do aluno é {aluno["nome"]} e tem média {aluno["média"]}.')
if aluno['média'] >= 6:
    print(f'{aluno["nome"]} foi aprovado!')
else:
    print(f'{aluno["nome"]} foi reprovado!')