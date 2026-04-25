# Ex 16: Leia: peso e altura. Calcule: IMC = peso / (altura2); Classifique: < 18.5 Abaixo do peso; 18.5–24.9 Normal; 25–29.9 Sobrepeso; ≥ 30 Obesidade

peso = float(input('Digite o seu peso em Kg: '))
altura = float(input('Digite a sua altura em metros: '))

calculo_imc = peso / (altura ** 2)

if calculo_imc < 18.5:
  print('Você está abaixo do peso')
elif calculo_imc >= 18.5 and calculo_imc <= 24.9:
  print('Você está com o peso normal')
elif calculo_imc >= 25 and calculo_imc <= 29.9:
  print('Você está com sobrepeso')
else:
  print('Você está obeso')