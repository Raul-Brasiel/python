casa = float(input('Digite o valor da casa: '))
salario = float(input('Digite o seu salário: '))
anos = int(input('Digite em quantos anos de financiamento: '))

mensal = casa/(anos*12)
salario = salario*0.3

if salario > mensal:
    print('Empréstimo aprovado!')
else:
    print('Empréstimo reprovado!')