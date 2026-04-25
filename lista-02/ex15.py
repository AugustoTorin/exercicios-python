# Ex 15: Leia duas notas e calcule a média. Mostre o resultado da expressão lógica: media >= 6

nota1 = float(input('Digite a primeira nota: '))
nota2 = float(input('Digite a segunda nota: '))

media = (nota1 + nota2) / 2
verificacao_media = media >= 6

print(verificacao_media)