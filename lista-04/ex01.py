# Ex 01: Crie um programa que receba um número de 1 a 7 e mostre o dia da semana correspondente. Exemplo: 1 → Domingo; 2 → Segunda; 7 → Sábado. Se o número for inválido, mostre: "Dia inválido".

numero = int(input('Digite um número de 1 a 7: '))

match numero:
    case 1:
        print('Domingo')
    case 2:
        print('Segunda')
    case 3:
        print('Terça')
    case 4:
        print('Quarta')
    case 5:
        print('Quinta')
    case 6:
        print('Sexta')
    case 7:
        print('Sábado')
    case _:
        print('Número inválido')