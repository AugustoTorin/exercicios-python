# Ex 19: Peça 10 números ao usuário. Mostre quantos são pares e quantos são ímpares.

contador = 1
contador_par = 0
contador_impar = 0

while contador <= 10:
  numero = int(input('DIgite um número: '))

  if numero % 2 == 0:
    contador_par += 1
  else:
    contador_impar += 1

  contador += 1

print(f'Foram digitados {contador_par} números pares e {contador_impar} números ímpares')