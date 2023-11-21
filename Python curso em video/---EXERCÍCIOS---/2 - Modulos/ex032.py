ano = int(input('Escreva um ano qualquer: '))
anobi = ano % 4
if anobi == 0:
    print('esse é um ano bissexto')
else:
    print('não é um ano bissexto')