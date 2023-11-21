pre = float(input('Qual o preço do produto? '))
cond = int(input('Como voce vai pagar? (1-A vista no dinheiro/cheque, 2-A vista no cartão, 3-Em até 2x no cartão, 4-Em 3x ou mais no cartão): '))
if cond == 1:
    avista = pre * 0.90
    print("O valor final ficou R${}".format(avista))
elif cond == 2:
    avistac = pre * 0.95
    print('O valor final ficou de R${}'.format(avistac))
elif cond == 3:
    print('O valor final ficou de R${}'.format(pre))
elif cond == 4:
    tre = pre * 1.20
    print('O valor final ficou de R${}'.format(tre))

