# Ex 18: Leia a idade. Regras: <16 Não vota; 16–17 Voto opcional; 18–69 Voto obrigatório; 70+ Voto opcional

idade = int(input('Digite a sua idade: '))

if idade < 16:
  print('Não vota')
elif idade <= 17:
  print('Voto opcional')
elif idade >= 18 and idade <= 69:
  print('Voto obrigatório')
else:
  print('Voto opcional')