# Ex 19: Leia uma temperatura em Celsius. Classifique: < 15 Frio; 15–25 Agradável; > 25 Quente

temperatura = int(input('Digite uma temperatura em Celsius: '))

if temperatura < 15:
  print('Frio')
elif temperatura <= 25:
  print('Agradável')
else:
  print('Quente')