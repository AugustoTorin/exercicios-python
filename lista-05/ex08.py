# Ex 08: Peça vários números ao usuário. O programa termina quando o usuário digita 0. Ao final, mostre quantos números positivos foram digitados.

contador = 0

while True:
    numero = int(input('Digite um número: '))

    if numero == 0:
        print(f'A quantidade de números positivos digitados é {contador}')
        break
    elif numero > 0:
        contador += 1