tot = 0
na = 0
for i in range(0, 7):
    n = int(input('Escreva o seu ano de nascimento: '))
    idade = 2022 - n
    if idade >= 21:
        tot += 1
    else:
        na += 1
print(f'{tot} são maiores de idade e {na} são menores de idade')

