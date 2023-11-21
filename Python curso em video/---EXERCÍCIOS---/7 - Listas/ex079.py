lista = []

while True:
    n = int(input('Digite um valor: '))
    if n not in lista:
        lista.append(n)
        print('Valor adicionado com sucesso!')
    else:
        print('Valor duplicado!')
    cond = str(input('Quer continuar?(S/N): ')).upper().strip()
    if cond == 'N':
        break

lista.sort()
print(f'Os numeros digitados foram {lista}')
