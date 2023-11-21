sal = float(input('Digite seu salario: '))
if sal >= 1250:
    salnovo = sal * 1.10
else:
    salnovo = sal * 1.15
print('seu salario de R${:.2f}, foi para R${:.2f}'.format(sal, salnovo))
