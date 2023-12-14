# Definindo a superclasse Animal
class Animal:
    # Método construtor para inicializar os atributos
    def __init__(self, nome, raca, cor, idade):
        self.nome = nome  # Atributo para armazenar o nome do animal
        self.raca = raca  # Atributo para armazenar a raça do animal
        self.cor = cor    # Atributo para armazenar a cor do animal
        self.idade = idade  # Atributo para armazenar a idade do animal
    
    # Método para exibir todas as informações do animal
    def ver_informacoes(self):
        return f"""
        Nome: {self.nome}
        Raça: {self.raca}\nCor: {self.cor}
        Idade: {self.idade}"""


# Criando a subclasse Cachorrinho que herda de Animal
class Cachorrinho(Animal):
    # Método construtor da subclasse
    def __init__(self, nome, raca, cor, idade):
        # Chamando o construtor da superclasse
        super().__init__(nome, raca, cor, idade)
    
    # Método específico para cachorro latir
    def latir(self):
        return f"O {self.nome} está latindo"


# Criando a subclasse Gatinho que herda de Animal
class Gatinho(Animal):
    # Método construtor da subclasse
    def __init__(self, nome, raca, cor, idade):
        # Chamando o construtor da superclasse
        super().__init__(nome, raca, cor, idade)


# Criando a subclasse Coelhinho que herda de Animal
class Coelhinho(Animal):
    # Método construtor da subclasse
    def __init__(self, nome, raca, cor, idade):
        # Chamando o construtor da superclasse
        super().__init__(nome, raca, cor, idade)


# Instanciando objetos das subclasses
meu_cachorrinho = Cachorrinho(nome="Buddy", raca="Labrador", cor="Amarelo", idade=3)
meu_gatinho = Gatinho(nome="Miau", raca="Siamese", cor="Branco", idade=2)
meu_coelhinho = Coelhinho(nome="Pelinho", raca="Holandês", cor="Branco e Marrom", idade=1)

# Exibindo as informações dos animais
print("Informações do Cachorrinho:")
print(meu_cachorrinho.ver_informacoes())
print(meu_cachorrinho.latir())  # Chamando o método específico para cachorro

print("Informações do Gatinho:")
print(meu_gatinho.ver_informacoes())

print("Informações do Coelhinho:")
print(meu_coelhinho.ver_informacoes())
