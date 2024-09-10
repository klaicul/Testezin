from Formageometrica import FormaGeometrica
import math

class Quadrado(FormaGeometrica):
    def __init__(self, lado):
        self.lado = lado

    def calcular_area(self):
        return self.lado ** 2

    def calcular_perimetro(self):
        return 4 * self.lado

class Circulo(FormaGeometrica):
    def __init__(self, raio):
        self.raio = raio

    def calcular_area(self):
        return math.pi * self.raio ** 2

    def calcular_perimetro(self):
        return 2 * math.pi * self.raio

class Triangulo(FormaGeometrica):
    def __init__(self, lado1, lado2, lado3):
        self.lado1 = lado1
        self.lado2 = lado2
        self.lado3 = lado3

    def calcular_area(self):
        s = (self.lado1 + self.lado2 + self.lado3) / 2
        return math.sqrt(s * (s - self.lado1) * (s - self.lado2) * (s - self.lado3))

    def calcular_perimetro(self):
        return self.lado1 + self.lado2 + self.lado3

quadrado = Quadrado(5)
print("Área do quadrado:", quadrado.calcular_area())
print("Perímetro do quadrado:", quadrado.calcular_perimetro())