# Mostre os números de 1 a 100 que são múltiplos de 3 e 5 ao mesmo tempo.

for i in range(1, 101):
    if i % 3 == 0 and i % 5 == 0:
        print(i)