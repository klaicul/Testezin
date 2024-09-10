from bd import BancoDeDados

class BancoDeDadosSimples(BancoDeDados):
    def adicionar_registro(self, chave, valor):
        self.registros[chave] = valor

    def atualizar_registro(self, chave, valor):
        if chave in self.registros:
            self.registros[chave] = valor
        else:
            print("Registro não encontrado.")

    def recuperar_registro(self, chave):
        return self.registros.get(chave, None)

    def excluir_registro(self, chave):
        if chave in self.registros:
            del self.registros[chave]
        else:
            print("Registro não encontrado.")

# Exemplo de uso
banco = BancoDeDadosSimples()
banco.adicionar_registro(1, "Registro 1")
banco.adicionar_registro(2, "Registro 2")

print(banco.recuperar_registro(1))  # Saída: Registro 1

banco.atualizar_registro(1, "Novo Registro 1")
print(banco.recuperar_registro(1))  # Saída: Novo Registro 1

banco.excluir_registro(2)
print(banco.recuperar_registro(2))  # Saída: None
