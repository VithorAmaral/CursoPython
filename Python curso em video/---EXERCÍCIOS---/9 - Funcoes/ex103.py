def ficha(nome='', gols=0):
    if nome == '':
        nome = '<desconhecido>'
    if gols.isnumeric():
        gols = int(gols)
    else:
        gols = 0
    print(f'O jogador {nome} fez {gols} gol(s) no campeonato.')


ficha(str(input('Nome do jogador: ')), str(input('Número de gols: ')))
