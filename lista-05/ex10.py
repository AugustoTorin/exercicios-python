# Ex 10: Peça uma senha correta ("python"). Conte quantas tentativas o usuário fez até acertar.

contador_tentativa = 0

while True:
    senha = input('Digite a senha: ')
    contador_tentativa += 1

    if senha != 'python':
        print('Senha inválida')
    else:
        print(f'Você acertou a senha em {contador_tentativa} tentativas')
        break