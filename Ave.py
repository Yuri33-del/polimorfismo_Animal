from Animal import Animal


class Ave(Animal):
    def __init__(self, nome, idade, cor_da_asas):
        super().__init__(nome, idade)
        self.cor_da_asas = cor_da_asas

    def fazer_som(self):
        return "A ave canta."

    def mover(self):
        return "A ave voa pelo céu."