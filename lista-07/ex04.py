# Ex 04: Percorra uma lista de números e encontre o maior valor, sem usar max().

lista = [23, 43, -32, 1, 97, -3, 0, 71, 24]
maior_numero = None

for numero in lista:
    if maior_numero == None or numero > maior_numero:
        maior_numero = numero

print(maior_numero)