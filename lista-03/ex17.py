# Ex 17: Leia um número de 1 a 7 e mostre o dia da semana. Se for inválido, mostrar erro.

numero = int(input('Digite um número de 1 a 7: '))

if numero == 1:
  print('Domingo')
elif numero == 2:
  print('Segunda')
elif numero == 3:
  print('Terça')
elif numero == 4:
  print('Quarta')
elif numero == 5:
  print('Quinta')
elif numero == 6:
  print('Sexta')
elif numero == 7:
  print('Sábado')
else:
  print('ERRO!')