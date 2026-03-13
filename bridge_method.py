from abc import ABC, abstractmethod

class Cor(ABC):
    @abstractmethod
    def aplicar_cor(self):
        pass

class Vermelho(Cor):
    def aplicar_cor(self):
        return "vermelho"

class Azul(Cor):
    def aplicar_cor(self):
        return "azul"

class Forma:
    def __init__(self, cor):
        self.cor = cor

    def desenhar(self):
        pass

class Circulo(Forma):
    def desenhar(self):
        print(f"Desenhando círculo de cor {self.cor.aplicar_cor()}")

class Quadrado(Forma):
    def desenhar(self):
        print(f"Desenhando quadrado de cor {self.cor.aplicar_cor()}")

cor_vermelha = Vermelho()
cor_azul = Azul()

circulo = Circulo(cor_vermelha)
quadrado = Quadrado(cor_azul)

circulo.desenhar()
quadrado.desenhar()