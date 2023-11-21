cont = 0
n = 0
while True:
    n = int(input('Digite um numero: '))
    if n < 0:
        print('Não é um numero valido')
        break
    else:
        for i in range(1, 11):
            print(f'{n} x {i} = {n*i}')
print('Programa encerrado')
