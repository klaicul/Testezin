from abc import ABC, abstractmethod

class Veiculo(ABC):
    def __init__(self, rodas):
        self.rodas = rodas
        self.velocidade = 0
        self.ligado = False

    @abstractmethod
    def ligar(self):
        pass

    @abstractmethod
    def parar(self):
        pass

    @abstractmethod
    def acelerar(self, velocidade):
        pass

    def quantidade_rodas(self):
        return self.rodas
