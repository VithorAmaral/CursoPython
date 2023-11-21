n1 = int(input('Escreva o primeiro numero: '))
n2 = int(input('Escreva o sefgundo numero: '))
n3 = int(input('Escreva o terceiro numero: '))
if n1 > n2 > n3:
    print('o maior numero é o {} e o menor é o {}'.format(n1, n3))
if n3 > n1 > n2:
    print('o maior numero é o {} e o menor é o {}'.format(n3, n2))
if n2 > n3 > n1:
    print('o maior numero é o {} e o menor é o {}'.format(n2, n1))
if n3 > n2 > n1:
    print('o maior numero é o {} e o menor é o {}'.format(n3, n1))
