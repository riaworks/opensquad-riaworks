# Task: Pontuar Conteudo Contra Criterios de Qualidade

## Task Config

```yaml
order: 1
```

## Objetivo

Avaliar o conteudo de carrossel e/ou Reel contra criterios de qualidade predefinidos, atribuindo pontuacao de 1 a 10 para cada criterio com justificativa detalhada.

## Processo

### 1. Recebimento e Contextualizacao

- Receber o conteudo finalizado (PNGs do carrossel e/ou roteiro do Reel)
- Identificar o tipo de conteudo sendo avaliado
- Carregar os criterios de qualidade relevantes do agente criador
- Verificar se e primeira avaliacao ou revisao (e qual ciclo: 1, 2 ou 3)

### 2. Avaliacao de Carrossel

Pontuar cada criterio de 1 a 10 com justificativa:

**Criterios Visuais:**
- **Legibilidade:** Todos os textos sao legiveis em tela de celular? Fontes respeitam tamanhos minimos?
- **Contraste:** Texto tem contraste WCAG AA (4.5:1) contra o fundo?
- **Hierarquia visual:** O olho sabe para onde ir primeiro em cada slide?
- **Consistencia:** Todos os slides parecem pertencer ao mesmo carrossel?
- **Margens:** Area de seguranca de 60px respeitada em todos os slides?

**Criterios de Conteudo:**
- **Clareza da mensagem:** A mensagem principal e compreendida em leitura rapida?
- **Fluxo narrativo:** A progressao entre slides faz sentido e mantem interesse?
- **CTA:** A chamada para acao e clara, relevante e acionavel?

### 3. Avaliacao de Reel

Pontuar cada criterio de 1 a 10 com justificativa:

**Criterios de Estrutura:**
- **Hook:** Os primeiros 2 segundos capturam atencao?
- **Timing:** A duracao esta entre 15-30s? O ritmo e adequado?
- **Cortes:** Ha transicoes a cada 3-5 segundos?
- **Loop:** O final conecta ao inicio de forma natural?

**Criterios de Acessibilidade:**
- **Legendas:** Texto na tela presente e legivel em todos os momentos?
- **Som desligado:** O Reel faz sentido completo sem audio?

**Criterios de Engajamento:**
- **CTA:** A chamada para acao e integrada e nao intrusiva?
- **Caption:** O texto do post complementa o video?
- **Hashtags:** Relevantes e com mix de volume adequado?

### 4. Calculo de Media e Classificacao

- Calcular media ponderada dos criterios
- Classificar conforme faixas:
  - **9-10:** Excelente — pronto para publicacao
  - **7-8:** Bom — sugestoes opcionais de melhoria
  - **5-6:** Aceitavel — revisao recomendada em pontos especificos
  - **4:** Limite — revisao obrigatoria em pontos bloqueantes
  - **1-3:** Insuficiente — rejeicao, refazer conteudo

## Formato de Entrega

```markdown
## Pontuacao: [Tipo de Conteudo] — [Tema]

| Criterio | Nota | Justificativa |
|----------|------|---------------|
| [nome]   | X/10 | [evidencia]   |
| ...      | ...  | ...           |

**Media:** X.X/10
**Classificacao:** [Excelente/Bom/Aceitavel/Limite/Insuficiente]
**Ciclo de revisao:** [1/2/3] de 3
```

## Criterios de Conclusao

- Todos os criterios aplicaveis avaliados com nota de 1 a 10
- Cada nota acompanhada de justificativa com evidencia especifica
- Media calculada corretamente
- Classificacao atribuida conforme faixas definidas
- Ciclo de revisao registrado
- Nenhum criterio avaliado de forma vaga ou sem referencia ao conteudo
