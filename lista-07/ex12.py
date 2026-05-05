# Percorra uma lista e classifique cada número como: Positivo, negativo, zero

lista_numeros = [2, 5, 7, -6, -2, 0, 45, -1, 0]

for numeros in lista_numeros:
    if numeros > 0:
        print('Positivo')
    elif numeros < 0:
        print('Negativo')
    else:
        print('Zero')