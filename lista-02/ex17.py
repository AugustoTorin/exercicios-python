# Ex 17: Leia: tem_cartao (True ou False), tem_ticket (True ou False). Mostre o resultado da expressão: tem_cartao or tem_ticket

# Cenário 1: Ambos falsos
tem_cartao = False
tem_ticket = False

verificacao = tem_cartao or tem_ticket

print(verificacao)

#Cenário 2: Cartão verdadeiro e ticket falso
tem_cartao = True
tem_ticket = False

verificacao = tem_cartao or tem_ticket

print(verificacao)

#Cenário 3: Carão falso e ticket verdadeiro
tem_cartao = False
tem_ticket = True

verificacao = tem_cartao or tem_ticket

print(verificacao)

#Cenário 4: Ambos vredadeiros
tem_cartao = True
tem_ticket = True

verificacao = tem_cartao or tem_ticket

print(verificacao)