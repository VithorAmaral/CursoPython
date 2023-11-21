n1 = float(input('Informe sua primeira nota: '))
n2 = float(input('Informe sua segunda nota: '))
media = (n1+n2)/2
if media < 5:
    print('Sua média foi de {} e voce esta reprovado'.format(media))
if 5 < media < 6.9:
    print('Sua media foi de {} e voce esta de recuperacao'.format(media))
if media > 7:
    print('Sua media foi de {} e voce esta aprovado'.format(media))
