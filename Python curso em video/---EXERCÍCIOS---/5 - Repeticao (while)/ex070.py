p = vp = menor = cont = 0
barato = ''
while True:
    n = str(input('Digite o nome do produto: '))
    preco = float(input('Digite o preço do produto: '))
    cont += 1
    if preco >= 1000:
        vp += 1
    if cont == 1:
        menor = preco
        barato = n
    else:
        if preco < menor:
            menor = preco
            barato = n
    p += preco
    cond = str(input('Quer continuar (S/N): ')).strip().upper()[0]
    if cond == 'N':
        break
print('Obrigado')
print(f'Sua compra deu um total de {p:.2f} reais')
print(f'{vp} produtos custaram mais de 1.000 reais')
print(f'O produto mais barato foi {barato} e custa {menor:.2f} reais')
