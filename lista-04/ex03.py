# Ex 03: Receba uma palavra que representa o turno: "m" → "Bom dia". "t" → "Boa tarde". "n" → "Boa noite". Se for diferente disso, exiba "Turno inválido".

turno = input('Digite um turno "m", "t" ou "n": ')

match turno:
    case 'm':
        print('Bom dia')
    case 't':
        print('Boa tarde')
    case 'n':
        print('Boa noite')
    case _:
        print('Turno inválido')