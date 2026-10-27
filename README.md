# Jogo do Nim em Python

Este projeto é uma implementação em **Python** (utilizando Paradigma Orientado a Objetos) do clássico **Jogo do Nim**, um jogo de estratégia matemática milenar disputado entre dois jogadores.

---

## Regras do Jogo

1. **Início da Partida:** O jogo começa com um total fixo de **21 peças** (palitinhos) no tabuleiro.
2. **Dinâmica de Turnos:** Os participantes (usuário vs. computador) jogam de forma alternada, removendo uma quantidade permitida de peças por rodada.
3. **Limite de Jogadas:** No início da partida, define-se o limite máximo de peças que podem ser retiradas por jogada.
4. **Condição de Vitória:** O jogador que realizar a última retirada de peças e esvaziar o tabuleiro vence a partida! 🎉

---

## Arquitetura e Funcionalidades

O código está estruturado dentro da classe principal `Main`, dividindo-se nas seguintes responsabilidades:

* **Menu Interativo (`iniciar`):** Permite ao usuário iniciar uma partida única ou sair do jogo diretamente pelo terminal.
* **Configuração de Tabuleiro e Limites (`escolher_pecas` e `escolher_jogadas`):**
  * Inicializa as 21 peças padrão.
  * Valida a entrada do usuário para garantir que o limite de jogadas por turno seja um número válido e coerente com as peças restantes.
  * Utiliza uma lógica matemática baseada no resto da divisão (`pecas % (jogadas + 1)`) para decidir estrategicamente quem fará o primeiro movimento.
* **Turno do Usuário (`usuario_escolhe_jogada`):** Gerencia a entrada interativa via terminal, validando se a quantidade de peças escolhida respeita os limites estabelecidos e atualizando o estado do jogo.
* **Inteligência Artificial (`computador_escolhe_jogada`):** A IA calcula de forma autônoma a jogada ideal para deixar o total restante em um múltiplo de `(jogadas + 1)`, assumindo o controle matemático da partida e buscando a vitória de forma inteligente.
* **Utilitário de Tela (`clear_page`):** Limpa o terminal automaticamente a cada turno, garantindo uma melhor experiência visual (compatível com Windows via `cls` e sistemas Unix/Linux/macOS via `clear`).

---
