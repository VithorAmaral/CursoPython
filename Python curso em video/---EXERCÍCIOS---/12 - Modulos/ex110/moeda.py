def aumentar(n, porc, formato=False):
    res = n + (n * porc / 100)
    return res if formato is False else moeda(res)


def diminuir(n, porc, formato=False):
    res = n - (n * porc / 100)
    return res if formato is False else moeda(res)


def dobro(n, formato=False):
    res = n * 2
    return res if formato is False else moeda(res)


def metade(n, formato=False):
    res = n / 2
    return res if formato is False else moeda(res)


def moeda(preco=0, moeda='R$'):
    return f'{moeda}{preco:.2f}'.replace('.', ',')


def resumo(preco=0, taxaa=10, taxar=5):
    print('-' * 30)
    print('RESUMO DO VALOR'.center(30))
    print('-' * 30)
    print(f'Preço analisado: \t\t{moeda(preco)}')
    print(f'Dobro do preço: \t\t{dobro(preco, True)}')
    print(f'Metade do preço: \t\t{metade(preco, True)}')
    print(f'Com {taxaa}% de aumento: \t{aumentar(preco, taxaa, True)}')
    print(f'Com {taxar}% de redução: \t{diminuir(preco, taxar, True)}')
    print('-' * 30)