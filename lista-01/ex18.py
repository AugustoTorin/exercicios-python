# Ex 18: Peça ao usuário o preço de um produto e mostre o preço com desconto de 10%.

preco = int(input("Digite o preço do prduto:"))

desconto = preco * 0.10
preco_final = preco - desconto

print("O produto com desconto de 10% fica no valor de", preco_final)