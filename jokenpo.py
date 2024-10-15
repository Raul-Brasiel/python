import random

for c in range(0,int(input('Digite quantas vezes quer jogar: '))):
    mao = input('Digite pedra, papel ou tesoura: ').lower().strip()

    maoPC = random.choice(['pedra', 'papel', 'tesoura'])
    print(f'Computador: {maoPC}')

    if maoPC == 'pedra' and mao == 'tesoura':
        print('Você perdeu.')
    elif maoPC == 'papel' and mao == 'tesoura':
        print('Você ganhou!')
    elif maoPC == 'tesoura' and mao == 'papel':
        print('Você perdeu.')
    elif maoPC == 'pedra' and mao == 'papel':
        print('Você ganhou.')
    elif maoPC == 'papel' and mao == 'pedra':
        print('Você perdeu.')
    elif maoPC == 'tesoura' and mao == 'pedra':
        print('Você ganhou!')
    else:
        print('Empate!')
print('==========fim==========')