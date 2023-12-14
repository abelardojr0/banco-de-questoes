# Modificando a superclasse Veiculo para ser mais genérica
class Veiculo:
    def __init__(self, modelo, marca, ano, cor):
        self.modelo = modelo
        self.marca = marca
        self.ano = ano
        self.cor = cor
    
    def ligar(self):
        return f"O {self.modelo} ligou"

# Criando a nova subclasse Moto que herda de Veiculo
class Moto(Veiculo):
    def __init__(self, modelo, marca, ano, cor, cilindradas):
        # Chamando o construtor da superclasse
        super().__init__(modelo, marca, ano, cor)
        self.cilindradas = cilindradas  # Novo atributo específico para a classe Moto
    
    def empinar(self):
        return f"A moto {self.modelo} está empinando"

# Instanciando um objeto da classe Moto
minha_moto = Moto(modelo="YZF-R6", marca="Yamaha", ano=2022, cor="Azul", cilindradas=600)

# Chamando o método ligar() e o método específico para moto
print(minha_moto.ligar())
print(minha_moto.empinar())
