r = 's'
media = 0
tot = 0
soma = 0
maior = 0
menor = 0
while r != 'n':
    n = int(input('Digite um numero: '))
    r = str(input('Quer continuar? '))
    soma += n
    tot += 1
    media = soma / tot
    if tot == 1:
        menor = n
        maior = n
    else:
        if n < menor:
            menor = n
        if n > maior:
            maior = n

print(f'FIM, voce digitou {tot} numeros e a média é {media}, o maior numero é o {maior} e o menor é o {menor}')

