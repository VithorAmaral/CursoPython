t = int(input('Escreva o primeiro termo: '))
r = int(input('Escreva a razao da pa: '))
cont = 1
while cont <= 10:
    print(f'{t} → ', end='')
    t += r
    cont += 1
print('FIM')