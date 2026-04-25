# Ex 09: Dada uma lista, crie duas listas: uma com números pares e outra com números ímpares.

lista = []
lista_par = []
lista_impar = []

while True:
  numero = int(input('Digite um número: '))

  lista.append(numero)

  if numero == 0:
    lista_par.append(numero)
    break
  elif numero % 2 == 0:
    lista_par.append(numero)
  else:
    lista_impar.append(numero)

print(f'Todos esses números foram digitados: {lista}')
print(f'Todos esses números são pares: {lista_par}')
print(f'Todos esses números são ímpares: {lista_impar}')