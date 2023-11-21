maior = menor = 0
for p in range(1, 6):
    peso = float(input(f'Digite o peso da {p}° pessoa: '))
    if p == 1:
        maior = menor = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso
print(f'O maior valor digitado foi {maior} e o menor foi {menor}')
