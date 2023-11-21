def voto(anodenasc):
    idade = 2022 - anodenasc
    if idade < 16:
        print(f'Com {idade} anos: VOTO NEGADO.')
    if 16 <= idade < 18:
        print(f'Com {idade} anos: VOTO OPCIONAL.')
    if 18 <= idade < 65:
        print(f'Com {idade} anos: VOTO OBRIGATÓRIO')
    if idade > 65:
        print(f'Com {idade} anos: VOTO OPCIONAL')


# Programa Principal
voto(int(input('Digite o seu ano de nascimento: ')))

