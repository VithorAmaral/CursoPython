lista = [[], []]
n = 0
for i in range(7):
    n = int(input('Digite um numero: '))
    lista.append(n)
    if n % 2 == 0:
        lista[0].append(n)
    else:
        lista[1].append(n)
lista[0].sort()
print(f'Os numeros pares são: {lista[0]}')
lista[1].sort()
print(f'Os numeros impares são: {lista[1]}')
