nome = input('Digite o nome da sua cidade: ').upper().split()

temSanto = 'SANTO' in nome[0]
if temSanto == True:
    print('Tem SANTO no nome.')
else:
    print('Não tem SANTO no nome.')