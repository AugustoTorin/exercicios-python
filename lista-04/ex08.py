# Ex 08: Receba um número de 1 a 12 e informe o trimestre ao qual o mês pertence: meses 1, 2, 3 → "1o trimestre"; meses 4, 5, 6 → "2o trimestre"; meses 7, 8, 9 → "3o trimestre"; meses 10, 11, 12 → "4o trimestre". Se o número for inválido, mostre "Mês inválido".

numero = int(input('Digite um número de 1 a 12: '))

match numero:
    case 1 | 2 | 3:
        print('Primeiro trimestre')
    case 4 | 5 | 6:
        print('Segundo trimestre')
    case 7 | 8 | 9:
        print('Terceiro trimestre')
    case 10 | 11 | 12:
        print('Quarto trimestre')
    case _:
        print('Mês inválido')