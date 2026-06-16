# Ex 19: Leia: salario, nome_limpo (True ou False). Mostre o resultado da expressão: salario >= 2000 and nome_limpo

#Cenário 1: Ambos falsos
salario = 1900
nome_limpo = False

verificacao = salario >= 2000 and nome_limpo

print(verificacao)

#Cenário 2: Ambos verdadeiros
salario = 2000
nome_limpo = True

verificacao = salario >= 2000 and nome_limpo

print(verificacao)

#Cenário 3: Nome limpo verdadeiro e salario false
salario = 1900
nome_limpo = True

verificacao = salario >= 2000 and nome_limpo

print(verificacao)

#Cenário 4: Nome limpo falso e salario verdadeiro
salario = 2100
nome_limpo = False

verificacao = salario >= 2000 and nome_limpo

print(verificacao)