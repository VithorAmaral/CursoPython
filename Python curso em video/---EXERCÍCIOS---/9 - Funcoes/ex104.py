def leiaint(msg):
    ok = False
    valor = 0
    while True:
        n = str(input(msg))
        if n.isnumeric():
            valor = int(n)
            ok = True
        else:
            print('Erro! Digite um numero inteiro valido!')
        if ok:
            break
    return valor


# Programa Principal
n = leiaint('Digite um numero: ')
print(f'Voce acabou de digitar o numero {n}')
