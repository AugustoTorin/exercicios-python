# Ex 16: Crie um menu que aparece continuamente: 1 - Dizer Olá; 2 - Dizer Tchau; 3 - Sair. O programa só termina quando o usuário escolher a opção 3.

while True:
  numero = int(input('Digite os números 1, 2 ou 3: '))

  if numero == 1:
    print('Olá')
  elif numero == 2:
    print('Tchau')
  else:
    print('Sair')
    break