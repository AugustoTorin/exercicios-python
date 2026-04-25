# Ex 09: Uma loja possui os seguintes setores: código 1 ou 2 → "Alimentos"; código 3 ou 4 → "Limpeza"; código 5 ou 6 → "Higiene". Crie um programa que receba o código e mostre o setor correspondente usando match case com comparação múltipla. Caso o código não exista, mostrar "Código inválido".

codigo_setor = int(input('Digite o código do setor: '))

match codigo_setor:
    case 1 | 2:
        print('Setor de Alimentos')
    case 3 | 4:
        print('Setor de Limpeza')
    case 5 | 6:
        print('Setor de Higiene')
    case _:
        print('Código inválido')