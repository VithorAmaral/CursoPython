t = int(input('Escreva o primeiro termo: '))
r = int(input('Escreva a razao da pa: '))
dt = t + (10-1) * r
for i in range(t, dt, r):
    print(i)
