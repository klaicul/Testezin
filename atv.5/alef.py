import random
from abc import ABC, abstractmethod

class Personagem(ABC):
    def __init__(self, nome, vida):
        self.nome = nome
        self.vida = vida

    @abstractmethod
    def atacar(self, alvo):
        pass

    @abstractmethod
    def defender(self, dano):
        pass

class Guerreiro(Personagem):
    def atacar(self, alvo):
        dano = random.randint(10, 20)
        print(f"{self.nome} ataca {alvo.nome} causando {dano} de dano.")
        alvo.defender(dano)

    def defender(self, dano):
        if random.random() < 0.3:
            print(f"{self.nome} defendeu o ataque.")
            dano = dano // 2
        self.vida -= dano
        if self.vida <= 0:
            print(f"{self.nome} foi derrotado!")

class Mago(Personagem):
    def atacar(self, alvo):
        dano = random.randint(15, 25)
        print(f"{self.nome} lança um feitiço em {alvo.nome} causando {dano} de dano.")
        alvo.defender(dano)

    def defender(self, dano):
        if random.random() < 0.2:
            print(f"{self.nome} desviou do ataque.")
            dano = 0
        self.vida -= dano
        if self.vida <= 0:
            print(f"{self.nome} foi derrotado!")

class Arqueiro(Personagem):
    def atacar(self, alvo):
        dano = random.randint(5, 15)
        print(f"{self.nome} dispara uma flecha em {alvo.nome} causando {dano} de dano.")
        alvo.defender(dano)

    def defender(self, dano):
        if random.random() < 0.4:
            print(f"{self.nome} esquivou do ataque.")
            dano = 0
        self.vida -= dano
        if self.vida <= 0:
            print(f"{self.nome} foi derrotado!")

class Monstro:
    def __init__(self, nome, vida):
        self.nome = nome
        self.vida = vida

    def atacar(self, alvo):
        dano = random.randint(5, 15)
        print(f"{self.nome} ataca {alvo.nome} causando {dano} de dano.")
        alvo.defender(dano)

    def defender(self, dano):
        if random.random() < 0.3:
            print(f"{self.nome} defendeu o ataque.")
            dano = dano // 2
        self.vida -= dano
        if self.vida <= 0:
            print(f"{self.nome} foi derrotado!")

# Função para simular o duelo
def duelo(personagens, monstros):
    for personagem in personagens:
        alvo = random.choice(monstros)
        personagem.atacar(alvo)

    for monstro in monstros:
        if monstro.vida > 0:
            alvo = random.choice(personagens)
            monstro.atacar(alvo)

# Criando personagens e monstros5
guerreiro = Guerreiro("Guerreiro", 100)
mago = Mago("Mago", 80)
arqueiro = Arqueiro("Arqueiro", 90)

monstro1 = Monstro("Monstro 1", 50)
monstro2 = Monstro("Monstro 2", 60)

# Simulando o duelo
duelo([guerreiro, mago, arqueiro], [monstro1, monstro2])

# Exibindo status após o duelo
print(f"Status dos personagens:")
print(f"{guerreiro.nome}: Vida = {guerreiro.vida}")
print(f"{mago.nome}: Vida = {mago.vida}")
print(f"{arqueiro.nome}: Vida = {arqueiro.vida}")

print("\nStatus dos monstros:")
print(f"{monstro1.nome}: Vida = {monstro1.vida}")
print(f"{monstro2.nome}: Vida = {monstro2.vida}")
