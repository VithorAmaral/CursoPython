import random
v = 0
while True:
    n = int(input('Digite um numero: '))
    npc = random.randint(0, 10)
    total = n + npc
    tipo = ' '
    while tipo not in 'PI':
        tipo = str(input('Par ou ímpar? ')).strip().upper()[0]
    print(f'Voce jogou {n} e o computador jogou {npc}. Total de {total}', end='')
    print(' DEU PAR' if total % 2 == 0 else ' DEU IMPAR')
    if tipo == 'P':
        if total % 2 == 0:
            print('VOCE VENCEU')
            v += 1
        else:
            print('VOCE PERDEU')
            break
    elif tipo == 'I':
        if total % 2 == 1:
            print('VOCE VENCEU')
            v += 1
        else:
            print('VOCE PERDEU')
            break
    print('Vamos jogar novamente...')
print(f'GAME OVER! Voce venceu {v} vezes')



