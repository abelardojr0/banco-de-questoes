# Definindo a classe Cachorrinho
class Cachorrinho:
    # Método construtor para inicializar os atributos
    def __init__(self, nome, raca, cor, idade):
        self.nome = nome  # Atributo para armazenar o nome do cachorrinho
        self.raca = raca  # Atributo para armazenar a raça do cachorrinho
        self.cor = cor    # Atributo para armazenar a cor do cachorrinho
        self.idade = idade  # Atributo para armazenar a idade do cachorrinho
    
    # Método para o cachorrinho latir
    def latir(self):
        return f"O {self.nome} está latindo"

# Instanciando um objeto da classe Cachorrinho
meu_cachorrinho = Cachorrinho(nome="Buddy", raca="Labrador", cor="Amarelo", idade=3)

# Chamando o método latir e exibindo o resultado na tela
print(meu_cachorrinho.latir())
