---
execution: inline
agent: reviewer
inputFile: squads/riaworks-youtube/output/youtube-script.md
outputFile: squads/riaworks-youtube/output/review.md
---

# Step 09: Revisão de Qualidade

## Context Loading

Load these files before executing:
- `squads/riaworks-youtube/output/youtube-script.md` — Script do vídeo para revisão
- `squads/riaworks-youtube/output/youtube-shorts.md` — Shorts para revisão
- `squads/riaworks-youtube/pipeline/data/quality-criteria.md` — Critérios de avaliação
- `squads/riaworks-youtube/pipeline/data/anti-patterns.md` — Padrões proibidos
- `squads/riaworks-youtube/pipeline/data/output-examples.md` — Referência de qualidade
- `squads/riaworks-youtube/pipeline/data/domain-framework.md` — Framework operacional
- `_opensquad/_memory/company.md` — Contexto da empresa

## Instructions

### Process
1. Ler COMPLETAMENTE o script e os shorts antes de avaliar
2. Verificar cada anti-pattern: se qualquer um for encontrado, é rejeição automática
3. Avaliar cada critério de quality-criteria.md individualmente (1-10)
4. Para cada nota <10, identificar o trecho exato e sugerir correção específica
5. Calcular score geral como média ponderada
6. Aplicar regras de decisão: APPROVE (≥7, nenhum <4), REJECT (<7 ou qualquer <4)
7. Se REJECT: listar mudanças obrigatórias com localização exata
8. Compilar review estruturado

## Output Format

```markdown
==============================
 REVIEW VERDICT: {APPROVE/REJECT/CONDITIONAL APPROVE}
==============================

Content: "{título do vídeo}"
Type: YouTube Script + 2 Shorts
Review Date: {YYYY-MM-DD}
Revision: {N} of 3

------------------------------
 SCORING TABLE — SCRIPT
------------------------------
| Critério | Score | Resumo |
|----------|-------|--------|
| Hook | X/10 | {justificativa} |
| Título | X/10 | {justificativa} |
| Estrutura e Retenção | X/10 | {justificativa} |
| Conteúdo e Valor | X/10 | {justificativa} |
| Tom e Voz | X/10 | {justificativa} |
| CTA e Encerramento | X/10 | {justificativa} |
| Thumbnail Concept | X/10 | {justificativa} |
| **OVERALL** | **X/10** | |

------------------------------
 SCORING TABLE — SHORTS
------------------------------
| Critério | Score | Resumo |
|----------|-------|--------|
| Hook Instantâneo | X/10 | {justificativa} |
| Densidade e Foco | X/10 | {justificativa} |
| Loop Design | X/10 | {justificativa} |
| Acessibilidade | X/10 | {justificativa} |
| Tom e Voz | X/10 | {justificativa} |
| **OVERALL** | **X/10** | |

------------------------------
 DETAILED FEEDBACK
------------------------------

### Strengths
- {ponto forte 1}
- {ponto forte 2}

### Required Changes (blocking)
1. {mudança obrigatória com localização exata e sugestão}
2. {mudança obrigatória}

### Suggestions (non-blocking)
1. {sugestão de melhoria}
2. {sugestão}

### Anti-Pattern Check
- [ ] Sem saudação no hook ✅/❌
- [ ] Título ≤100 chars ✅/❌
- [ ] Thumbnail definido ✅/❌
- [ ] Payoff nos últimos 30% ✅/❌
- [ ] Demonstração prática presente ✅/❌
- [ ] Acentuação pt-BR correta ✅/❌
```

## Output Example

```markdown
==============================
 REVIEW VERDICT: CONDITIONAL APPROVE
==============================

Content: "Claude 4 Mudou Tudo Que Sabíamos Sobre IA — Testei e o Resultado É Assustador"
Type: YouTube Script + 2 Shorts
Review Date: 2026-03-26
Revision: 1 of 3

------------------------------
 SCORING TABLE — SCRIPT
------------------------------
| Critério | Score | Resumo |
|----------|-------|--------|
| Hook | 9/10 | Abre com afirmação forte e teaser do resultado. Excelente. |
| Título | 8/10 | Bom curiosity gap, mas acima de 70 chars — pode ser truncado. |
| Estrutura e Retenção | 8/10 | 3 seções bem definidas com mini-hooks. Pattern interrupts marcados. |
| Conteúdo e Valor | 9/10 | Demonstração prática com métricas reais. Forte. |
| Tom e Voz | 8/10 | Técnico e direto, mas seção 2 fica levemente formal. |
| CTA e Encerramento | 7/10 | CTA contextualizado mas poderia ser mais específico. |
| Thumbnail Concept | 7/10 | Descrito mas falta emoção facial. |
| **OVERALL** | **8.0/10** | |

### Strengths
- Hook excepcional — cria tensão imediata sem saudação
- Dados concretos e verificáveis ao longo do script

### Required Changes (blocking)
1. **Título**: Reduzir para ≤70 chars. Sugestão: "Claude 4 Mudou Tudo — Testei e o Resultado É Assustador" (59 chars)

### Suggestions (non-blocking)
1. Seção 2: trocar "O modelo demonstrou capacidades superiores" por linguagem mais conversacional
2. Thumbnail: adicionar descrição de expressão facial (surpresa/choque)
```

## Veto Conditions

Reject and redo if ANY are true:
1. Score atribuído sem justificativa escrita
2. Review não segue o formato padrão (tabela + feedback + anti-pattern check)
3. Feedback de rejeição não inclui sugestão de correção específica

## Quality Criteria

- [ ] Cada critério tem score + justificativa
- [ ] Anti-patterns verificados explicitamente
- [ ] Mudanças obrigatórias têm localização exata e sugestão
- [ ] Strengths mencionados (mesmo em REJECT)
- [ ] Veredito coerente com scores
