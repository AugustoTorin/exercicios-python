# Ex 20: Peça números ao usuário e multiplique todos eles. O programa termina quando o usuário digitar 1. (Mostre o resultado final)

numeros_multiplicados = 1

while True:
  numero = int(input('Digite um número: '))

  if numero != 1:
    numeros_multiplicados *= numero
  else:
    print(f'O resultado da multiplicação de todos os números digitados é {numeros_multiplicados}')
    break