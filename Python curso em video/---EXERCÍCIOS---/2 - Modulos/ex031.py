dist = float(input('Escreva a distancia em km: '))
if dist >= 200:
    cobra = dist * 0.45
else:
    cobra = dist * 0.50
print('o preco da sua viagem foi de R${}'.format(cobra))
