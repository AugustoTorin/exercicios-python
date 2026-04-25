# Ex 10: Crie um programa que receba o valor de uma compra. Se o valor for maior ou igual a 100, aplique 10% de desconto. Caso contrário, mantenha o valor normal. Use operador ternário para calcular o valor final. Exemplo: Compra de 200 → 180. Compra de 80 → 80

valor_compra = float(input('Digite o valor da compra: '))

preco_final = valor_compra * 0.9 if valor_compra >= 100 else valor_compra

print(f'O valor final da compra é {preco_final}')