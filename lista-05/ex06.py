# Ex 06: Peça ao usuário para digitar um número maior que 10. Continue pedindo enquanto ele digitar valores inválidos.

while True:
    numero = int(input('Digite um número maior do que 10: '))

    if numero < 10:
        print('Número inválido')
    else:
        print('Número válido')
        break