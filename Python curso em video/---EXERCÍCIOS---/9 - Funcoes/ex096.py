def area(a, b):
    ar = a * b
    print(f'A area de um terreno de {a} x {b} é de {ar}m²')


print('      CONTROLE DE TERRENOS  ')
print('----------------------------')
area(float(input('LARGURA(M): ')), float(input('COMPRIMENTO(m): ')))
