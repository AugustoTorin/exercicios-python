# Ex 20: Leia: idade, tem_autorizacao (True ou False). Mostre o resultado da expressão: idade >= 16 or (idade >= 12 and tem_autorizacao)

idade = int(input('Digite a sua idade: '))
tem_autorizacao = True or False

verificacao = idade >= 16 or (idade >= 12 and tem_autorizacao)

print(verificacao)