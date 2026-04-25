# Ex 07: Calcule a média dos números da lista.

lista_numeros = []

while True:
  numero = int(input('Digite um número: '))

  if numero != 0:
    lista_numeros.append(numero)
  else:
    media = sum(lista_numeros) / len(lista_numeros)
    print(f'A média dos números digitados é {media}')
    break