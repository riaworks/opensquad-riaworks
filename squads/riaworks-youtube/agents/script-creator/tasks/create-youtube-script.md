---
task: "Create YouTube Script"
order: 2
input: |
  - selected_angle: Ângulo escolhido pelo usuário
  - selected_tone: Tom de voz escolhido
  - research_data: Dados da pesquisa original
output: |
  - youtube_script: Script completo no formato youtube-script
---

# Create YouTube Script

Cria um roteiro completo de vídeo YouTube a partir do ângulo selecionado, otimizado para retenção e CTR.

## Process

1. Ler ângulo selecionado e tom de voz escolhido
2. Desenvolver thumbnail concept (3-4 palavras, expressão facial, cores)
3. Refinar título final: 50-70 chars, keyword nos primeiros 40, curiosity gap + benefício
4. Escrever hook (0-30s): abrir loop de curiosidade, estabelecer stakes, teaser do payoff
5. Escrever setup (30s-1:30): contexto + promessa específica do vídeo
6. Criar 3-5 seções do corpo:
   - Cada seção começa com mini-hook
   - Demonstração/evidência prática em cada seção
   - Transição com curiosidade para próxima seção
   - Pattern interrupt marcado a cada 45-90 segundos
7. Posicionar payoff no ponto 60-70% do vídeo
8. Escrever summary (últimos 1-2 min): recap 3 bullets + CTA contextualizado
9. Compor descrição SEO: Preview (160 chars) + timestamps + links + tags

## Output Format

Seguir o formato do best-practice youtube-script:
=== TÍTULO === / === THUMBNAIL CONCEPT === / === HOOK === / === INTRO === / === BODY === / === CLIMAX === / === SUMMARY === / === CTA + END SCREEN === / === DESCRIPTION === / === TAGS ===

## Output Example

```
=== TÍTULO ===
Claude 4 Mudou Tudo — Testei com Código Real e o Resultado É Assustador

=== THUMBNAIL CONCEPT ===
Visual: Rosto com expressão de choque olhando para tela de código
Text overlay: "MUDOU TUDO" (amarelo bold sobre fundo escuro)
Cores: Fundo preto/roxo, texto amarelo neon, logo Claude no canto
Composição: Face 60% do frame à direita, texto à esquerda

=== HOOK (0-30s) ===
[Script]: "A Anthropic acabou de lançar o Claude 4. E depois de testar 48 horas seguidas, posso dizer: o jogo mudou. Não é atualização incremental. É um salto. E vou mostrar uma capacidade que nenhum outro modelo tem."
[Visual cues]: Screen recording do Claude 4 gerando código, resultado aparecendo em real-time
[Pattern interrupt]: Zoom rápido no resultado + sound effect

=== INTRO (30s-1min) ===
[Script]: "Sou Riaworks, 20 anos em sistemas, e nos últimos 2 anos testo cada modelo de IA que aparece. O Claude 4 é diferente. Vou mostrar 3 testes com código real."
[Visual cues]: B-roll do setup, logos dos concorrentes

=== BODY ===
Section 1: O Que Mudou (Timestamp: ~1:00-4:00)
[Script]: "Três mudanças fundamentais..." | [Pattern interrupts]: Comparativo visual lado a lado | [Key point]: Raciocínio 3x mais longo

Section 2: Teste Real (Timestamp: ~4:00-7:30)
[Script]: "Benchmark é papel. Vamos ao teste real com 47 endpoints..." | [Pattern interrupts]: Screen recording + contador | [Key point]: 12 min vs 4 horas

Section 3: Onde Falha (Timestamp: ~7:30-10:00)
[Script]: "Nem tudo são flores. A maioria dos reviews não é honesta..." | [Pattern interrupts]: Tela com erro | [Key point]: Contexto longo = alucinação

=== CLIMAX (at ~70%) ===
[Script]: "A parte que eu não esperava. Uma capacidade que nenhum review mencionou..." | [Visual cues]: Demo ao vivo

=== SUMMARY (last 1-2 min) ===
"Resumindo: salto real em raciocínio, código prático, e feature X. Precisa melhorar em contextos extensos."

=== CTA + END SCREEN (last 20s) ===
"Se quer ver como integrei no meu workflow, esse vídeo aqui é o próximo passo." | [End screen]: Subscribe + próximo vídeo

=== DESCRIPTION ===
Claude 4 testado por 48h com código real. 3 testes práticos e uma capacidade que ninguém falou.
⏱️ 0:00 Hook | 1:00 Mudanças | 4:00 Teste real | 7:30 Falhas | 9:00 Feature surpresa | 11:00 Veredicto

=== TAGS ===
claude 4, anthropic, ia para programadores, benchmark ia 2026, teste ia, claude code
```

## Quality Criteria

- [ ] Título 50-70 chars com keyword front-loaded
- [ ] Thumbnail concept antes do roteiro
- [ ] Hook sem saudação, cria curiosity gap em 30s
- [ ] 3-5 seções com mini-hooks e pattern interrupts
- [ ] Pelo menos 1 demonstração prática marcada
- [ ] Payoff nos últimos 30% do vídeo
- [ ] CTA contextualizado (não genérico)
- [ ] Descrição com timestamps e keywords
- [ ] Duração estimada 8-15 minutos
- [ ] Acentuação pt-BR correta

## Veto Conditions

Reject and redo if ANY are true:
1. Hook com saudação ("Olá pessoal")
2. Título >100 chars ou todo CAPS
3. Sem thumbnail concept
4. Payoff nos primeiros 50% do vídeo
5. Zero demonstração prática
6. Acentuação incorreta
