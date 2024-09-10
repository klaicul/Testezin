from agenda import AgendaDeContatos

class AgendaDeContatosSimples(AgendaDeContatos):
    def adicionar_contato(self, nome, telefone, email):
        if nome not in self.contatos:
            self.contatos[nome] = {'telefone': telefone, 'email': email}
        else:
            print("Contato já existe na agenda.")

    def atualizar_contato(self, nome, telefone, email):
        if nome in self.contatos:
            self.contatos[nome] = {'telefone': telefone, 'email': email}
        else:
            print("Contato não encontrado.")

    def recuperar_contato(self, nome):
        return self.contatos.get(nome, None)

    def excluir_contato(self, nome):
        if nome in self.contatos:
            del self.contatos[nome]
        else:
            print("Contato não encontrado.")