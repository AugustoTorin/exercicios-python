# Ex 11: Calcule a soma de todos os números pares entre 1 e 50 usando while.

contador = 1
soma_pares = 0

while contador <= 50:
  if contador % 2 == 0:
    soma_pares += contador
    contador += 1
  else:
    contador += 1

print(soma_pares)