# Ex 05: Leia três números e informe qual é o maior.

n1 = int(input('Digite o primeiro número: '))
n2 = int(input('Digite o segundo número: '))
n3 = int(input('Digite o terceiro número: '))

if n1 > n2 and n1 > n3:
   print('O primeiro número digitado é o maior.')
elif n2 > n3:
   print('O segundo número digitado é o maior.')
else:
   print('O terceiro número digitado é o maior.')