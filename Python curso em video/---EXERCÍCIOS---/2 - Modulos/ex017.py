import math
ca = float(input('informe o comprimento do cateto adjacente: '))
co = float(input('informe o comprimento do cateto oposto: '))
hipo = math.sqrt(co**2 + ca ** 2)
print('a hipotenusa mede: {}'.format(hipo))
