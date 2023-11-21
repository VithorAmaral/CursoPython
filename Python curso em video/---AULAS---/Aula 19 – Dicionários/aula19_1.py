pessoas = {'Nome': 'Vithor', 'Sexo': 'M', 'Idade': '18'}
print(pessoas)
print(pessoas['Nome'])
print(pessoas['Idade'])
print(f'O {pessoas["Nome"]} tem {pessoas["Idade"]} anos')
print(pessoas.keys())
print(pessoas.values())
print(pessoas.items())
for k in pessoas.keys():
    print(k)
for k in pessoas.values():
    print(k)
for k, v in pessoas.items():
    print(f'{k} = {v}')