# Definindo a superclasse Veiculo
class Veiculo:
    def __init__(self, modelo, marca, ano, cor):
        self.modelo = modelo
        self.marca = marca
        self.ano = ano
        self.cor = cor
    
    def ligar(self):
        return f"O {self.modelo} ligou"

# Criando a subclasse Carro que herda de Veiculo
class Carro(Veiculo):
    def __init__(self, modelo, marca, ano, cor, qtde_portas):
        # Chamando o construtor da superclasse
        super().__init__(modelo, marca, ano, cor)
        self.qtde_portas = qtde_portas  # Novo atributo específico para a classe Carro
    
# Instanciando um objeto da classe Carro
meu_carro = Carro(modelo="Civic", marca="Honda", ano=2022, cor="Prata", qtde_portas=4)

# Chamando o método ligar() e exibindo informações sobre o carro
print(meu_carro.ligar())
