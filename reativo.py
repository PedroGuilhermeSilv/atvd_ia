class AgenteReativoSimples:
    def agir(self, percepcao):
        if percepcao == "sujo":
            return "aspirar"
        else:
            return "nada"


class Ambiente:
    sala: str

    def __init__(self):
        self.sala = "limpa"

    def percepcao(self):
        return self.sala

    def sujar_sala(self):
        self.sala = "sujo"

    def limpar_sala(self):
        self.sala = "limpa"


# Criando o ambiente e o agente
ambiente = Ambiente()
agente = AgenteReativoSimples()


# Função para simular o ciclo de vida do agente
def ciclo_de_vida(
    agente: AgenteReativoSimples, ambiente: Ambiente, passos: InterruptedError
):
    for _, i in enumerate(range(passos)):
        percepcao_atual = ambiente.percepcao()
        print("Percepção atual:", percepcao_atual)

        acao = agente.agir(percepcao_atual)
        print("Ação escolhida:", acao)

        if acao == "aspirar":
            ambiente.limpar_sala()
            print("A sala foi aspirada.")
        else:
            print("Nenhuma ação realizada.")

        if i % 2 == 0:
            ambiente.sujar_sala()

        print("---------------")


# Testando o ciclo de vida do agente por 6 passos
ciclo_de_vida(agente, ambiente, 6)
