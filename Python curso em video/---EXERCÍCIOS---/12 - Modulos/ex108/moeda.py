def aumentar(n, porc):
    return n + (n * porc/100)


def diminuir(n, porc):
    return n - (n * porc/100)


def dobro(n):
    return n*2


def metade(n):
    return n/2


def moeda(preço=0, moeda='R$'):
    return f'{moeda}{preço:.2f}'.replace('.', ',')
