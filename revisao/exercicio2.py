#Escreva uma função que receba um inteiro x e um vetor v[0..n-1] de inteiros em ordem
#crescente e insira x no vetor de modo a manter a ordem crescente.

def inserir_x(vetor, x):
    tamanho = len(vetor)
    for i in range(tamanho):
        if i == 0:
            if x < vetor[0]:
                vetor.insert(0, x)
                break
        elif i == tamanho-1:
            if x > vetor[i]:
                vetor.insert(tamanho,x)
        else:
            if x > vetor[i] and x < vetor[i+1]:
                vetor.insert(i+1,x)
    print(f'Vetor após inserir {x}: {vetor}')

vetor = [1,2,3,4,5]
x = 6

print(f'Vetor: {vetor}')
inserir_x(vetor, x)