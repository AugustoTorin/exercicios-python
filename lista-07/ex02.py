# Ex 02: Peça um número ao usuário e calcule a soma de todos os números de 1 até ele.

numero = int(input('Digite um número: '))
soma = 0

for i in range(1, numero):
    soma += numero

print(f'A soma do número 1 até o número {numero} é: {soma}')