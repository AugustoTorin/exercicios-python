# Ex 06: Receba dois números e um operador: "+". "-". "*". "/". Use match case para realizar a operação correspondente. Se o operador for inválido, mostre "Operação inválida".

n1 = int(input('Digite um número: '))
n2 = int(input('Digite outro número: '))
operador = input('Digite "+" para adição, "-" para subtração, "*" para multiplicação e "/" para divisão: ')

match operador:
    case '+':
        soma = n1 + n2
        print(soma)
    case '-':
        sub = n1 - n2
        print(sub)
    case '*':
        multi = n1 * n2
        print(multi)
    case '/':
        div = n1 / n2
        print(div)
    case _:
        print('Operação inválida')