# Ex 16: Leia: idade, concluiu_ensino_medio (True ou False) Mostre o resultado da expressão: idade >= 18 and concluiu_ensino_medio

idade = int(input('Digite a sua idade: '))
concluiu_ensino_medio = True or False

habilitacao = idade >= 18 and concluiu_ensino_medio

print(habilitacao)