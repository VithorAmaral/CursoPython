import random
lista = [0, 1, 2, 3, 4, 5]
n = random.choice(lista)
ne = int(input('advinhe o numero entre 0 e 5: '))
if n == ne:
    print('Parabens, voce acertou')
else:
    print('Voce errou, o numero era {}'.format(n))
