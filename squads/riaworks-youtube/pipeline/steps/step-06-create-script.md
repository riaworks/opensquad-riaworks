---
execution: subagent
agent: script-creator
format: youtube-script
inputFile: squads/riaworks-youtube/output/angles.md
outputFile: squads/riaworks-youtube/output/youtube-script.md
model_tier: powerful
---

# Step 06: Criação de Script YouTube

## Context Loading

Load these files before executing:
- `squads/riaworks-youtube/output/angles.md` — Ângulo selecionado pelo usuário
- `squads/riaworks-youtube/output/research-results.md` — Dados da pesquisa original
- `squads/riaworks-youtube/pipeline/data/domain-framework.md` — Estrutura de roteiro
- `squads/riaworks-youtube/pipeline/data/output-examples.md` — Exemplos de scripts completos
- `squads/riaworks-youtube/pipeline/data/anti-patterns.md` — Padrões a evitar
- `squads/riaworks-youtube/pipeline/data/tone-of-voice.md` — Tom de voz selecionado
- `squads/riaworks-youtube/pipeline/data/quality-criteria.md` — Critérios de qualidade
- `_opensquad/_memory/company.md` — Contexto da empresa

## Instructions

### Process
1. Ler o ângulo selecionado e o tom de voz escolhido pelo usuário
2. Desenvolver o thumbnail concept ANTES do roteiro
3. Criar título final otimizado (50-70 chars, keyword nos primeiros 40)
4. Escrever hook (0-30s) que abre loop de curiosidade
5. Desenvolver setup (30s-1:30) com contexto e promessa
6. Criar 3-5 seções do corpo com mini-hooks, demonstrações, e pattern interrupts marcados
7. Posicionar payoff nos últimos 30% do vídeo
8. Escrever CTA contextualizado + encerramento
9. Compor descrição SEO (PPP) com timestamps
10. Listar 5-10 tags relevantes
11. Otimizar: verificar duração (8-15 min), retenção hooks, acessibilidade
12. Self-review contra quality-criteria.md e anti-patterns.md

## Output Format

Seguir EXATAMENTE o formato definido no best-practice youtube-script.md:

```
=== TÍTULO ===
[50-70 chars, keyword nos primeiros 40, curiosity gap + benefício]

=== THUMBNAIL CONCEPT ===
[Visual, text overlay 3-4 palavras, cores, composição]

=== HOOK (0-30s) ===
[Script falado + visual cues]

=== INTRO (30s-1min) ===
[Contexto + promessa + visual cues]

=== BODY ===
Section 1-5: [Subheading + script + pattern interrupts + key points]

=== CLIMAX ===
[Momento de maior valor]

=== SUMMARY ===
[Recap + takeaways]

=== CTA + END SCREEN ===
[CTA contextualizado + elementos end screen]

=== DESCRIPTION ===
[PPP: Preview + Proof + Push + Timestamps + Links]

=== TAGS ===
[5-10 keywords]
```

## Output Example

```
=== TÍTULO ===
Testei o Claude 4 por 48h com Código Real — O Resultado Me Assustou

=== THUMBNAIL CONCEPT ===
Visual: Expressão de surpresa, tela de código ao fundo com highlights verdes
Text overlay: "48H DE TESTE" (amarelo, fonte bold)
Cores: Fundo escuro, texto amarelo neon, highlights verdes no código

=== HOOK (0-30s) ===
[Script]: "Em 48 horas testando o Claude 4, descobri algo que muda tudo para devs. E não é o que os reviews estão dizendo."
[Visual cues]: Time-lapse da tela com código sendo gerado | Zoom no resultado final

=== BODY ===
Section 1: Setup do Teste (~1:00-4:00)
[Script]: "Peguei meu projeto real de logística — 47 endpoints, código legado de 5 anos..."
[Pattern interrupts]: Screenshot da codebase, contador de endpoints, zoom na complexidade
[Key point]: Condições reais, não benchmark artificial

Section 2: Resultados (~4:00-8:00)
[Script]: "12 minutos. É isso. O Claude 4 refatorou em 12 minutos o que levaria 4 horas..."
[Pattern interrupts]: Split-screen antes/depois, gráfico de tempo, highlight das melhorias
[Key point]: 20x mais rápido com zero erros de compilação

=== DESCRIPTION ===
Testei Claude 4 por 48h com projeto real de logística (47 endpoints). Resultados surpreendentes.
⏱️ 0:00 Hook | 1:00 Setup | 4:00 Resultados | 8:00 Surpresa | 10:00 Veredicto

=== TAGS ===
claude 4, teste ia, programação com ia, anthropic, benchmark 2026, dev brasileiro
```

## Veto Conditions

Reject and redo if ANY are true:
1. Hook contém saudação ("Olá pessoal", "E aí galera")
2. Título acima de 100 caracteres ou todo em CAPS
3. Sem thumbnail concept definido
4. Payoff entregue nos primeiros 50% do vídeo
5. Conteúdo puramente teórico sem momento de demonstração
6. Acentuação pt-BR incorreta

## Quality Criteria

- [ ] Título 50-70 chars com keyword nos primeiros 40
- [ ] Thumbnail concept definido antes do roteiro
- [ ] Hook cria curiosity gap nos primeiros 30s
- [ ] 3-5 seções com mini-hooks e pattern interrupts
- [ ] Pelo menos 1 demonstração/case prático
- [ ] Duração estimada 8-15 minutos
- [ ] CTA contextualizado (não genérico)
- [ ] Descrição com timestamps e keywords
- [ ] Tom de voz consistente com a escolha do usuário
- [ ] Acentuação pt-BR correta em todo o texto
