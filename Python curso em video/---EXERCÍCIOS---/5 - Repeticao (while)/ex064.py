n = 0
tot = 0
totd = 0
tot9 = 0
while n != 999:
    n = int(input('Digite um numero: '))
    if n == 999:
        tot += n*0
        totd += 0
    else:
        tot += n
        totd += 1
print(f'FIM, a soma dos numeros foi {tot} e foram digitados {totd - tot9} numeros')