# Ex 12: Leia um número e verifique se ele está entre 10 e 20. Mostre o resultado da expressão lógica.

numero = int(input('Digite um número: '))

verificacao = numero >= 10 and numero <= 20

print(verificacao)