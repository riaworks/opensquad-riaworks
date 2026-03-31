---
execution: subagent
agent: instagram-reels-creator
format: instagram-reels
inputFile: squads/riaworks-instagram/output/angles.md
outputFile: squads/riaworks-instagram/output/instagram-reels-content.md
model_tier: powerful
---

# Step 08: Criar Conteudo Instagram Reels

## Context Loading

Load these files before executing:
- `squads/riaworks-instagram/output/angles.md` — Angulo selecionado
- `squads/riaworks-instagram/output/research-results.md` — Pesquisa com dados
- `squads/riaworks-instagram/pipeline/data/tone-of-voice.md` — Tom de voz selecionado
- `squads/riaworks-instagram/pipeline/data/output-examples.md` — Exemplos de referencia
- `squads/riaworks-instagram/pipeline/data/quality-criteria.md` — Criterios de qualidade
- `squads/riaworks-instagram/pipeline/data/anti-patterns.md` — Erros a evitar
- `_opensquad/_memory/company.md` — Contexto da empresa

## Instructions

### Process
1. Ler o angulo selecionado e a pesquisa. Adaptar o angulo para formato video curto.
2. Escrever hook visual dos primeiros 2 segundos (text overlay + acao em tela).
3. Criar setup rapido (2-5s) que estabelece contexto.
4. Desenvolver delivery section com roteiro falado + text overlays + direcoes de corte a cada 3-5s.
5. Criar CTA final (3-5s) com acao especifica.
6. Projetar loop design: como o final conecta visualmente com o inicio.
7. Escrever caption com hook nos primeiros 125 chars.
8. Sugerir audio (trending sound ou direcao de audio original).
9. Otimizar: testar variacao de hook, refinar ritmo, garantir duracao 15-30s.

## Output Format

```
=== REEL SCRIPT ===

HOOK (0-2s):
[Visual]: [o que aparece na tela]
[Audio]: [som ou fala]
[Text Overlay]: [texto na tela — max 10 palavras]

SETUP (2-5s):
[Visual]: [cena]
[Script]: [fala — 1-2 frases]

DELIVERY (5-Xs):
[Visual]: [shot-by-shot com cortes]
[Script]: [roteiro completo]
[Text Overlays]: [pontos-chave na tela]

CTA (ultimos 3-5s):
[Visual]: [frame final]
[Script]: [fala — 1 pedido especifico]
[Text Overlay]: [CTA na tela]

LOOP DESIGN:
[Como o final conecta com o inicio]

=== CAPTION ===
[Hook 125 chars]
[Contexto]
[CTA]

=== HASHTAGS ===
[5-15 hashtags]

=== AUDIO NOTE ===
[Sugestao de audio]

=== DURATION ===
[Duracao estimada em segundos]
```

## Output Example

[Use o Exemplo 2 do arquivo output-examples.md como referencia de qualidade. O output deve ter o mesmo nivel de detalhe pratico.]

## Veto Conditions

Reject and redo if ANY are true:
1. Duracao estimada acima de 30 segundos
2. Nao ha text overlay no hook (primeiros 2 segundos)
3. Nao ha direcao de legendas/subtitulos
4. Hook nao e especifico a esta noticia/tema

## Quality Criteria

- [ ] Hook visual claro nos primeiros 2 segundos
- [ ] Duracao entre 15-30 segundos
- [ ] Cortes visuais a cada 3-5 segundos indicados
- [ ] Roteiro conversacional e energetico
- [ ] Loop design descrito
- [ ] CTA especifico e acionavel
- [ ] Caption com hook efetivo nos primeiros 125 chars
- [ ] Audio sugerido relevante ao conteudo
- [ ] Legendas/subtitulos mencionados
- [ ] Tom de voz consistente
