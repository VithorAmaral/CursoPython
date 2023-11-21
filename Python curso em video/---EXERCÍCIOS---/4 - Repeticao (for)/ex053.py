f = str(input('Digite uma frase: ')).strip().upper()
palavras = f.split()
junto = ''.join(palavras)
inverso = ''
for letra in range(len(junto) - 1, -1, -1):
    inverso += junto[letra]
print(junto, inverso)
if junto == inverso:
    print('É um palindromo')
else:
    print('Não é um palindromo')
