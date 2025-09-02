#Escreva uma função que verifique se um vetor v[0..n-1] está em ordem crescente.
#(Este exercício põe em prática a estratégia de escrever os testes antes de inventar algoritmos para o problema.)

def verificar_oc(vetor):
    tamanho = len(vetor)
    esta_oc = True
    for i in range(tamanho-1):
        if vetor[i] > vetor[i+1] or vetor[i] == vetor[i+1]:
            print('Vetor não é crescente')
            esta_oc = False
            break
    if esta_oc == True:
        print('Vetor é crescente')
vetor = [1,2,3,4,5,4]

verificar_oc(vetor)