from datetime import date
class carro:
    def __init__(self, modelo, marca, ano, combustivel):
        self.modelo = modelo
        self.marca = marca
        self.ano = ano
        self.combustivel = combustivel

    def getModelo(self):
        return self.modelo

    def setModelo(self, modelo):
        self.modelo = modelo

    def getMarca(self):
        return self.marca

    def setMarca(self, marca):
        self.marca = marca

    def getAno(self):
        return self.ano

    def setAno(self, ano):
        self.ano = ano

    def getCombustivel(self):
        return self.combustivel

    def setCombustivel(self, combustivel):
        self.combustivel = combustivel

    def consultarInsencaoIPVA(self):
        data_atual = date.today()
        ano_atual = int(data_atual.year)
        idadeVeiculo = ano_atual - self.ano

        if idadeVeiculo > 20:
            print('Este veiculo é isento de IPVA')
        else:
            if idadeVeiculo == 20:
                print('Seu veiculo será isento no proximo ano')
            else:
                print('Seu veiculo será isento em %d ano(s).' %(20-idadeVeiculo))
                print('Consulte o ipva no detran do seu estado')


c1 = carro('Fusca', 'VW', 1956, 'Gasolina')
print(c1.getModelo())
c1.consultarInsencaoIPVA()

print('')
c2 = carro('Polo', 'VW', 2019, 'Flex')
print(c2.getModelo())
c2.consultarInsencaoIPVA()

