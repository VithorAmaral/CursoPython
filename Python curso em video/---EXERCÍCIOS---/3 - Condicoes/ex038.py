n1 = int(input('Escreva um valor: '))
n2 = int(input('Escreva outro valor: '))
if n1 > n2:
    print('{} é maior e {} é menor'.format(n1, n2))
elif n2 > n1:
    print('{} é maior e {} é menor: '.format(n2, n1))
elif n1 == n2:
    print('{} é igual a {}'.format(n1, n2))

