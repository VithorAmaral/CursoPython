'''n1 = int(input('Digite um numero: '))
f = 1
c = n1
while c > 0:
    f *= c
    c -= 1
print(f)
'''
n1 = int(input('Digite um numero: '))
f = 1
for i in range(n1, 1, -1):
    f *= n1
    n1 -= 1
print(f)
