p = float(input('Escreva seu peso: '))
a = float(input('Escreva sua altura: '))
imc = p/a ** 2
if imc < 18.5:
    print('Seu imc é de {:.1f} e voce esta abaixo do peso'.format(imc))
elif 18.6 < imc <= 25:
    print('Seu imc é de {:.1f} e voce está no peso ideal'.format(imc))
elif 25.1 < imc <= 30:
    print('Seu imc é de {:.1f} e voce esta sobrepeso'.format(imc))
elif 30.1 < imc <=40:
    print('Seu imc é de {:.1f} e voce está obeso'.format(imc))
elif imc > 40.1:
    print('Seu imc é de {:.1f} e voce esta em obesidade morbida'.format(imc))
