# Ex 05: Crie uma nova lista com os elementos invertidos.

lista_real = [1, 2, 3, 4, 5, 6, 7]
indice = len(lista_real) - 1
lista_inversa = []

while indice >= 0:
  lista_inversa.append(lista_real[indice])
  indice -= 1

print(lista_inversa)