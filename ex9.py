salario = float(input('Digite o seu salário: '))

if salario <= 1000:
    salario = salario*1.10 #aumento de 10%
else:
    salario = salario*1.05 #aumento de 5%
print(f'Salário depois do aumento: {salario:.2f}')