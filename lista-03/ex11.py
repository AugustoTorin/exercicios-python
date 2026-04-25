# Ex 11: Leia o valor de uma compra. Aplique desconto: Valor Desconto; ≥ 1000 10%; ≥ 500 5%; < 500 sem desconto. Mostre o valor final.

valor_compra = float(input('Digite o valor da compra: '))

if valor_compra >= 1000:
  desconto = 10 / 100
  desconto_final = valor_compra * desconto
  preco_final = valor_compra - desconto_final

  print(f'O produto teve um desconto de 10% e ficou no valor de {preco_final} reais')

elif valor_compra >= 500 and valor_compra <= 999:
  desconto = 5 / 100
  desconto_final = valor_compra * desconto
  preco_final = valor_compra - desconto_final

  print(f'O produto teve um desconto de 5% e ficou no valor de {preco_final} reais')

else:
  print(f'O produto não teve desconto e manteve o valor de {valor_compra} reais')