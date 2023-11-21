import random
n = (random.randint(0, 100), random.randint(0, 100), random.randint(0, 100), random.randint(0, 100), random.randint(0, 100))
print(f'Os valores soreteados foram :', end='')
for i in n:
    print(f'{i} ', end='')
print(f'\nO maior valor sorteado foi {max(n)}')
print(f'O menor valor sorteado foi {min(n)}')