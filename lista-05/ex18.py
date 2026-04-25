# Ex 18: Peça 5 números ao usuário usando while. Ao final, mostre a soma.

contador = 1
soma_numeros = 0

while contador <= 5:
  numero = int(input('Digite um número: '))

  soma_numeros += numero
  contador += 1

print(f'A soma dos números digitados é {soma_numeros}')