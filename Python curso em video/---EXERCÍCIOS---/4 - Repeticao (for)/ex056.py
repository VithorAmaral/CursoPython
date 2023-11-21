media = 0
maioridadehomem = 0
nomevelho = ''
totmulher20 = 0
for i in range(0,4):
    n = str(input('Informe seu nome: '))
    idade = int(input('Informe sua idade: '))
    sexo = str(input('Informe seu sexo: '))
    media += idade/4
    if i == 1 and sexo == 'masculino':
        maioridadehomem = idade
        nomevelho = n
    if sexo == 'masculino' and idade > maioridadehomem:
        maioridadehomem = idade
        nomevelho = n
    if sexo == 'feminino' and idade < 20:
        totmulher20 += 1

print(f'A media de idade do grupo é de {media} anos.')
print(f'O homem mais velho tem {maioridadehomem} anos e se chama {nomevelho}')
print(f'São {totmulher20} mulheres com menos de 20 anos')
