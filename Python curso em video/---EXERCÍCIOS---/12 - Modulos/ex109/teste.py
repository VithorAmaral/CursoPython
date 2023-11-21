import moeda
numero = float(input('Digite o preço: R$'))
print(f'A metade de {moeda.moeda(numero)} é {moeda.metade(numero, True)}')
print(f'O dobro de {moeda.moeda(numero)} é {moeda.dobro(numero, False)}')
print(f'Aumentando 10%, temos {moeda.aumentar(numero, 10, True)}')
print(f'Reduzindo 13%, temos {moeda.diminuir(numero, 13, False)}')


