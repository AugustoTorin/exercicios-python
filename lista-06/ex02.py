# Ex 02: Encontre o maior número dentro de uma lista sem usar max().

lista_maior_numero = []
maior_numero = None

while True:
  numero = int(input('Digite um número: '))

  if maior_numero == None:
    maior_numero = numero
  elif numero > maior_numero:
    maior_numero = numero

  lista_maior_numero.append(maior_numero)

  if numero == 0:
    print(f'O maior número da lista, digitado, é {maior_numero}')
    break