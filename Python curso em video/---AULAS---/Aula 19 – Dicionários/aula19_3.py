pessoas = {'Nome': 'Vithor', 'Sexo': 'M', 'Idade': '18'}
pessoas['Nome'] = 'Leandro'
pessoas['peso'] = 98.5
for k, v in pessoas.items():
    print(f'{k} = {v}')