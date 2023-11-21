def leiaInt(msg):
    while True:
        try:
            n = int(input(msg))
        except (ValueError, TypeError):
            print('ERRO: por favor, digite um numero inteiro válido.')
            continue
        except (KeyboardInterrupt):
            print('\nEntrada de dados interrompida pelo usuario.')
            return 0
        else:
            return n


def leiaFloat(msg):
    while True:
        try:
            n = float(input(msg))
        except (ValueError, TypeError):
            print('Erro: por favor, digite um numero real valido')
            continue
        except (KeyboardInterrupt):
            print('\nEntrada de daos interrompida pelo usuario.')
            return 0
        else:
            return n


i = leiaInt('Digite um valor inteiro: ')
r = leiaFloat('Digite um valor real: ')
print(f'O valor inteiro digitado foi {i} e o real foi {r}')

