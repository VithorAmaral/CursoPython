nasc = int(input('Informe a data de nascimento do atleta: '))
idade = 2022 - nasc
if idade <= 9:
    print('O atleta tem {} anos e é um atleta mirim'.format(idade))
elif 9 < idade <= 14:
    print('O atleta tem {} anos e é um atleta infantil'.format(idade))
elif 14 < idade <= 19:
    print('O atleta tem {} anos e é um atleta junior'.format(idade))
elif 19 < idade <= 20:
    print('O atleta tem {} anos e é um atleta senior'.format(idade))
elif idade > 20:
    print('O atleta tem {} anos e é um atleta master'.format(idade))

