# Relembrando a classe Locadora e subclasse Jogo da questão anterior
class Locadora:
    def __init__(self, nome, genero, ano):
        self.nome = nome
        self.genero = genero
        self.ano = ano
    
    def alugar(self, dia):
        return f"O {self.nome} foi alugado no dia {dia}"

class Jogo(Locadora):
    def __init__(self, nome, genero, ano, preco, modalidade):
        # Chamando o construtor da superclasse
        super().__init__(nome, genero, ano)
        self.preco = preco  # Novo atributo específico para a classe Jogo
        self.modalidade = modalidade  # Novo atributo específico para a classe Jogo
    
    def finalizar(self):
        return f"O jogo {self.nome} foi finalizado"

    # Polimorfismo do método alugar
    def alugar(self, dia):
        return f"O jogo {self.nome} foi alugado no dia {dia} e custou {self.preco} reais"

# Instanciando um objeto da classe Jogo
meu_jogo = Jogo(nome="The Last of Us", genero="Ação/Aventura", ano=2013, preco=50.0, modalidade="Single Player")

# Chamando os métodos alugar() e finalizar() e exibindo os resultados
dia_do_aluguel = "2023-01-15"
print(meu_jogo.alugar(dia=dia_do_aluguel))
print(meu_jogo.finalizar())
