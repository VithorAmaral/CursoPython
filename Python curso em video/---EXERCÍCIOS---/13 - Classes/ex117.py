class carro:
    velMax = 0
    ligado = False
    cor = ''

    def __init__(self, v, l, c):
        self.velMax = v
        self.ligado = l
        self.cor = c

    def mostrar(self):
        print(
            f'A velocidade maxima do carro: {self.velMax}\nO carro está ligado? {self.ligado}\nA cor do carro: {self.cor}')
        print('------------------------------')

    def ligar(self):
        self.ligado = True

    def desligar(self):
        self.ligado = False

    def andar(self):
        if self.ligado:
            print('Andando')
        else:
            print('Carro desligado')


c1 = carro(200, False, 'Preto')
c2 = carro(220, True, 'Branco')
c3 = carro(400, False, 'Azul')

c1.ligar()

c1.mostrar()
c2.mostrar()
c3.mostrar()

c1.andar()
c2.andar()
c3.andar()

