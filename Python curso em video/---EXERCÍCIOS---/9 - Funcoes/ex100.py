from random import randint
from time import sleep


def sorteia(lista):
    print('Sorteando 5 valores da lista: ', end='')
    for i in range(5):
        n = randint(1, 10)
        lista.append(n)
        print(f'{n} ', end='')
        sleep(0.3)
    print('PRONTO!')


def somapar(lista):
    soma = 0
    for i in lista:
        if i % 2 == 0:
            soma += i
    print(f'Somando os valores pares de {lista}, temos {soma}')


numeros = []
sorteia(numeros)
somapar(numeros)
