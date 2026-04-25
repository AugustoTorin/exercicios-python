# Ex 07: Receba uma nota de 0 a 10 e classifique como: "Aprovado" se nota for maior ou igual a 7. "Recuperação" se nota for maior ou igual a 5 e menor que 7. "Reprovado" se for menor que 5. Use operador ternário encadeado.

nota = int(input('Digite a nota de 0 a 10: '))

print('Aprovado') if nota >= 7 else print('Recuperação') if nota >= 5 and nota <= 7 else print('Reprovado')