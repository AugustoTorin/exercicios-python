# Ex 02: Crie um programa que receba uma letra e informe: "Vogal" para a, e, i, o, u. "Consoante" para qualquer outra letra. Use match case com comparação múltipla para as vogais.

letra = input('Digite uma letra: ')

match letra:
    case 'a' | 'e' | 'i' | 'o' | 'u':
        print('Vogal')
    case _:
        print('Consoante')