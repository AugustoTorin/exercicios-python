# Ex 05: Crie um programa que receba a idade de uma pessoa e mostre: "Maior de idade" se tiver 18 anos ou mais. "Menor de idade" caso contrário. Use operador ternário.

idade = int(input('Digite a sua idade: '))

print('Maior de idade') if idade >= 18 else print('Menor de idade')