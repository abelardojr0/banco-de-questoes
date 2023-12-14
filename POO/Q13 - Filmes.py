# Relembrando a classe Locadora e subclasse Filme da questão anterior
class Locadora:
    def __init__(self, nome, genero, ano):
        self.nome = nome
        self.genero = genero
        self.ano = ano
    
    def alugar(self, dia):
        return f"O {self.nome} foi alugado no dia {dia}"

class Filme(Locadora):
    def __init__(self, nome, genero, ano, duracao, elenco):
        # Chamando o construtor da superclasse
        super().__init__(nome, genero, ano)
        self.duracao = duracao  # Novo atributo específico para a classe Filme
        self.elenco = elenco  # Novo atributo específico para a classe Filme
    
    def em_cartaz(self):
        return f"O filme {self.nome} está em cartaz"

    # Polimorfismo do método alugar
    def alugar(self, dia):
        return f"O filme {self.nome} foi alugado no dia {dia} de graça"

# Instanciando um objeto da classe Filme
meu_filme = Filme(nome="Interestelar", genero="Ficção Científica", ano=2014, duracao="169 minutos", elenco=["Matthew McConaughey", "Anne Hathaway"])

# Chamando os métodos alugar() e em_cartaz() e exibindo os resultados
dia_do_aluguel = "2023-01-15"
print(meu_filme.alugar(dia=dia_do_aluguel))
print(meu_filme.em_cartaz())
