soma = 0
for i in range(1, 501):
    if i % 2 == 1 and i % 3 == 0:
        soma += i
print(f'A soma de todos os valores solicitados é {soma}.')

