---
execution: inline
agent: script-creator
inputFile: squads/riaworks-youtube/output/research-results.md
outputFile: squads/riaworks-youtube/output/angles.md
---

# Step 04: Geração de Ângulos

## Context Loading

Load these files before executing:
- `squads/riaworks-youtube/output/research-results.md` — Notícia selecionada pelo usuário
- `squads/riaworks-youtube/pipeline/data/domain-framework.md` — Framework de ângulos e hooks
- `squads/riaworks-youtube/pipeline/data/output-examples.md` — Exemplos de output de qualidade
- `squads/riaworks-youtube/pipeline/data/anti-patterns.md` — Padrões a evitar
- `_opensquad/_memory/company.md` — Contexto da empresa Riaworks

## Instructions

### Process
1. Ler a notícia selecionada pelo usuário no checkpoint anterior
2. Identificar o core insight da notícia — o que é genuinamente novo/importante
3. Gerar 5 ângulos distintos usando os drivers emocionais do domain-framework:
   - 🔴 Medo/Urgência
   - 🟢 Oportunidade
   - 📚 Educacional
   - ↔️ Contrário
   - ⭐ Inspiracional
4. Para cada ângulo: criar título provisório, hook de abertura, e pitch de 1 frase
5. Classificar os ângulos por potencial de viralização (baseado nos padrões dos canais investigados)

## Output Format

```markdown
# Ângulos: {título da notícia}

**Notícia base:** {resumo da notícia em 1 frase}
**Core insight:** {o que é genuinamente novo/importante}

---

## Ângulo 1: 🔴 Medo/Urgência
**Título provisório:** {50-70 chars}
**Hook (primeiros 10s):** "{frase de abertura do vídeo}"
**Pitch:** {1 frase descrevendo a abordagem}
**Potencial:** ⭐⭐⭐⭐⭐ / ⭐⭐⭐⭐ / ⭐⭐⭐

## Ângulo 2: 🟢 Oportunidade
[mesma estrutura]

## Ângulo 3: 📚 Educacional
[mesma estrutura]

## Ângulo 4: ↔️ Contrário
[mesma estrutura]

## Ângulo 5: ⭐ Inspiracional
[mesma estrutura]
```

## Output Example

```markdown
# Ângulos: Anthropic Lança Claude 4

**Notícia base:** Anthropic lançou Claude 4 com raciocínio 3x mais longo e melhorias significativas em código.
**Core insight:** Primeiro modelo que genuinamente reduz tempo de refatoração de código legado em ordem de magnitude.

---

## Ângulo 1: 🔴 Medo/Urgência
**Título provisório:** Devs Que Ignorarem o Claude 4 Vão Ficar para Trás — Testei e Provei
**Hook:** "Se você é dev e ainda não testou o Claude 4, você já está perdendo produtividade. Não é exagero — eu medi."
**Pitch:** Foco na gap competitiva: quem usa IA avançada vs quem não usa, com dados concretos.
**Potencial:** ⭐⭐⭐⭐

## Ângulo 2: 🟢 Oportunidade
**Título provisório:** Claude 4 Mudou Tudo — Essa É Sua Janela Antes Que Todo Mundo Descubra
**Hook:** "A Anthropic acabou de lançar algo que muda o jogo pra dev. E a maioria nem sabe ainda."
**Pitch:** Foco na vantagem de first-mover: quem dominar primeiro terá edge competitivo.
**Potencial:** ⭐⭐⭐⭐⭐

## Ângulo 3: 📚 Educacional
**Título provisório:** Testei o Claude 4 com Código Real — Resultado É Assustador [Comparativo]
**Hook:** "48 horas testando o Claude 4 com projetos reais de logística. Aqui estão os resultados."
**Pitch:** Teste prático transparente com métricas reais, sem hype.
**Potencial:** ⭐⭐⭐⭐⭐

## Ângulo 4: ↔️ Contrário
**Título provisório:** Todo Mundo Tá Elogiando o Claude 4 — Mas Encontrei 3 Problemas Sérios
**Hook:** "Os reviews estão todos positivos. Mas ninguém testou o que eu testei. E descobri 3 falhas graves."
**Pitch:** Contrarian take honesto — reconhece melhorias mas expõe limitações reais.
**Potencial:** ⭐⭐⭐⭐

## Ângulo 5: ⭐ Inspiracional
**Título provisório:** Em 2026, Um Dev com IA Vale por 10 — O Claude 4 Provou Isso
**Hook:** "Imagine ter 10 estagiários que nunca dormem, nunca reclamam, e entregam em minutos. Esse é o Claude 4."
**Pitch:** Visão aspiracional do futuro do dev com IA, usando o Claude 4 como case.
**Potencial:** ⭐⭐⭐
```

## Veto Conditions

Reject and redo if ANY are true:
1. Menos de 5 ângulos distintos gerados
2. Dois ou mais ângulos usam o mesmo driver emocional
3. Hooks são genéricos e não fazem referência à notícia específica

## Quality Criteria

- [ ] 5 ângulos com drivers emocionais genuinamente distintos
- [ ] Cada título tem 50-70 caracteres e segue fórmula curiosity gap + benefício
- [ ] Cada hook é específico à notícia (não seria reutilizável para outra notícia)
- [ ] Potencial de viralização avaliado com justificativa implícita
- [ ] Alinhado com tom de voz do Canal Riaworks (técnico, direto, opinativo)
