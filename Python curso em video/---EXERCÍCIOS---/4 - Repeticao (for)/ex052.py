n = int(input('Digite um numero: '))
tot = 0
for i in range(1, n+1):
    if n % i == 0:
        tot +=1
if tot == 2:
    print('é um numero primo')
else:
    print('Não é um numero primo')