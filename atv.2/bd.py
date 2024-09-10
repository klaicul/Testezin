from abc import ABC, abstractmethod

class BancoDeDados(ABC):
    def __init__(self):
        self.registros = {}

    @abstractmethod
    def adicionar_registro(self, chave, valor):
        pass

    @abstractmethod
    def atualizar_registro(self, chave, valor):
        pass

    @abstractmethod
    def recuperar_registro(self, chave):
        pass

    @abstractmethod
    def excluir_registro(self, chave):
        pass
