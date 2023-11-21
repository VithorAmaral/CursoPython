time = []
jogador = {}
partidas = []

while True:
    jogador.clear()
    jogador["nome"] = str(input('Digite o nome do jogador: '))
    tot = int(input(f'Digite quantas partidas o {jogador["nome"]} jogou: '))
    partidas.clear()
    for c in range(tot):
        partidas.append(int(input(f'Quantos gols na partida {c+1}? ')))
    jogador["gols"] = partidas[:]
    jogador["total"] = sum(partidas)
    time.append(jogador.copy())
    while True:
        resp = str(input('Quer continuar?(S/N): ')).upper()
        if resp in 'SN':
            break
        print('Erro! Responda apenas S ou N.')
    if resp == 'N':
        break
print('-='* 30)
print('cod', end='')
for i in jogador.keys():
    print(f'{i:<15}', end='')
print()
print('-' * 40)
for k, v in enumerate(time):
    print(f'{k:>3}', end=' ')
    for d in v.values():
        print(f'{str(d):<15}', end='')
    print()
print('_' * 40)
while True:
    busca = int(input('Mostrar dados de qual jogador? '))
    if busca == 999:
        break
    if busca >= len(time):
        print(f'Erro! Não existe jogador com codigo {busca}')
    else:
        print(f' --- LEVANTAMENTO DO JOGADOR {time[busca]["nome"]}:')
        for i, g in enumerate(time[busca]["gols"]):
            print(f'    No jogo {i+1} fez {g} gols')
    print('-'*40)
print('<< VOLTE SEMPRE >>')