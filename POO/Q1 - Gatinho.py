# Definindo a classe Gatinho
class Gatinho:
    # Método construtor para inicializar os atributos
    def __init__(self, nome, raca, cor, idade):
        self.nome = nome  # Atributo para armazenar o nome do gatinho
        self.raca = raca  # Atributo para armazenar a raça do gatinho
        self.cor = cor    # Atributo para armazenar a cor do gatinho
        self.idade = idade  # Atributo para armazenar a idade do gatinho

# Instanciando um objeto da classe Gatinho
meu_gatinho = Gatinho(nome="Miau", raca="Siamese", cor="Branco", idade=2)

# Exibindo os atributos do gatinho na tela
print("Nome:", meu_gatinho.nome)
print("Raça:", meu_gatinho.raca)
print("Cor:", meu_gatinho.cor)
print("Idade:", meu_gatinho.idade)
