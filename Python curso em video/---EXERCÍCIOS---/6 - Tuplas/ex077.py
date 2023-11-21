tupla = ('Arroz', 'Feijao', 'Maionese', 'Batata', 'Sorvete', 'Tomate', 'Carne', 'Tamandua', 'Formiga', 'Brocolis', 'Gabigol')
for i in tupla:
    print(f'\nNa palavra {i.upper()} temos ', end='')
    for letra in i:
        if letra.lower() in "aeiou":
            print(letra, end=' ')
