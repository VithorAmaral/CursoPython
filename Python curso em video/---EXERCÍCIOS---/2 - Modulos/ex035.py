l1 = float(input('Escreva o comprimento da 1° reta: '))
l2 = float(input('Escreva o comprimento da 2° reta: '))
l3 = float(input('Escreva o comprimento da 3° reta: '))
if l1 < l2+l3 and l2 < l1+l3 and l3 < l1+l2:
    print('forma um triangulo')
else:
    print('nao forma um triangulo')