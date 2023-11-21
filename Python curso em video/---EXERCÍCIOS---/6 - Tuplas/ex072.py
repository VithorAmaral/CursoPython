num = ('Zero', 'Um', 'Dois', 'Tres', 'Quatro', 'Cinco', 'Seis', 'Sete', 'Oito', 'Nove', 'Dez', 'Onze', 'Doze', 'Treze', 'Quatorze', 'Quinze', 'Dezeseis', 'Dezesete', 'Dezoito', 'Dezenove', 'Vinte')

n = int(input('Digite um numero entre 0 e 20: '))
while 0 > n or n > 20:
    n = int(input('Tente novamente. Digite um numero entre 0 e 20: '))
print(f'Voce digitou o numero {num[n]}')
