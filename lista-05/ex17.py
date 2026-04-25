# Ex 17: Peça ao usuário um número entre 1 e 10. Continue pedindo até ele digitar um valor válido.

while True:
  numero = int(input('Digite um número entre 1 e 10: '))

  if numero >= 1 and numero <= 10:
    print('Número válido')
    break
  else:
    print('Número inválido')