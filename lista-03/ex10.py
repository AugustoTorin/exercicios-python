# Ex 10: Leia um ano e informe se ele é bissexto. Regra simplificada: Se for divisível por 4 → bissexto; Senão → não é

ano = int(input('Digite um ano qualquer: '))
conta_ano_bissexto = ano % 4

if conta_ano_bissexto == 0:
   print('O ano digitado é bissexto.')
else:
   print('O ano digitado não é bissexto.')