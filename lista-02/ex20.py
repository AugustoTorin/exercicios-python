# Ex 20: Leia: idade, tem_autorizacao (True ou False). Mostre o resultado da expressão: idade >= 16 or (idade >= 12 and tem_autorizacao)

#Cenário 1: Tem autorização verdadeiro e idade menor que 12
idade = 11
tem_autorizacao = True

verificacao = idade >= 16 or (idade >= 12 and tem_autorizacao)

print(verificacao)

#Cenário 2: Tem autorização verdadeiro e idade menor que 16 e maior do que 12
idade = 15
tem_autorizacao = True

verificacao = idade >= 16 or (idade >= 12 and tem_autorizacao)

print(verificacao)

#Cenário 3: Tem autorização falso e idade maior que 16
idade = 17
tem_autorizacao = False

verificacao = idade >= 16 or (idade >= 12 and tem_autorizacao)

print(verificacao)

#Cenário 4: Tem autorização falso e idade menor que 16 e maior do que 12
idade = 14
tem_autorizacao = False

verificacao = idade >= 16 or (idade >= 12 and tem_autorizacao)

print(verificacao)