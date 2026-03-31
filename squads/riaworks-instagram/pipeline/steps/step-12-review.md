---
execution: inline
agent: reviewer
inputFile: squads/riaworks-instagram/output/instagram-feed-content.md
outputFile: squads/riaworks-instagram/output/review-report.md
on_reject: create-feed
---

# Step 12: Revisao de Qualidade

## Context Loading

Load these files before executing:
- `squads/riaworks-instagram/output/instagram-feed-content.md` — Conteudo do carrossel
- `squads/riaworks-instagram/output/instagram-reels-content.md` — Roteiro do reel
- `squads/riaworks-instagram/output/research-results.md` — Pesquisa original (para verificar precisao)
- `squads/riaworks-instagram/pipeline/data/quality-criteria.md` — Criterios de avaliacao
- `squads/riaworks-instagram/pipeline/data/anti-patterns.md` — Erros a verificar
- `_opensquad/_memory/company.md` — Contexto da marca

## Instructions

### Process
1. Ler TODOS os arquivos de contexto antes de iniciar a avaliacao.
2. Avaliar o conteudo do carrossel: hook, slides, caption, hashtags, CTA — cada criterio de 1-10 com justificativa.
3. Avaliar o roteiro do reel: hook, duracao, roteiro, legendas, CTA — cada criterio de 1-10 com justificativa.
4. Verificar precisao tecnica: todos os dados, benchmarks e claims citados no conteudo estao corretos segundo a pesquisa?
5. Verificar tom de voz: esta consistente com a escolha do usuario?
6. Verificar anti-padroes: algum erro da lista de anti-patterns esta presente?
7. Compilar relatorio com verdict (APPROVE/REJECT), scoring table, feedback detalhado, e path to approval se rejeitado.

## Output Format

```
==============================
 REVIEW VERDICT: [APPROVE/REJECT]
==============================

Content: Canal Riaworks Instagram — [tema]
Review Date: [data]
Revision: [N] of 3

------------------------------
 CARROSSEL — SCORING TABLE
------------------------------
| Criterio | Score | Summary |
|----------|-------|---------|
| ... | .../10 | ... |

OVERALL: .../10

------------------------------
 REEL — SCORING TABLE
------------------------------
| Criterio | Score | Summary |
|----------|-------|---------|
| ... | .../10 | ... |

OVERALL: .../10

DETAILED FEEDBACK:
[Strengths, required changes, suggestions]

PATH TO APPROVAL:
[Se rejeitado: lista de mudancas obrigatorias]
```

## Output Example

[Seguir o formato dos exemplos da best-practice review.md. Cada score com justificativa. Required changes com localizacao especifica. Strengths reconhecidos.]

## Veto Conditions

Reject and redo if ANY are true:
1. Algum score aparece sem justificativa escrita
2. Verdict contradiz os scores (ex: APPROVE com score abaixo de 4)

## Quality Criteria

- [ ] Todos os criterios avaliados e pontuados
- [ ] Cada score tem justificativa de pelo menos 1 frase
- [ ] Feedback inclui localizacao especifica (slide X, paragrafo Y)
- [ ] Required changes separados de suggestions
- [ ] Strengths reconhecidos mesmo em REJECT
- [ ] Precisao tecnica verificada contra pesquisa original
