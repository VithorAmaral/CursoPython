val = float(input('Escreva o valor da casa: '))
sal = float(input('Quanto voce ganha? '))
anos = int(input('Em quantos anos voce vai pagar essa casa? '))
valm = val/(anos*12)
if valm > 0.3*sal:
    print('Voce nao pode pedir o emprestimo')
else:
    print('Voce pode pedir o emprestimo')
print('O valor dessa casa é de R${:.2f} por mes'.format(valm))
