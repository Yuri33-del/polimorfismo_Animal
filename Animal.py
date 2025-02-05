class Animal:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def fazer_som(self):
        return "O animal faz um som."

    def mover(self):
        return "O animal se move."

    def alimentar(self):
        return f"O {self.nome} está se alimentando."