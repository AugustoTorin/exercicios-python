# Ex 06: Dada uma lista, crie outra lista sem elementos repetidos (mantendo a ordem).

lista_01 = [5, 1, 6, 5, 2, 3, 1, 3]
lista_02 = []
indice = 0

while indice < len(lista_01):
  if lista_01[indice] not in lista_02:
    lista_02.append(lista_01[indice])
  indice += 1

print(lista_02)