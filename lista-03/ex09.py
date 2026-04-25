# Ex 09: Leia a idade de uma pessoa e classifique: Idade Categoria: 0–12 Criança; 13–17 Adolescente; 18–59 Adulto; 60+ Idoso

idade = int(input('Digite a sua idade: '))

if idade <= 12:
   print('Você é uma criança.')
elif idade >= 13 and idade <= 17:
   print('Você é um adolescente.')
elif idade >= 18 and idade <= 59:
   print('Você é um adulto.')
else:
   print('Você é um idoso.')