import random
tot = 0
n = int(input('Digite um numero de 1 a 10: '))
lista = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
ale = random.choice(lista)
while ale != n:
    tot += 1
    n = int(input('Não foi esse o numero escolhido! Tente de novo outro numero: '))
print(f'Parabéns, o numero escolhido pelo pc foi {ale}. Você acertou depois de {tot} tentativas!')
