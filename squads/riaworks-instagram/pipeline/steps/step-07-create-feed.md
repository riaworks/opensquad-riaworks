---
execution: subagent
agent: instagram-feed-creator
format: instagram-feed
inputFile: squads/riaworks-instagram/output/angles.md
outputFile: squads/riaworks-instagram/output/instagram-feed-content.md
model_tier: powerful
---

# Step 07: Criar Conteudo Instagram Feed

## Context Loading

Load these files before executing:
- `squads/riaworks-instagram/output/angles.md` — Angulo selecionado pelo usuario
- `squads/riaworks-instagram/output/research-results.md` — Pesquisa completa com dados
- `squads/riaworks-instagram/pipeline/data/tone-of-voice.md` — Tom de voz (o usuario ja selecionou; use o tom escolhido)
- `squads/riaworks-instagram/pipeline/data/output-examples.md` — Exemplos de referencia
- `squads/riaworks-instagram/pipeline/data/quality-criteria.md` — Criterios de qualidade
- `squads/riaworks-instagram/pipeline/data/anti-patterns.md` — Erros a evitar
- `_opensquad/_memory/company.md` — Contexto da empresa

## Instructions

### Process
1. Ler o angulo selecionado e a pesquisa completa. Identificar dados-chave, metricas e fontes.
2. Escolher o formato de carrossel mais adequado ao angulo (Editorial, Listicle, Tutorial, Mito vs Realidade, Storytelling, Problema-Solucao).
3. Escrever o hook do cover slide (max 20 palavras, provocativo, especifico a esta noticia).
4. Desenvolver 6-8 slides de conteudo com hierarquia headline + supporting text (40-80 palavras cada).
5. Criar slide de CTA com acao especifica (comment keyword, save, share).
6. Escrever caption completa: hook nos primeiros 125 chars → body com valor → CTA → pergunta.
7. Criar otimizacao: testar 2 variacoes do hook (A/B), otimizar hashtags, refinar calls-to-action.
8. Compilar versao final com todos os elementos.

## Output Format

```
=== FORMAT ===
[Nome do formato escolhido]

=== SLIDES ===
Slide 1 (Cover):
  Title: [max 20 palavras]
  Photo: [descricao da foto]
  Background: [cor]

Slide 2 ([Papel]):
  Headline: [texto bold principal]
  Supporting text: [texto de apoio com dados]
  Accent keywords: [palavras para destacar]
  Background: [light/dark/accent]

[...continuar ate o ultimo slide]

Slide N (CTA):
  Photo: [imagem final]
  Source: [fonte do conteudo]
  CTA: [acao especifica]

=== CAPTION ===
[Hook nos primeiros 125 chars]

[Body com valor]

[Pergunta para engajamento]

=== HASHTAGS ===
[5-15 hashtags mix nicho + broad]

=== HOOK VARIATIONS (A/B) ===
Hook A: [versao original]
Hook B: [variacao alternativa]
```

## Output Example

[Use o Exemplo 1 do arquivo output-examples.md como referencia de qualidade e profundidade. O output deve ter o mesmo nivel de detalhe e especificidade.]

## Veto Conditions

Reject and redo if ANY are true:
1. Algum slide tem menos de 40 palavras (headline + supporting text)
2. Hook do cover nao menciona dados especificos ou nao para o scroll
3. Caption nao tem hook nos primeiros 125 caracteres
4. Menos de 6 slides de conteudo (excluindo cover e CTA)

## Quality Criteria

- [ ] Formato de carrossel adequado ao angulo escolhido
- [ ] Cover slide com hook bold e provocativo (max 20 palavras)
- [ ] Cada slide entre 40-80 palavras com hierarquia headline + supporting
- [ ] Dados quantitativos da pesquisa usados nos slides
- [ ] Caption com hook efetivo nos primeiros 125 chars
- [ ] CTA especifico e acionavel no ultimo slide
- [ ] 5-15 hashtags relevantes para tech/IA brasileiro
- [ ] Tom de voz consistente com a escolha do usuario
- [ ] 2 variacoes de hook (A/B testing)
- [ ] Fontes citadas no conteudo
