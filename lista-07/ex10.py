# Dada uma string, conte quantas vogais existem.

texto = 'Olá, este é um código que conta quantas vogais tem linha de texto.'
texto = texto.lower()
contador_vogal = 0
vogais = 'aeiouáéó'

for letra in texto:
    if letra in vogais:
        contador_vogal += 1

print(f'A quantidade de vogais no texto é {contador_vogal}')