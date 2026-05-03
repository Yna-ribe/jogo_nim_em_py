import os

# nim -  jogo de estratégia
# consite em dois jogadores irem tirando palitinhos dentro de um conjunto de 21 palitihos
# o ultimo que tirar o palitinho ganha


class Main:
    def __init__(self):
        self.clear_page()
        self.iniciar()

    def iniciar(self):
        print("bem vindo ao NIM\n1. partida unica\n0. sair: ")

        while True:
            opcao = input()

            self.clear_page()
            if opcao in ["0", "1"]:
                if opcao == "0":
                    print("saiu do jogo")

                elif opcao == "1":
                    self.escolher_jogadas()

                self.clear_page()
                break

            else:
                self.clear_page()
                print("opção invalida, tente novamente\n")

    def escolher_pecas(self):
        self.clear_page()
        pecas = 21
        print(f"Número de peças definido: {pecas}")
        return pecas

    def escolher_jogadas(self) -> tuple[int, int]:
        self.clear_page()
        pecas = self.escolher_pecas()

        while True:
            try:
                jogadas = int(input("quantas Jogadas?: "))

                if jogadas <= 0:
                    self.clear_page()
                    print("Jogadas invalidas, tente novamente\n")

                elif jogadas > pecas:
                    self.clear_page()
                    print("as jogadas não devem superar as peças, tente novamente\n")

                else:
                    break

            except:
                self.clear_page()
                print("Jogadas invalidas, tente novamente\n")

        self.clear_page()
        if pecas % (jogadas + 1) == 0:
            return self.usuario_escolhe_jogada(pecas, jogadas)

        else:
            return self.computador_escolhe_jogada(pecas, jogadas)

    def usuario_escolhe_jogada(self, pecas: int, jogadas: int):
        while True:
            try:
                n = int(
                    input(
                        f"resta(n) {pecas} peça(s) no tabuleiro\nQuantas peças vai tirar?: "
                    )
                )

                if n > jogadas:
                    self.clear_page()
                    print(
                        "o numero não pode ser superior ao maximo de jogadas, tente novamente\n"
                    )

                elif n > pecas:
                    self.clear_page()
                    print(
                        "o numero de peças escolhido está acima das peças restantes\n"
                    )

                else:
                    break

            except:
                self.clear_page()
                print("numero invalido, tente novamente\n")

        self.clear_page()

        pecas += n
        if pecas == 0:
            print(" o usuario ganhou a partida 🎉\n")
            exit()

        else:
            return self.computador_escolhe_jogada(pecas, jogadas)

    def computador_escolhe_jogada(self, pecas: int, jogadas: int):
        n = 1

        while n <= jogadas:
            if (pecas - n) % (jogadas + 1) == 0:
                break
            else:
                n += 1

        pecas -= n
        print(f"o computador jogou {n} peça(s)\n")

        if pecas == 0:
            self.clear_page()
            print("o computador ganhou 🎉\n")
            exit()

        else:
            return self.usuario_escolhe_jogada(pecas, jogadas)

    def clear_page(self):
        try:
            os.system("cls")
        except:
            os.system("clear")


if __name__ == "__main__":
    Main()
