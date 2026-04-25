# Ex 10: Encontre o segundo maior número da lista. Exemplo: [10, 20, 5, 40, 30]. Saída: 30. Regras: Não pode usar sort(). Não pode usar max() duas vezes direto.

lista_numeros = []
maior_numero = None
segundo_maior_numero = None

while True:
    numero = int(input('Digite um número: '))

    if maior_numero == None:
        maior_numero = numero
    elif numero > maior_numero:
        segundo_maior_numero = maior_numero
        maior_numero = numero
    elif numero < maior_numero and (segundo_maior_numero is None or numero > segundo_maior_numero):
        segundo_maior_numero = numero

    lista_numeros.append(numero)

    if len(lista_numeros) == 3:
        break

print(lista_numeros)
print(f'O segundo maior número digitado foi: {segundo_maior_numero}')