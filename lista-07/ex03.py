# Ex 03: Dada uma lista de números, conte quantos são positivos.

lista_numeros = [2, 4, -5, -3, 6, 9, 0, -21, 34]
contador_positivos = 0

for numero in lista_numeros:
    if numero > 0:
        contador_positivos += 1

print(lista_numeros)
print(f'A lista contém {contador_positivos} número(s) positivos')