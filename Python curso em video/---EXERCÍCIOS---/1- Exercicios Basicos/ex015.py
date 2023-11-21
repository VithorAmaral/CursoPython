d = float(input('quantos dias o carro foi alugado? '))
km = float(input('quantos km rodou? '))
pd = d*60
pkm = km*0.15
vf = pd+pkm
print('o valor final foi de {:.2f} reais!'.format(vf))
