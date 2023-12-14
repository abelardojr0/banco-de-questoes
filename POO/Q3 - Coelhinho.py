# Definindo a classe Coelhinho
class Coelhinho:
    # Método construtor para inicializar os atributos
    def __init__(self, nome, raca, cor, idade):
        self.nome = nome  # Atributo para armazenar o nome do coelhinho
        self.raca = raca  # Atributo para armazenar a raça do coelhinho
        self.cor = cor    # Atributo para armazenar a cor do coelhinho
        self.idade = idade  # Atributo para armazenar a idade do coelhinho
    
    # Método para exibir todas as informações do coelhinho
    def ver_informacoes(self):
        return f"""
        Nome: {self.nome}
        Raça: {self.raca}\nCor: {self.cor}
        Idade: {self.idade}"""

# Instanciando um objeto da classe Coelhinho
meu_coelhinho = Coelhinho(nome="Pelinho", raca="Holandês", cor="Branco e Marrom", idade=1)

# Chamando o método ver_informacoes() e exibindo o resultado na tela
informacoes_coelhinho = meu_coelhinho.ver_informacoes()
print(informacoes_coelhinho)
