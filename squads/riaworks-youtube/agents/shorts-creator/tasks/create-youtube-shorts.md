---
task: "Create YouTube Shorts"
order: 1
input: |
  - selected_angle: Ângulo escolhido pelo usuário
  - selected_tone: Tom de voz escolhido
  - research_data: Dados da pesquisa
output: |
  - shorts_drafts: 2 variantes de YouTube Shorts completas
---

# Create YouTube Shorts

Cria 2 variantes de YouTube Shorts a partir do ângulo selecionado, otimizadas para completion rate e loop replays.

## Process

1. Ler ângulo selecionado, tom de voz, e dados da pesquisa
2. Identificar o insight mais impactante da notícia para condensar em 30-45 segundos
3. Para cada variante:
   a. Criar hook instantâneo (0-2s): text overlay bold + frase provocadora
   b. Desenvolver delivery (2-40s): shot-by-shot com cortes a cada 3-5s
   c. Escrever script falado: ritmo rápido, zero filler, 1 takeaway
   d. Marcar text overlays em cada momento-chave
   e. Criar punchline/loop: final que conecta visual ou narrativamente ao início
4. Variante A e B devem ter abordagens criativas DISTINTAS:
   - Diferente hook (dado vs pergunta)
   - Diferente estrutura (linear vs reveal)
   - Diferente loop mechanism
5. Escrever título, descrição com #Shorts, loop note, e audio note

## Output Format

```
=== SHORT VARIANTE A ===

HOOK (0-2s):
[Visual]: descrição do que aparece na tela
[Audio]: frase falada ou music cue
[Text Overlay]: texto bold na tela (máx 8 palavras)

DELIVERY (2-Xs):
[Visual]: shot-by-shot (Cut 1, Cut 2, etc.)
[Script]: roteiro falado completo
[Text Overlays]: textos que aparecem em cada momento

PUNCHLINE/LOOP (últimos 5-10s):
[Visual]: frame final
[Script]: frase de fechamento
[Text Overlay]: texto final

TITLE: título do Short
DESCRIPTION: descrição + #Shorts + hashtags
LOOP NOTE: como o final conecta ao início
AUDIO NOTE: direção de áudio

=== SHORT VARIANTE B ===
[mesma estrutura, abordagem diferente]
```

## Output Example

```
=== SHORT VARIANTE A ===

HOOK (0-2s):
[Visual]: Tela de código com IA gerando em velocidade acelerada
[Audio]: "A IA acabou de fazer em 3 minutos o que levava 3 dias."
[Text Overlay]: "3 MINUTOS vs 3 DIAS" (branco bold, fundo vermelho)

DELIVERY (2-35s):
[Visual]: Cut 1 (2-8s) — Screenshot do prompt
[Script]: "Peguei uma tarefa real: mapear 200 endpoints de uma API legada."
[Text Overlays]: "200 ENDPOINTS"

[Visual]: Cut 2 (8-18s) — Screen recording acelerado
[Script]: "Claude Code mapeou todos, achou 12 deprecados, gerou docs Swagger."
[Text Overlays]: "✅ 200 mapeados" → "⚠️ 12 deprecados" → "📄 Swagger"

[Visual]: Cut 3 (18-28s) — Comparativo lado a lado
[Script]: "Manual: 3 dias, 4 erros. IA: 3 minutos, zero erros."
[Text Overlays]: "IA: 0 erros ✅" vs "Manual: 4 erros ❌"

[Visual]: Cut 4 (28-35s) — Webcam close-up
[Script]: "Quem usa IA vai substituir quem não usa."

PUNCHLINE/LOOP (35-40s):
[Visual]: Volta para tela de código (mesma cena do hook)
[Script]: "E isso foi só um teste simples..."
[Text Overlay]: "SÓ UM TESTE..."

TITLE: IA fez em 3 minutos o que levava 3 dias #programação
DESCRIPTION: Testei Claude Code numa tarefa real de API. #Shorts #IA #Programação #ClaudeCode #Dev
LOOP NOTE: "E isso foi só um teste..." volta para a tela de IA gerando código = loop visual
AUDIO NOTE: Áudio original narrado, ritmo acelerado, whoosh nos cortes

=== SHORT VARIANTE B ===

HOOK (0-2s):
[Visual]: Contador de endpoints em fast-forward (0 → 200)
[Audio]: "200 endpoints. 3 minutos. Zero erros."
[Text Overlay]: "200 → 3min → 0 erros" (verde neon, fundo escuro)

DELIVERY (2-30s):
[Visual]: Cut 1 (2-10s) — Split screen: lado esquerdo trabalho manual, lado direito IA
[Script]: "Do lado esquerdo: eu fazendo manual. 3 dias. Do lado direito: Claude Code. 3 minutos."
[Text Overlays]: "MANUAL: 3 DIAS" / "IA: 3 MIN"

[Visual]: Cut 2 (10-20s) — Zoom no output da IA
[Script]: "Documentação Swagger completa. 12 endpoints deprecados identificados. Que eu nem sabia que existiam."
[Text Overlays]: "SWAGGER ✅" → "12 DEPRECADOS 🔍"

[Visual]: Cut 3 (20-30s) — Webcam com expressão séria
[Script]: "A pergunta não é se a IA substitui. É quanto tempo você tá perdendo sem ela."

PUNCHLINE/LOOP (30-35s):
[Visual]: Contador reinicia (200 → 0 → começa de novo)
[Script]: "200 endpoints..."
[Text Overlay]: "DE NOVO?"

TITLE: 200 endpoints em 3 minutos com IA #dev
DESCRIPTION: Manual vs IA — o resultado fala por si. #Shorts #IA #Dev #ClaudeCode #API
LOOP NOTE: Contador reiniciando conecta ao contador do hook = loop numérico
AUDIO NOTE: Voz firme e confiante, sem música, sound effect de countdown
```

## Quality Criteria

- [ ] 2 variantes com abordagens criativas distintas
- [ ] Hook em 2 segundos com text overlay bold
- [ ] 1 takeaway por Short
- [ ] Text overlays ao longo de todo o Short
- [ ] Loop design documentado e funcional
- [ ] 15-45 segundos estimados
- [ ] #Shorts e 3-5 hashtags incluídos
- [ ] Acentuação pt-BR correta

## Veto Conditions

Reject and redo if ANY are true:
1. Apenas 1 variante criada (precisa de 2)
2. Variantes A e B usam o mesmo hook approach
3. Short estimado acima de 60 segundos
4. Sem text overlays marcados
5. Sem loop note documentado
