# Ex 05: Peça um número e mostre sua tabuada de 1 a 10.

numero = int(input('Digite um número: '))

for multiplicador in range(1, 11):
    resultado = numero * multiplicador
    print(f'{numero} x {multiplicador} = {resultado}')