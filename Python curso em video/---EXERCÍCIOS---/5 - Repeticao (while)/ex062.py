t = int(input('Escreva o primeiro termo: '))
r = int(input('Escreva a razao da pa: '))
cont = 1
total = 0
mais = 10
while mais != 0:
    total += mais
    while cont <= total:
        print(f'{t} → ', end='')
        t += r
        cont += 1
    print('PAUSA')
    mais = int(input('Quantos termos voce quer mostrar a mais? '))
print('FIM')
