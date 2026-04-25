# Ex 07: Some apenas os números pares de 1 a 100.

soma = 0

for numero in range(1, 101):
    if numero % 2 == 0:
        soma += numero

print(f'A soma dos números pares entre 1 e 100 é: {soma}')