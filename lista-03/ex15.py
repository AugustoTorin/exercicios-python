# Ex 15: Leia um número e verifique se ele é múltiplo de 3.

numero = int(input('Digite um número: '))
multiplo_de_3 = numero % 3

if multiplo_de_3 == 0:
  print('Este número é múltiplo de 3')
else:
  print('Este número não é múltiplo de 3')