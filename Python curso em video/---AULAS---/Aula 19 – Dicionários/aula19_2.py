pessoas = {'Nome': 'Vithor', 'Sexo': 'M', 'Idade': '18'}
del pessoas['Sexo']
for k, v in pessoas.items():
    print(f'{k} = {v}')