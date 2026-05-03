import os

#nim -  jogo de estratégia
#consite em dois jogadores irem tirando palitinhos dentro de um conjunto de 21 palitihos
#o ultimo que tirar o palitinho ganha

class Main:
    def __init__(self):
        self.clear_page()
        self.iniciar()

    def iniciar(self):
        print("bem vindo ao NIM\n\n1. campeonato\n2. partida unica\n0. sair: ")

        while True:
            opcao = input()

            self.clear_page()
            if opcao in ['0','1','2']:
                break
            else:
                self.clear_page()
                print("opção invalida, tente novamente\n")


    @property
    def clear_page(self):
        try:
            os.system('cls')
        except:
            os.system('clear')


if __name__ == "__main__":
    Main()