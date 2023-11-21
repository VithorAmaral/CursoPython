from random import randint
from time import sleep
from operator import itemgetter
numeros = {'jogador1': randint(1, 6), 'jogador2': randint(1, 6), 'jogador3': randint(1, 6), 'jogador4': randint(1, 6)}
ranking = []
print('Valores sorteados: ')
for k, v in numeros.items():
    print(f'{k} tirou {v} no dado.')
    sleep(1)
ranking = sorted(numeros.items(), key=itemgetter(1), reverse=True)
print('-='*30)
print('== RANKING DOS JOGADORES ==')
for i, v in enumerate(ranking):
    print(f' {i+1}° lugar: {v[0]} com {v[1]}.')
    sleep(1)