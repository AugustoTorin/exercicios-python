# Ex 14: Leia uma nota de 0 a 10 e classifique: Nota Conceito: ≥ 9 A; ≥ 7 B; ≥ 5 C; < 5 D

nota = int(input('Digite a nota do aluno: '))

if nota >= 9 and nota <= 10:
  print('A')
elif nota >= 7:
  print('B')
elif nota >= 5:
  print('C')
else:
  print('D')