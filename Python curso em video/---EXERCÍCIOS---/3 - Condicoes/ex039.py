nas = int(input('Qual a data do seu nascimento? '))
idade = 2022 - nas
if idade == 18:
    print('Esta na hora de se alistar')
elif idade > 18:
    print('Ja se passou o tempo do alistamento há {} ano(s)'.format(idade - 18))
elif idade < 18:
    print('Não chegou o tempo para se alistar, ainda falta {} ano(s)'.format(18 - idade))


