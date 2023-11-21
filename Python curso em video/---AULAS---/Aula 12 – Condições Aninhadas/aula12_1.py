nome = str(input('Qual é o seu nome? '))
if nome == 'Vithor':
    print('Que nome bonito')
elif nome in 'Ana Claudia Jessica Juliana':
    print('Belo nome feminino')
elif nome == 'Pedro' or nome == 'Maria' or nome == 'Paulo':
    print('Seu nome é bem popular no Brasil')
else:
    print('voce tem um nome normal')
print('Tenha um bom dia, {}!'.format(nome))
