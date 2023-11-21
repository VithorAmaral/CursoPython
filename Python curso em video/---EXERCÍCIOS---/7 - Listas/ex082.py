listapar = []
listaimpar = []
lista = []
while True:
    n = int(input('Digite um valor: '))
    lista.append(n)
    if n % 2 == 0:
        listapar.append(n)
    else:
        listaimpar.append(n)
    cond = str(input('Deseja continuar?(S/N): ')).strip().upper()
    if cond == 'N':
        break
print(f'Os numeros pares digitados são: {listapar}')
print(f'Os numeros impares digitados são: {listaimpar}')
print(f'Os valores digitados foram{lista}')
