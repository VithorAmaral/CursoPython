import random
n1 = input('Escreva o nome do aluno 1: ')
n2 = input('Escreva o nome do aluno 2: ')
n3 = input('Escreva o nome do aluno 3: ')
n4 = input('Escreva o nome do aluno 3: ')
lista = [n1, n2, n3, n4]
random.shuffle(lista)

print('a ordem de apresentação sera: ')
print(lista)