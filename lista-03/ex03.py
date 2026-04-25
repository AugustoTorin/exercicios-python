# Ex 03: Leia um número e informe se ele é: positivo, negativo ou zero

numero = int(input('Digite um número: '))

if numero == 0:
   print('O número digitado é zero.')
elif numero < 0:
   print('O número digitado é negativo.')
else:
   print('O número digitado é positivo.')