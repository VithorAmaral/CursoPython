aluno = {}
aluno['nome'] = str(input('Digite o nome do aluno: '))
aluno['media'] = float(input('Digite a média do aluno: '))
if aluno['media'] < 7:
    aluno['situação'] = 'Reprovado'
else:
    aluno['situação'] = 'Aprovado'
print(f'O nome é igual a {aluno["nome"]}')
print(f'A média é igual a {aluno["media"]}')
print(f'A situação é igual a {aluno["situação"]}')

