trabalhador = {}
trabalhador['nome'] = str(input('Digite o nome do trabalhador: '))
nasc = int(input('Digite o ano de nascimento do trabalhador: '))
trabalhador['idade'] = 2022 - nasc
trabalhador['carteira'] = int(input('Digite a carteira de trabalho(0 não tem): '))
if trabalhador['carteira'] != 0:
    trabalhador['ano'] = int(input('Ano de contratação: '))
    idadeano = 2022 - trabalhador['ano']
    apo = trabalhador['idade'] - idadeano
    trabalhador['salario'] = int(input('Salario: R$ '))
    trabalhador['aposentadoria'] = apo + 35
print(f'O nome do trabalhador é {trabalhador["nome"]}')
print(f'O(a) {trabalhador["nome"]} tem {trabalhador["idade"]} anos')
print(f'A carteira de trabalho do(a) {trabalhador["nome"]} é {trabalhador["carteira"]}')
if trabalhador["carteira"] != 0:
    print(f'O(a) {trabalhador["nome"]} foi contratado em {trabalhador["ano"]}')
    print(f'O(a) {trabalhador["nome"]} ganha R$ {trabalhador["salario"]}')
    print(f'O(a) {trabalhador["nome"]} vai se aposentar com {trabalhador["aposentadoria"]} anos')
