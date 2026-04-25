# Ex 06: Conte quantos números pares existem entre 1 e 50.

contador_pares = 0

for i in range(1, 51):
    if i % 2 == 0:
        contador_pares += 1

print(f'Entre 1 e 50 existem {contador_pares} números pares')