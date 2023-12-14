class Tamagotchi:
    def __init__(self, nome, level, energia):
        self.nome = nome
        self.level = level
        self.energia = energia

    def comer(self):
        # Método para aumentar a energia em 10 pontos
        self.energia += 10
        return f"{self.nome} comeu e ganhou 10 pontos de energia. Energia atual: {self.energia}"

    def brincar(self):
        # Método para diminuir a energia em 15 pontos
        if self.energia >= 15:
            self.energia -= 15
            return f"{self.nome} brincou e gastou 15 pontos de energia. Energia atual: {self.energia}"
        else:
            return f"{self.nome} está muito cansado para brincar. Energia atual: {self.energia}"

# Instanciando um objeto da classe Tamagotchi
meu_tamagotchi = Tamagotchi(nome="Tama", level=1, energia=50)

# Usando os métodos comer() e brincar() e exibindo os resultados
print(meu_tamagotchi.comer())
print(meu_tamagotchi.brincar())
print(meu_tamagotchi.brincar())  # Tentando brincar novamente para mostrar a mensagem de cansaço
