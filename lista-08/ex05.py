# Receba um texto e conte quantas vogais existem.

texto = 'O meu nome é Augusto Mota Torin'
vogais = 'aeiouáéúíó'
contador_vogal = sum(texto.count(letra) for letra in vogais)

print(f'A quantidade de vogais no texto é {contador_vogal}')