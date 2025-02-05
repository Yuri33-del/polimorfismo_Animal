from Ave import Ave
from Mamifero import Mamifero
from Peixe import Peixe


def exibir_informacoes(animal):
    print(f"Nome: {animal.nome}")
    print(f"Idade: {animal.idade}")
    print(f"Som: {animal.fazer_som()}")
    print(f"Movimento: {animal.mover()}")
    print(f"Alimentação: {animal.alimentar()}")
    print("-" * 50)


# Programa principal para testar a implementação
def main():
    # Criando objetos de diferentes tipos de animais
    leao = Mamifero("Leão", 5, "denso")
    papagaio = Ave("Papagaio", 2, "verde")
    tubarao = Peixe("Tubarão", 8, "rugosa")

    # Exibindo informações dos animais
    exibir_informacoes(leao)
    exibir_informacoes(papagaio)
    exibir_informacoes(tubarao)


if __name__ == "__main__":
    main()