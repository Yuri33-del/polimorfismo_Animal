from Animal import Animal


class Peixe(Animal):
    def __init__(self, nome, idade, tipo_de_escama):
        super().__init__(nome, idade)
        self.tipo_de_escama = tipo_de_escama

    def fazer_som(self):
        return "Os peixes não fazem som, são silenciosos."

    def mover(self):
        return "O peixe nada nas águas."