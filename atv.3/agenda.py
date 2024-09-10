from abc import ABC, abstractmethod

class AgendaDeContatos(ABC):
    def __init__(self):
        self.contatos = {}

    @abstractmethod
    def adicionar_contato(self, nome, telefone, email):
        pass

    @abstractmethod
    def atualizar_contato(self, nome, telefone, email):
        pass

    @abstractmethod
    def recuperar_contato(self, nome):
        pass

    @abstractmethod
    def excluir_contato(self, nome):
        pass
