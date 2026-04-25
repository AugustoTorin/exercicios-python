# Ex 14: Leia um número e verifique se ele é múltiplo de 3 e de 5 ao mesmo tempo.

numero = int(input('Digite um número: '))

verificacao = numero % 3 == 0 and numero % 5 == 0

print(verificacao)