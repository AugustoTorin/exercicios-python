# Ex 08: Leia: dois números, uma operação (+, -, *, /). Use if elif para realizar a operação escolhida.

n1 = int(input('Digite um número: '))
n2 = int(input('Digite outro número: '))
operacao = input('Digite (+) para fazer uma adição, (-) para um subtração, (*) para uma multiplicação e (/) para uma divisão: ')

if operacao == '+':
   print(n1 + n2)
elif operacao == '-':
   print(n1 - n2)
elif operacao == '*':
   print(n1 * n2)
else:
   print(n1 // n2)