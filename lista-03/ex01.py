# Ex 01: Leia um número inteiro e informe se ele é par ou ímpar.

numero = int(input('Digite um número: '))
resto_divisao = numero % 2

if resto_divisao == 0:
   print('O número digitado é par.')
else:
   print('O número digitado é ímpar.')