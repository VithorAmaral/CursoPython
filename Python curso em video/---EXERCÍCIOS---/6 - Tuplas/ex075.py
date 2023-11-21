n = (int(input('Digite um numero: ')), int(input('Digite um numero: ')), int(input('Digite um numero: ')), int(input('Digite um numero: ')))
print(f'O numero 9 apareceu {n.count(9)} vezes')
if 3 in n:
    print(f'O primeiro valor 3 apareceu na posição {n.index(3)+1}')
else:
    print('Não tem o numero 3 nessa lista')
for i in n:
    if i % 2 == 0:
        print(f'Os numeros pares sorteados foram: {i}')
