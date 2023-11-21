lista = []
while True:
    n = int(input('Digite um numero: '))
    cond = str(input('Quer continuar?(S/N): ')).strip().upper()
    lista.append(n)
    if cond == 'N':
        break

print(f'Voce digitou {len(lista)} numeros')
lista.sort(reverse=True)
print(f'Os numeros digitados foram {lista}')
if 5 in lista:
    print('O numero 5 está na lista')
else:
    print('O numero 5 não está na lista')



