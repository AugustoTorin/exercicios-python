# Ex 09: Peça ao usuário uma senha. Continue pedindo até ele digitar "1234".

while True:
    senha = input('Digite a senha numérica de 4 digitos: ')

    if senha == '1234':
        print('Senha válida')
        break