from veiculo import Veiculo


class Carro(Veiculo):
    def ligar(self):
        self.ligado = True
        print("Carro ligado.")

    def parar(self):
        self.velocidade = 0
        print("Carro parado.")

    def acelerar(self, velocidade):
        if self.ligado:
            self.velocidade += velocidade
            print(f"Carro acelerando a {self.velocidade} km/h.")
        else:
            print("Você precisa ligar o carro primeiro.")

class Moto(Veiculo):
    def ligar(self):
        self.ligado = True
        print("Moto ligada.")

    def parar(self):
        self.velocidade = 0
        print("Moto parada.")

    def acelerar(self, velocidade):
        if self.ligado:
            self.velocidade += velocidade
            print(f"Moto acelerando a {self.velocidade} km/h.")
        else:
            print("Você precisa ligar a moto primeiro.")

class Caminhao(Veiculo):
    def ligar(self):
        self.ligado = True
        print("Caminhão ligado.")

    def parar(self):
        self.velocidade = 0
        print("Caminhão parado.")

    def acelerar(self, velocidade):
        if self.ligado:
            self.velocidade += velocidade
            print(f"Caminhão acelerando a {self.velocidade} km/h.")
        else:
            print("Você precisa ligar o caminhão primeiro.")
