nome = input('Digite seu nome: ')
n1 = int(input('Digite a primeira nota: '))
n2 = int(input('Digite a segunda nota: '))
n3 = int(input('Digite a terceira nota: '))
n4 = int(input('Digite a quarta nota: '))
media = (n1+n2+n3+n4)/4
print(f'\nlegal {nome}, A sua media é {media}')
if media >= 7:
    print('Voce foi aprovado!')
else:
    print('Voce foi reprovado.')


