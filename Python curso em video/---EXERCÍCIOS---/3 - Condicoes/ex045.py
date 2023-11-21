import random
jo = str(input('Escolha entre Pedra, Papel, Tesoura: '))
lista = ['Pedra', 'Papel', 'Tesoura']
pc = random.choice(lista)
if pc == 'Tesoura' and jo == 'Papel':
    print('O computador escolheu Tesoura e voce escolheu papel, então voce perdeu')
elif pc == 'Tesoura' and jo == 'Pedra':
    print('O computador escolheu tesoura e voce escolheu pedra, voce ganhou')
elif pc == 'Pedra' and jo == 'Tesoura':
    print('O computador escolheu pedra e voce escolheu tesoura, voce perdeu')
elif pc == 'Pedra' and jo == 'Papel':
    print('O computador escolheu Pedra e voce escolheu papel, voce ganhou')
elif pc == 'Papel' and jo == 'Tesoura':
    print('O computador escolheu Papel e voce escolheu Tesoura, voce ganhou')
elif pc == 'Papel' and jo == 'Pedra':
    print('O computador escolheu Papel e voce escolheu Pedra, voce perdeu')
elif pc == 'Papel' and jo == 'Papel':
    print('Deu empate')
elif pc == 'Tesoura' and jo == 'Tesoura':
    print('Deu empate')
elif pc == 'Pedra' and jo == 'Pedra':
    print('Deu empate')

