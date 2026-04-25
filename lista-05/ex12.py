# Ex 12: Peça vários números ao usuário. O programa para quando digitar 0. No final, mostre a média dos números digitados (sem contar o zero).

contador = 0
numeros_media = 0

while True:
  numero = int(input('Digite um número: '))

  if numero != 0:
    numeros_media += numero
    contador += 1
  else:
    resultado_final = numeros_media / contador
    print(resultado_final)
    break