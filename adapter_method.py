import math

class BuracoRedondo:
    def __init__(self, raio):
        self.raio = raio

    def obter_raio(self):
        return self.raio

    def encaixa(self, pino):
        raio_buraco = self.obter_raio()
        raio_pino = pino.obter_raio()

        if raio_buraco >= raio_pino:
            return True
        else:
            return False

class PinoRedondo:
    def __init__(self, raio):
        self.raio = raio

    def obter_raio(self):
        return self.raio

class PinoQuadrado:
    def __init__(self, largura):
        self.largura = largura

    def obter_largura(self):
        return self.largura

#Adaptador para usar PinoQuadrado como PinoRedondo
class AdaptadorPinoQuadrado(PinoRedondo):
    def __init__(self, pino):
        self.pino_quadrado = pino

    def obter_raio(self):
        return (self.pino_quadrado.obter_largura() * math.sqrt(2))/2

buraco = BuracoRedondo(5) #Cria o tamanho do buraco
pino_redondo = PinoRedondo(5)

print("Pino redondo encaixa:", buraco.encaixa(pino_redondo))

pino_quadrado_pequeno = PinoQuadrado(5)
pino_quadrado_grande = PinoQuadrado(10)

adaptador_pequeno = AdaptadorPinoQuadrado(pino_quadrado_pequeno)
adaptador_grande = AdaptadorPinoQuadrado(pino_quadrado_grande)

print("Pino quadrado p encaixa:", buraco.encaixa(adaptador_pequeno))
print("Pino quadrado g encaixa:", buraco.encaixa(adaptador_grande))