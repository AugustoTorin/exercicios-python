# Ex 03: Dada uma lista de inteiros, conte quantos números são pares.

lista_numeros_inteiros = []
contagem = 1
indice = 0
contador_pares = 0

while contagem <= 5:
  numeros = int(input('Digite um número: '))
  lista_numeros_inteiros.append(numeros)

  if lista_numeros_inteiros[indice] % 2 == 0:
    contador_pares += 1

  contagem += 1
  indice += 1

print(f'Quantidade de números pares: {contador_pares}')