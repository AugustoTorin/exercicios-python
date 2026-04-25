# Ex 08: Conte quantas vezes um determinado valor aparece na lista. Exemplo: lista = [1, 2, 2, 3, 2], valor = 2. Saída: 3

lista = [1, 2, 4, 5, 6, 1, 4, 1, 6, 7, 2, 3, 1, 4, 8, 1]

valor = int(input((f'Digite um dos valores da lista {lista}: ')))

quantidade = lista.count(valor)
print(f'O número {valor} apareceu essa quantidade de vezes na lista: {quantidade}')