---
id: optimize-instagram-feed
name: "Otimizar Carrossel Instagram"
order: 3
---

## Objective

Otimizar o carrossel criado na task anterior através de testes A/B de hooks, refinamento de hashtags, melhoria do CTA e um quality pass final para maximizar performance no Instagram.

## Process

### Step 1 — A/B Testing de Hooks

Gerar 3 variações alternativas para o hook do Slide 1, cada uma usando uma técnica diferente:
- **Variação A — Dado chocante:** Liderar com o número mais impactante da notícia
- **Variação B — Pergunta provocativa:** Abrir com uma pergunta que o leitor não consegue ignorar
- **Variação C — Afirmação contrária:** Começar com uma declaração que desafia a expectativa

Para cada variação, escrever também a primeira linha da caption correspondente (máx 125 chars).
Avaliar e recomendar a melhor opção com justificativa baseada em padrões de engajamento.

### Step 2 — Otimização de Hashtags

Revisar o bloco de hashtags e aplicar a estratégia 5-5-5:
- **5 hashtags de alto volume** (500K+ posts): para alcance e descoberta (#tecnologia, #ia, #programacao)
- **5 hashtags de médio volume** (50K-500K): para competição equilibrada (#devbrasil, #techbrasil)
- **5-10 hashtags de nicho** (5K-50K): para audiência qualificada (#iaparadevs, #automatizacaotech)

Remover hashtags banidas, irrelevantes ou muito saturadas. Verificar relevância de cada hashtag para o tema específico do carrossel.

### Step 3 — Refinamento do CTA

Avaliar o CTA atual nos dois pontos de contato:
- **Slide final:** O CTA entrega valor adicional? Dá uma razão concreta para agir? Evita o genérico "siga para mais"?
- **Caption:** A pergunta/instrução final é específica o suficiente para gerar comentários reais?

Reescrever se necessário, aplicando a fórmula: **Ação específica + Benefício claro + Baixa fricção**.

### Step 4 — Quality Pass Final

Revisar todo o conteúdo verificando:
- Ortografia e gramática em português brasileiro
- Consistência de tom entre slides e caption
- Palavras por slide dentro do range 40-80
- Primeira linha da caption dentro de 125 caracteres
- Fluxo narrativo coeso do slide 1 ao último
- Nenhum claim sem dados de suporte
- Nenhum anti-pattern presente (ver agent.md)

## Output Format

Apresentar as otimizações de forma comparativa (antes/depois) e o carrossel final consolidado.

## Output Example

```
## Otimização do Carrossel: [Título]

### A/B Hooks

| Variação | Hook Slide 1 | Caption L1 | Recomendação |
|----------|-------------|------------|--------------|
| Original | "O Google acaba de matar essa profissão" | "🔥 O Google lançou uma IA que faz code review melhor que devs" | — |
| A (Dado) | "47% mais rápido que qualquer dev humano" | "🔥 Uma IA acaba de superar devs em code review por 47%" | — |
| B (Pergunta) | "Quanto tempo você perde em code review?" | "🔥 E se você pudesse cortar 47% do tempo de code review?" | ✅ Recomendada |
| C (Contrária) | "Code review manual é perda de tempo" | "🔥 Pare de fazer code review manual. Sério." | — |

**Justificativa:** Variação B combina dado concreto com envolvimento direto
do leitor, gerando maior taxa de swipe por criar curiosidade pessoal.

### Hashtags Otimizadas

**Removidas:** #coding (muito genérica), #futurotrabalho (baixa relevância)
**Adicionadas:** #iaparadevs (nicho qualificado), #ferramentasdev (médio volume)

**Bloco final:**
#inteligenciaartificial #tecnologia #programacao #ia #google
#devbrasil #techbrasil #codereview #python #javascript
#iaparadevs #ferramentasdev #produtividadedev #automacaotech
#aprendizado #carreiratech

### CTA Refinado

**Antes:** "Qual tarefa repetitiva você mais queria automatizar?"
**Depois:** "Comenta a tarefa que mais te toma tempo no dia — vou
mostrar como automatizar as 3 mais votadas no próximo post."

**Motivo:** Adiciona incentivo concreto (próximo post) e reduz a
fricção da resposta (qualquer tarefa serve).

### Quality Pass

- [x] Ortografia e gramática revisadas
- [x] Tom consistente em todos os slides
- [x] Palavras por slide: mín 42, máx 78 ✅
- [x] Caption L1: 61 caracteres ✅
- [x] Fluxo narrativo coeso
- [x] Todos os claims com dados verificáveis
- [x] Nenhum anti-pattern detectado
```

## Quality Criteria

1. **Hooks testáveis** — As 3 variações de hook devem ser genuinamente diferentes em abordagem, não apenas reformulações da mesma frase.
2. **Hashtags verificadas** — Cada hashtag deve ser relevante para o tema e ter volume de posts compatível com a estratégia 5-5-5.
3. **CTA com incentivo** — O CTA final deve oferecer algo além de engajamento genérico: valor futuro, recurso adicional ou benefício social.
4. **Zero erros no quality pass** — O carrossel final não pode conter erros de ortografia, slides fora do range de palavras ou claims sem dados.

## Veto Conditions

1. **Hook sem teste** — Se apenas 1-2 variações foram geradas (em vez de 3), a task não está completa.
2. **Hashtags não categorizadas** — Se as hashtags não estão organizadas pela estratégia 5-5-5, o bloco precisa ser revisado.
3. **Quality pass incompleto** — Se qualquer item do checklist não foi verificado, a task não pode ser marcada como concluída.
