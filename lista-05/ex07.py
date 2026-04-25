# Ex 07: Peça números ao usuário e some todos eles. O programa deve parar quando o usuário digitar 0.

resultado = 0

while True:
    numero = int(input('Digite um número: '))

    if numero != 0:
        resultado += numero
    else:
        print(resultado)
        break