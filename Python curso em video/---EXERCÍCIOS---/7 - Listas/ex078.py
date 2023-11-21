numeros = []
maior = 0
menor = 0
for i in range(5):
    numeros.append(int(input(f'Digite um numero para a posição {i}: ')))
    if i == 0:
        maior = menor = numeros[i]
    else:
        if numeros[i] > maior:
            maior = numeros[i]
        if numeros[i] < menor:
            menor = numeros[i]
print(f'Voce digitou os valores {numeros}')
print(f'O maior valor digitado foi {maior} nas posições ', end='')
for c, v in enumerate(numeros):
    if v == maior:
        print(f'{c}...', end='')
print()
print(f'O menor numero digitado foi {menor} nas posições ', end='')
for c, v in enumerate(numeros):
    if v == menor:
        print(f'{c}...', end='')
print()
