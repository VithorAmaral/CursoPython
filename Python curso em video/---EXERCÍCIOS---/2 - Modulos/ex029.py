km = int(input('qual foi a sua velocidade em km? '))
if km <= 80:
    print('voce nao foi multado')
else:
    multa = (km - 80) * 7
    print('voce foi multado no valor de R${:.2f}'.format(multa))
