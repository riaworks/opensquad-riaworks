---
execution: subagent
agent: shorts-creator
format: youtube-shorts
inputFile: squads/riaworks-youtube/output/angles.md
outputFile: squads/riaworks-youtube/output/youtube-shorts.md
model_tier: powerful
---

# Step 07: Criação de YouTube Shorts

## Context Loading

Load these files before executing:
- `squads/riaworks-youtube/output/angles.md` — Ângulo selecionado pelo usuário
- `squads/riaworks-youtube/output/research-results.md` — Dados da pesquisa
- `squads/riaworks-youtube/pipeline/data/domain-framework.md` — Estrutura de Shorts
- `squads/riaworks-youtube/pipeline/data/output-examples.md` — Exemplo de Short completo
- `squads/riaworks-youtube/pipeline/data/anti-patterns.md` — Padrões a evitar
- `squads/riaworks-youtube/pipeline/data/tone-of-voice.md` — Tom de voz selecionado
- `_opensquad/_memory/company.md` — Contexto da empresa

## Instructions

### Process
1. Ler o ângulo selecionado e o tom de voz escolhido
2. Extrair o insight mais impactante da notícia para condensar em 30-45 segundos
3. Criar hook instantâneo (0-2s) com text overlay bold
4. Desenvolver delivery (2-40s) com 1 ponto, 1 takeaway, zero fluff
5. Criar punchline/loop (últimos 5-10s) que conecta de volta ao hook
6. Escrever título conciso e curiosity-driven
7. Compor descrição com #Shorts e 3-5 hashtags
8. Documentar loop note e audio note
9. Criar 2 variantes de Shorts (mesmo tema, abordagens diferentes)

## Output Format

Seguir EXATAMENTE o formato do best-practice youtube-shorts.md, MAS criar 2 variantes:

```
=== SHORT VARIANTE A ===

HOOK (0-2s): [Visual + Audio + Text Overlay]
DELIVERY (2-40s): [Visual + Script + Text Overlays]
PUNCHLINE/LOOP (últimos 5-10s): [Visual + Script + Text Overlay]

TITLE: [título]
DESCRIPTION: [descrição com #Shorts + hashtags]
LOOP NOTE: [como o final conecta ao início]
AUDIO NOTE: [direção de áudio]

=== SHORT VARIANTE B ===
[mesma estrutura, abordagem diferente]
```

## Output Example

```
=== SHORT VARIANTE A ===

HOOK (0-2s):
[Visual]: Tela de código com IA gerando em velocidade acelerada
[Audio]: "A IA fez em 3 minutos o que levava 3 dias."
[Text Overlay]: "3 MIN vs 3 DIAS" (branco bold, fundo vermelho)

DELIVERY (2-35s):
[Visual]: Cut 1 (2-8s) — Screenshot do prompt
[Script]: "Tarefa real: mapear 200 endpoints de uma API legada."
[Text Overlays]: "200 ENDPOINTS"

[Visual]: Cut 2 (8-18s) — Screen recording acelerado
[Script]: "Claude Code mapeou todos, achou 12 deprecados, gerou Swagger."
[Text Overlays]: "✅ 200" → "⚠️ 12 deprecados" → "📄 Swagger"

[Visual]: Cut 3 (18-28s) — Comparativo lado a lado
[Script]: "Manual: 3 dias, 4 erros. IA: 3 minutos, zero erros."
[Text Overlays]: "IA: 0 erros ✅" vs "Manual: 4 erros ❌"

PUNCHLINE/LOOP (35-40s):
[Visual]: Volta para tela de código (mesma cena do hook)
[Script]: "E isso foi só um teste simples..."
[Text Overlay]: "SÓ UM TESTE..."

TITLE: IA fez em 3 minutos o que levava 3 dias #programação
DESCRIPTION: Teste real com Claude Code. #Shorts #IA #Programação #ClaudeCode
LOOP NOTE: Final volta à mesma cena visual do hook = loop automático
AUDIO NOTE: Narração acelerada, whoosh nos cortes

=== SHORT VARIANTE B ===

HOOK (0-2s):
[Visual]: Contador numérico acelerando: 0 → 200
[Audio]: "200 endpoints. 3 minutos. Zero erros."
[Text Overlay]: "200 → 3min → 0 erros" (verde neon)

DELIVERY (2-28s):
[Visual]: Split-screen Manual vs IA lado a lado
[Script]: "Esquerda: eu fazendo manual, 3 dias. Direita: Claude Code, 3 minutos."
[Text Overlays]: "MANUAL: 3 DIAS" / "IA: 3 MIN"

PUNCHLINE/LOOP (28-33s):
[Visual]: Contador reinicia de 200 → 0
[Script]: "200 endpoints..."
[Text Overlay]: "DE NOVO?"

TITLE: 200 endpoints em 3 minutos com IA #dev
DESCRIPTION: Manual vs IA — resultado fala por si. #Shorts #IA #Dev #API
LOOP NOTE: Contador reiniciando conecta ao hook = loop numérico
AUDIO NOTE: Voz firme, sem música, countdown effect
```

## Veto Conditions

Reject and redo if ANY are true:
1. Short acima de 60 segundos estimados
2. Mais de 1 takeaway por Short (deve ser 1 ponto, 1 insight)
3. Sem text overlays ao longo do Short
4. Sem design de loop (final não conecta ao início)
5. Faltando #Shorts no título ou descrição
6. Acentuação pt-BR incorreta

## Quality Criteria

- [ ] Hook nos primeiros 2 segundos com text overlay bold
- [ ] Duração estimada 15-45 segundos
- [ ] 1 tópico, 1 takeaway por Short
- [ ] Text overlays presentes ao longo de todo o Short
- [ ] Loop design documentado
- [ ] #Shorts incluído + 3-5 hashtags
- [ ] 2 variantes distintas criadas
- [ ] Acentuação pt-BR correta
