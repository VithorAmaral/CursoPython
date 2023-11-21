nome = input('Digite seu nome: ')
quant_notas = int(input('Quantas notas gostaria de avaliar? '))

notas = []

for i in range(0, quant_notas):
    nota = float(input(f'Digite a nota{i+1}: '))

soma_notas = 0

for cada_nota in notas:
    soma_notas += cada_nota

media = soma_notas/quant_notas

print(f'Legal {nome}! A sua média é de {media:.2f}')
