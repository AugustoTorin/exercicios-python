# Ex 09: Leia o preço de um produto e o percentual de desconto. Calcule o valor do desconto e o preço final.

preco = float(input('Digite o preço do produto: '))
desconto = int(input('Digite o percentual de desconto: '))

calculo1_desconto = desconto / 100
calculo2_desconto = preco * calculo1_desconto
preco_final = preco - calculo2_desconto

print(f'Preço: {preco}')
print(f'Desconto: {desconto}%')
print(f'Preço Final: {preco_final}')