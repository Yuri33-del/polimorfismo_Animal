from Animal import Animal


class Mamifero(Animal):
    def __init__(self, nome, idade, tipo_de_pelo):
        super().__init__(nome, idade)
        self.tipo_de_pelo = tipo_de_pelo

    def fazer_som(self):
        return "O mamífero emite um som característico."

    def mover(self):
        return "O mamífero anda sobre quatro patas ou duas."