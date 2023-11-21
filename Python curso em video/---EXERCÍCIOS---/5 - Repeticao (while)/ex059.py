n1 = int(input('Dgite um numero: '))
n2 = int(input('Digite outro numero: '))
n3 = ''
n4 = ''
op = 0
while op != 5:
    op = int(input('Escolha a operação desejada: (1- Somar, 2- Multiplicar, 3-Maior, 4-Novos numeros, 5-Sair do programa): '))
    if op == 1:
        print(f'A soma desses dois numeros é: {n1+n2}')
    elif op == 2:
        print(f'A multiplicação desses dois numeros é: {n1*n2}')

    elif op == 3:
        if n1 > n2:
            print(f'O maior numero é o {n1}')
        elif n2 > n1:
            print(f'O maior numero é o {n2}')
    elif op == 4:
        n1 = int(input('Dgite um numero: '))
        n2 = int(input('Digite outro numero: '))
    elif op == 5:
        print('Finalizando....')
        break
    else:
        print('Opção invalida. Tente novamente')
        op = int(input('Escolha a operação desejada: (1- Somar, 2- Multiplicar, 3-Maior, 4-Novos numeros, 5-Sair do programa): '))
        break

print('Acabou o programa')

