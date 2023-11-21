sal = float(input('Digite seu salario: '))
saln = 0
if sal < 500:
    saln = sal * 1.15
if 500 <= sal < 1000:
    saln = sal * 1.10
if sal > 1000:
    saln = sal * 1.05
print(f'O seu salario de R${sal}, com o ajuste foi para R${saln}')
