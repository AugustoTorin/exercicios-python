# Ex 04: Verifique se um número específico está presente na lista. Exemplo: lista = [1, 3, 5, 7], buscar = 5. Saída: "Encontrado" ou "Não encontrado"

lista_numeros = []
contador = 1

while contador <= 5:
  lista_numeros.append(int(input('Digite um número: ')))
  contador += 1

if 7 in lista_numeros:
  print('Número 7 encontrado')
else:
  print('Número 7 não encontrado')

print(lista_numeros)