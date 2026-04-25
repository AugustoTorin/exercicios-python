# Ex 01: Percorra os números de 1 a 20 e imprima se cada número é par ou ímpar.

for numero in range(1, 21):
    if numero % 2 == 0:
        print(f'Número par: {numero}')
    else:
        print(f'Número ímpar: {numero}')