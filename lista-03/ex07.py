# Ex 07: Crie um programa que peça uma senha. Se a senha for 1234, mostre: Acesso permitido. Caso contrário: Acesso negado.

senha = int(input('Digite uma senha de 4 números: '))

if senha == 1234:
   print('Acesso permitido.')
else:
   print('Acesso negado.')