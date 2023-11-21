import moeda
numero = float(input('Digite o preço: R$ '))
print(F'A metade de {numero} é {moeda.metade(numero)}')
print(f'O dobro de {numero} é {moeda.dobro(numero)}')
print(f'Aumentando 10%, temos {moeda.aumentar(numero, 10)}')
print(f'Reduzindo 13%, temos {moeda.diminuir(numero, 13)}')