dados = {'nome': 'Pedro','sexo': 'M', 'idade': 25, 'formação': 'Administração'}
del dados['sexo']
dados['idade'] = 26
dados['Salário'] = 2650

print(dados.values())
print(dados.keys())
print(dados.items())

for k, v in dados.items():
    print(f'{k}: {v}')