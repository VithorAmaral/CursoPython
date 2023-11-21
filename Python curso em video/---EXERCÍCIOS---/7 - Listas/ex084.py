pessoas = []
galera = []
totpes = 0
menor = maior = 0
while True:
    pessoas.append(str(input('Digite o nome da pessoa: ')))
    totpes += 1
    pessoas.append(float(input('Digite o peso da pessoa: ')))
    if len(galera) == 0:
        menor = maior = pessoas[1]
    else:
        if pessoas[1] > maior:
            maior = pessoas[1]
        if pessoas[1] < menor:
            menor = pessoas[1]
    galera.append(pessoas[:])
    pessoas.clear()
    cond = str(input('Deseja continuar?(S/N): ')).strip().upper()
    if cond == 'N':
        break

print(f'Foram cadastradas {len(galera)} pessoas')
print(f'O maior peso foi de {maior} Kg. Peso de ', end='')
for p in galera:
    if p[1] == maior:
        print(f'[{p[0]}] ', end='')
print()
print(f'O menor peso foi de {menor} Kg. Peso de ', end='')
for p in galera:
    if p[1] == menor:
        print(f'[{p[0]}]')
print()



