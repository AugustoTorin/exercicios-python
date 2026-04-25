# Ex 01: Dada uma lista de números, calcule a soma de todos os elementos usando while.

lista_numeros = []

while True:
    numeros = int(input('Digite um número para adicionar na lista: '))

    if numeros != 0:
        lista_numeros.append(numeros)
    else:
        soma_total = sum(lista_numeros)
        print(soma_total)
        break