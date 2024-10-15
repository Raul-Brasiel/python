cont = ('zero','um','dois','três','quatro','cinco',
        'seis','sete','oito','nove','dez',
        'onze','doze','treze','quatorze','quinze',
        'dezesseis','dezessete','dezoito','dezenove','vinte')

n = int(input('Digite um número: '))

while True:
    if n >= 0 and n <=20:
        print(f'O número digitado foi {cont[n]}.')
        break
    n = int(input('Digite um número válido de 0 a 20: '))