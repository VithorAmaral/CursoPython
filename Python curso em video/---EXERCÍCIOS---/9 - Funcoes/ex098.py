def contador(inicio, fim, passo):
    for i in range(1, 11, 1):
        print(i)
    print('---------------')
    for i in range(10, 0, -2):
        print(i)
    print('---------------')
    for i in range(inicio, fim, passo):
        print(i)


contador(inicio=int(input('Digite o numero do inicio: ')), fim=int(input('Digite o numero do fim: ')), passo=int(input('De quanto em quantos numeros voce quer pular? ')))












