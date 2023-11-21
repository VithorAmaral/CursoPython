totpar = 0
totimpar = 0
n = 1
while n != 0:
    n = int(input('Digite um numero: '))
    if n != 0:
        if n % 2 == 0:
            totpar += 1
        else:
            totimpar += 1
print(f'{totimpar} numeros são ímpares e {totpar} são pares')