# Ex 20: Leia: usuário e senha. Considere: usuario = "admin"; senha = "python123" Se ambos estiverem corretos: Login realizado com sucesso. Caso contrário: Usuário ou senha incorretos

usuario = input('Digite seu login de usuário: ')
senha = input('Digite a senha: ')

if usuario == 'admin' and senha == 'python123':
  print('Login realizado com sucesso')
else:
  print('Usuário ou senha incorretos')