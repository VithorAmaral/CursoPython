vi = vh = vf20 = 0

while True:
    i = int(input('Digite sua idade: '))
    if i >= 18:
        vi += 1
    s = str(input('Digite seu sexo: (M/F): ')).strip().upper()
    if s == 'M':
        vh += 1
    if s == 'F' and i < 20:
        vf20 += 1
    cont = str(input('Quer continuar? (S/N): ')).strip().upper()
    if cont == 'N':
        break
print('Obrigado por utilizar o sistema!')
print(f'{vi} pessoas tem mais de 18 anos')
print(f'Foram cadastrados {vh} homens')
print(f'Foram cadastradas {vf20} mulheres com menos de 20 anos')
