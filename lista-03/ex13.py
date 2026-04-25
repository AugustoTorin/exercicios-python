# Ex 13: Leia três lados de um triângulo. Classifique: Condição Tipo: 3 lados iguais Equilátero; 2 lados iguais Isósceles; Todos diferentes Escaleno

lado1 = int(input('Digite a primeira medida do triângulo: '))
lado2 = int(input('Digite a segunda medida do triângulo: '))
lado3 = int(input('Digite a terceira medida do triângulo: '))

if lado1 == lado2 == lado3:
  print('Este é um triângulo equilátero')
elif lado1 == lado2 or lado1 == lado3 or lado2 == lado3:
  print('Este é um triângulo isósceles')
else:
  print('Este é um triângulo escaleno')