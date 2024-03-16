## Agente Reativo Simples:
- **Baseado em Percepção Atual:** O agente reativo simples decide suas ações exclusivamente com base nas percepções imediatas do ambiente. Ele não considera o histórico de percepções nem prevê as consequências de suas ações.

- **Decisões Diretas:** Cada percepção resulta em uma ação específica. Não há raciocínio complexo ou ponderação de opções. O agente simplesmente associa cada percepção a uma ação pré-programada.

- **Sem Modelo Interno:** Ao contrário de outros tipos de agentes, como os baseados em modelos, o agente reativo simples não mantém um modelo interno do ambiente. Ele não tenta entender ou representar o estado completo do ambiente.

- **Limitações de Complexidade:** Devido à sua simplicidade, os agentes reativos simples são adequados apenas para ambientes muito simples e previsíveis. Eles podem ser eficazes em ambientes onde as ações necessárias são óbvias e diretas com base em percepções imediatas

## Exemplo:
- No exemplo citado tempo, o `AgenteReativoSimples` que interage com o `Ambiente`, caso a percepção do ambiente seja igual a sujo o agente irá aspirar senão ele não faz nada.