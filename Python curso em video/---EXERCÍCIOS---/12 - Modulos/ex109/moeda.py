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
