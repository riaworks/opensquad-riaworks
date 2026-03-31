---
task: "Generate Feedback"
order: 2
input: |
  - scores: Tabela de scores do task anterior
output: |
  - review: Review completo com veredito, feedback, e sugestões
---

# Generate Feedback

Compila os scores em um review estruturado com veredito, feedback acionável, e sugestões de melhoria.

## Process

1. Ler tabela de scores do task anterior
2. Aplicar regras de decisão:
   - Overall ≥ 7/10, nenhum critério <4/10 → APPROVE
   - Overall ≥ 7/10, não-crítico entre 4-6/10 → CONDITIONAL APPROVE
   - Overall < 7/10 → REJECT
   - Hook <6/10 → REJECT (hard trigger)
   - Título <5/10 → REJECT (hard trigger)
   - Anti-pattern FAIL → REJECT (hard trigger)
3. Para cada score <10: formular feedback acionável com:
   - O que está errado (diagnóstico)
   - Onde está (localização exata)
   - Como corrigir (sugestão específica)
4. Classificar feedback como blocking (obrigatório) ou non-blocking (sugestão)
5. Listar strengths (mínimo 1, mesmo em REJECT)
6. Compilar review no formato padronizado
7. Documentar número da revisão

## Output Format

```markdown
==============================
 REVIEW VERDICT: {APPROVE/REJECT/CONDITIONAL APPROVE}
==============================

Content: "{título}"
Type: YouTube Script + 2 Shorts
Review Date: {YYYY-MM-DD}
Revision: {N} of 3

SCORING TABLE — SCRIPT
| Critério | Score | Resumo |
|----------|-------|--------|
...
OVERALL: X/10

SCORING TABLE — SHORTS
| Critério | Score | Resumo |
|----------|-------|--------|
...
OVERALL: X/10

DETAILED FEEDBACK
### Strengths
### Required Changes (blocking)
### Suggestions (non-blocking)
### Anti-Pattern Check
```

## Output Example

```markdown
==============================
 REVIEW VERDICT: CONDITIONAL APPROVE
==============================

Content: "Claude 4 Mudou Tudo — Testei e o Resultado É Assustador"
Type: YouTube Script + 2 Shorts
Review Date: 2026-03-26
Revision: 1 of 3

SCORING TABLE — SCRIPT
| Critério | Score | Resumo |
|----------|-------|--------|
| Hook | 9/10 | Abre com afirmação forte, sem saudação, teaser do resultado |
| Título | 7/10 | Bom gap mas 78 chars — será truncado |
| Estrutura | 8/10 | 3 seções com mini-hooks, pattern interrupts marcados |
| Conteúdo | 9/10 | Demonstração prática com métricas reais |
| Tom | 8/10 | Técnico e direto, seção 2 levemente formal |
| CTA | 7/10 | Contextualizado mas poderia ser mais específico |
| Thumbnail | 7/10 | Descrito mas falta emoção facial |
OVERALL: 8.0/10

SCORING TABLE — SHORTS
| Critério | Score | Resumo |
|----------|-------|--------|
| Hook | 9/10 | Ambas variantes têm hooks fortes e visuais |
| Densidade | 8/10 | 1 takeaway por Short, sem filler |
| Loop | 8/10 | Loop A natural, Loop B criativo |
| Acessibilidade | 9/10 | Text overlays completos, #Shorts presente |
| Tom | 8/10 | Consistente com canal |
OVERALL: 8.5/10

### Strengths
- Hook excepcional — tensão imediata sem saudação
- Dados concretos e verificáveis ao longo do script
- Shorts variante B com loop numérico criativo

### Required Changes (blocking)
1. **Título**: Reduzir para ≤70 chars → "Claude 4 Mudou Tudo — Testei e É Assustador" (51 chars)

### Suggestions (non-blocking)
1. Seção 2: linguagem mais conversacional ("demonstrou capacidades" → "mostrou que consegue")
2. Thumbnail: adicionar expressão facial (surpresa/choque)
3. CTA: especificar exatamente qual vídeo recomendar no end screen

### Anti-Pattern Check
- [x] Sem saudação no hook ✅
- [x] Título ≤100 chars ✅
- [x] Thumbnail definido ✅
- [x] Payoff nos últimos 30% ✅
- [x] Demonstração prática presente ✅
- [x] Acentuação pt-BR correta ✅
```

## Quality Criteria

- [ ] Veredito coerente com scores e regras de decisão
- [ ] Cada mudança blocking tem diagnóstico + localização + sugestão
- [ ] Strengths listados (mínimo 1)
- [ ] Blocking e non-blocking claramente separados
- [ ] Anti-pattern check completo
- [ ] Número da revisão documentado

## Veto Conditions

Reject and redo if ANY are true:
1. Veredito contradiz os scores (ex: APPROVE com critério <4)
2. Mudança blocking sem sugestão de correção
3. Zero strengths mencionados
