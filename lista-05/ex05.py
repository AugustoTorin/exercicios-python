# Ex 05: Peça um número ao usuário e mostre a tabuada desse número de 1 até 10.

numero = int(input('Digite um número: '))
multiplicador = 1

while multiplicador <= 10:
    multiplicacao = numero * multiplicador
    multiplicador += 1
    print(multiplicacao)