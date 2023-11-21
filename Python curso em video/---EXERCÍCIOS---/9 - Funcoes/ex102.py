def fatorial(num, show):
    '''
    → Calcula o Fatorial de um numero
    :param num: O numero a ser calculado
    :param show: (opcional) Mostrar ou não a conta
    :return: O valor do Fatorial de um numero n.
    '''
    f = 1
    for i in range(num, 0, -1):
        if show:
            print(i, end='')
            if i > 1:
                print(' x ', end='')
            else:
                print(' = ', end='')
        f *= i
    return f


# Programa Principal
print(fatorial(5, True))
