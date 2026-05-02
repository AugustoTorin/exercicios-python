# Dada uma lista, crie outra lista com os elementos na ordem inversa (usando for).

lista = [1, 2, 3, 4, 5]
lista_invertida = []

for i in range(len(lista) - 1, -1, -1):
    lista_invertida.append(lista[i])

print(lista_invertida)