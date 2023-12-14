# Definindo a superclasse Locadora
class Locadora:
    def __init__(self, nome, genero, ano):
        self.nome = nome
        self.genero = genero
        self.ano = ano
    
    def alugar(self, dia):
        return f"O {self.nome} foi alugado no dia {dia}"

# Criando a subclasse Jogo que herda de Locadora
class Jogo(Locadora):
    def __init__(self, nome, genero, ano, plataforma):
        # Chamando o construtor da superclasse
        super().__init__(nome, genero, ano)
        self.plataforma = plataforma  # Atributo específico para a classe Jogo

# Criando a subclasse Filme que herda de Locadora
class Filme(Locadora):
    def __init__(self, nome, genero, ano, duracao):
        # Chamando o construtor da superclasse
        super().__init__(nome, genero, ano)
        self.duracao = duracao  # Atributo específico para a classe Filme

# Instanciando objetos das subclasses
meu_jogo = Jogo(nome="The Last of Us", genero="Ação/Aventura", ano=2013, plataforma="PlayStation 4")
meu_filme = Filme(nome="Interestelar", genero="Ficção Científica", ano=2014, duracao="169 minutos")

# Chamando o método alugar() e exibindo informações sobre o aluguel
print(meu_jogo.alugar(dia="2023-01-15"))
print(meu_filme.alugar(dia="2023-01-15"))
