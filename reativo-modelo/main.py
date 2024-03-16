class AgenteReativo:
    def __init__(self, ambiente):
        self.ambiente = ambiente
        self.posicao = self.ambiente.posicao_inicial
        self.ambiente.posicao_agente = self.posicao  # Adicionado

    def acao(self):
        while self.posicao != self.ambiente.posicao_objetivo:
            acao = self.escolher_acao()
            self.executar_acao(acao)
            self.ambiente.mostrar_estado()

        print("Objetivo alcançado!")

    def escolher_acao(self):
        possiveis_acoes = self.ambiente.obter_acoes_disponiveis(self.posicao)
        import random

        return random.choice(possiveis_acoes)

    def executar_acao(self, acao):
        self.posicao = self.ambiente.transicao(self.posicao, acao)
        self.ambiente.posicao_agente = self.posicao  # Adicionado


class Ambiente:
    def __init__(self, tamanho, posicao_inicial, posicao_objetivo):
        self.tamanho = tamanho
        self.posicao_inicial = posicao_inicial
        self.posicao_objetivo = posicao_objetivo
        self.posicao_agente = None  # Adicionado

    def obter_acoes_disponiveis(self, posicao):
        possiveis_acoes = []
        x, y = posicao
        if x > 0:
            possiveis_acoes.append("cima")
        if x < self.tamanho[0] - 1:
            possiveis_acoes.append("baixo")
        if y > 0:
            possiveis_acoes.append("esquerda")
        if y < self.tamanho[1] - 1:
            possiveis_acoes.append("direita")
        return possiveis_acoes

    def transicao(self, posicao, acao):
        x, y = posicao
        if acao == "cima":
            return (x - 1, y)
        elif acao == "baixo":
            return (x + 1, y)
        elif acao == "esquerda":
            return (x, y - 1)
        elif acao == "direita":
            return (x, y + 1)

    def mostrar_estado(self):
        for i in range(self.tamanho[0]):
            for j in range(self.tamanho[1]):
                if (i, j) == self.posicao_inicial:
                    print("I", end=" ")
                elif (i, j) == self.posicao_objetivo:
                    print("O", end=" ")
                elif (i, j) == self.posicao_agente:  # Adicionado
                    print("A", end=" ")
                else:
                    print("-", end=" ")
            print()
        print()


ambiente = Ambiente(
    tamanho=(5, 5),
    posicao_inicial=(0, 0),
    posicao_objetivo=(4, 4))
agente = AgenteReativo(ambiente)
agente.acao()
