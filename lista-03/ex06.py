# Ex 06: Leia a nota final de um aluno. Classifique: Nota ≥ 7 → Aprovado; Nota ≥ 5 e < 7 → Recuperação; Nota < 5 → Reprovado

nota_final = float(input('Digite a nota final do aluno: '))

if nota_final >= 7:
   print('Aprovado!')
elif nota_final >= 5 and nota_final < 7:
   print('Recuperação!')
else:
   print('Reprovado!')