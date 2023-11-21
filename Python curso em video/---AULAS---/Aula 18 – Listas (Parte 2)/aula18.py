test = list()
test.append('Vithor')
test.append(18)
galera = list()
galera.append(test[:])
test[0] = 'Maria'
test[1] = 22
galera.append(test[:])
print(galera)
