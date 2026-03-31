---
task: "Score Content"
order: 1
input: |
  - youtube_script: Script do vídeo para avaliação
  - youtube_shorts: 2 variantes de Shorts para avaliação
  - quality_criteria: Critérios de qualidade do squad
  - anti_patterns: Padrões proibidos
output: |
  - scores: Tabela de scores com justificativas para script e shorts
---

# Score Content

Avalia o script YouTube e os Shorts contra os critérios de qualidade definidos, produzindo tabelas de scoring com justificativas.

## Process

1. Ler COMPLETAMENTE o script e os Shorts antes de avaliar (nunca skimmar)
2. Verificar cada anti-pattern do anti-patterns.md:
   - Hook com saudação? → REJECT automático
   - Título >100 chars? → REJECT automático
   - Sem thumbnail concept? → REJECT automático
   - Payoff nos primeiros 50%? → REJECT automático
   - Zero demonstração prática? → REJECT automático
   - Acentuação incorreta? → REJECT automático
3. Avaliar SCRIPT contra 7 critérios do quality-criteria.md (1-10 cada):
   - Hook (peso 25%)
   - Título (peso 20%)
   - Estrutura e Retenção (peso 20%)
   - Conteúdo e Valor (peso 15%)
   - Tom e Voz (peso 10%)
   - CTA e Encerramento (peso 5%)
   - Thumbnail Concept (peso 5%)
4. Avaliar SHORTS contra 5 critérios (1-10 cada):
   - Hook Instantâneo (peso 30%)
   - Densidade e Foco (peso 25%)
   - Loop Design (peso 20%)
   - Acessibilidade (peso 15%)
   - Tom e Voz (peso 10%)
5. Para cada score: identificar trecho exato que justifica a nota
6. Calcular overall como média ponderada

## Output Format

```yaml
script_scores:
  - criterion: "Hook"
    weight: 25
    score: X
    justification: "texto com referência ao trecho exato"
  - criterion: "Título"
    weight: 20
    score: X
    justification: "..."
  overall: X.X

shorts_scores:
  - criterion: "Hook Instantâneo"
    weight: 30
    score: X
    justification: "..."
  overall: X.X

anti_pattern_check:
  - pattern: "Hook com saudação"
    status: "PASS" | "FAIL"
  - pattern: "Título >100 chars"
    status: "PASS" | "FAIL"
```

## Output Example

```yaml
script_scores:
  - criterion: "Hook"
    weight: 25
    score: 9
    justification: "Hook abre com afirmação provocativa ('A Anthropic acabou de lançar...') sem saudação. Cria curiosity gap claro com teaser ('capacidade que nenhum outro modelo tem'). Forte."
  - criterion: "Título"
    weight: 20
    score: 7
    justification: "Bom curiosity gap mas 78 chars — excede limite de 70, será truncado em mobile. Keyword 'Claude 4' nos primeiros chars é correto."
  overall: 8.1

shorts_scores:
  - criterion: "Hook Instantâneo"
    weight: 30
    score: 9
    justification: "Variante A: '3 MINUTOS vs 3 DIAS' como text overlay é forte e instiga scroll-stop. Variante B: contador numérico é criativo e visual."
  overall: 8.5

anti_pattern_check:
  - pattern: "Hook com saudação"
    status: "PASS"
  - pattern: "Título >100 chars"
    status: "PASS"
  - pattern: "Thumbnail concept"
    status: "PASS"
  - pattern: "Payoff timing"
    status: "PASS"
  - pattern: "Demonstração prática"
    status: "PASS"
  - pattern: "Acentuação pt-BR"
    status: "PASS"
```

## Quality Criteria

- [ ] Todos os critérios avaliados com score e justificativa
- [ ] Anti-patterns verificados explicitamente
- [ ] Scores usam trechos exatos como evidência
- [ ] Overall calculado como média ponderada correta
- [ ] Script e Shorts avaliados separadamente

## Veto Conditions

Reject and redo if ANY are true:
1. Qualquer critério sem justificativa escrita
2. Anti-pattern check incompleto
3. Score inconsistente com justificativa
