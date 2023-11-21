n = int(input('Escreva um numero qualquer: '))
d = int(input('Em qual formato voce quer a conversao? (1-Binario, 2-Octal, 3-Hexadecimal): '))
if d == 1:
    print('{} convertido em binario é: {}'.format(n, bin(n)[2:]))
elif d == 2:
    print('{} convertido em binario é: {}'.format(n, oct(n)[2:]))
elif d == 3:
    print('{} convertido em Hexadecimal é: {}'.format(n, hex(n)[2:]))
