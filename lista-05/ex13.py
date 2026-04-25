# Ex 13: Peça números ao usuário até ele digitar 0. Mostre qual foi o maior número informado.

maior_numero = None

while True:
  numero = int(input('Digite um número: '))

  if maior_numero == None:
    maior_numero = numero
  elif numero > maior_numero:
    maior_numero = numero

  if numero == 0:
    print(maior_numero)
    break