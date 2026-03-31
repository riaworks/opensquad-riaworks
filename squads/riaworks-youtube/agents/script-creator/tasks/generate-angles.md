---
task: "Generate Angles"
order: 1
input: |
  - selected_news: Notícia selecionada pelo usuário no checkpoint
  - research_results: Dados completos da pesquisa
output: |
  - angles: 5 ângulos distintos com títulos, hooks, e potencial
---

# Generate Angles

Gera 5 ângulos emocionalmente distintos a partir de uma única notícia selecionada. Cada ângulo transforma a mesma história em conteúdo completamente diferente.

## Process

1. Identificar o core insight da notícia — o que é genuinamente novo/importante
2. Para cada driver emocional (Medo, Oportunidade, Educacional, Contrário, Inspiracional):
   a. Definir a perspectiva única que esse ângulo traz
   b. Criar título provisório (50-70 chars, keyword nos primeiros 40)
   c. Escrever hook de abertura (primeiros 10 segundos do vídeo)
   d. Resumir o pitch em 1 frase
3. Avaliar potencial de viralização (1-5 estrelas) baseado nos padrões dos canais investigados:
   - Provocação = alto engajamento (@deborahfolloni: 189K)
   - Teste prático = alto watch time (@RenatoAsse: 272K)
   - Número concreto = alto CTR (@TalksbyLeo: 71K)
4. Ordenar do maior para menor potencial

## Output Format

```yaml
news_base: "resumo da notícia em 1 frase"
core_insight: "o que é genuinamente novo"
angles:
  - driver: "🔴 Medo/Urgência"
    title: "50-70 chars"
    hook: "frase de abertura do vídeo"
    pitch: "1 frase descrevendo a abordagem"
    potential: 4
  - driver: "🟢 Oportunidade"
    title: "..."
    hook: "..."
    pitch: "..."
    potential: 5
```

## Output Example

```yaml
news_base: "Anthropic lançou Claude 4 com raciocínio 3x mais longo"
core_insight: "Primeiro modelo que reduz tempo de refatoração de código legado em ordem de magnitude"
angles:
  - driver: "🔴 Medo/Urgência"
    title: "Devs Que Ignorarem o Claude 4 Vão Ficar para Trás"
    hook: "Se você é dev e ainda não testou o Claude 4, você já está perdendo produtividade."
    pitch: "Gap competitiva: quem usa IA avançada vs quem não usa."
    potential: 4
  - driver: "🟢 Oportunidade"
    title: "Claude 4 Mudou Tudo — Sua Janela Antes de Todo Mundo"
    hook: "A Anthropic lançou algo que muda o jogo pra dev. E a maioria nem sabe."
    pitch: "Vantagem de first-mover: dominar primeiro = edge competitivo."
    potential: 5
  - driver: "📚 Educacional"
    title: "Testei o Claude 4 com Código Real — Resultado Assustador"
    hook: "48 horas testando Claude 4 com projetos reais. Aqui estão os resultados."
    pitch: "Teste prático transparente com métricas reais, sem hype."
    potential: 5
  - driver: "↔️ Contrário"
    title: "Todo Mundo Elogiando o Claude 4 — Encontrei 3 Problemas"
    hook: "Os reviews estão positivos. Mas ninguém testou o que eu testei."
    pitch: "Contrarian honesto — reconhece melhorias, expõe limitações."
    potential: 4
  - driver: "⭐ Inspiracional"
    title: "Em 2026, Um Dev com IA Vale por 10 — Claude 4 Provou"
    hook: "Imagine 10 estagiários que nunca dormem. Esse é o Claude 4."
    pitch: "Visão aspiracional do futuro do dev com IA."
    potential: 3
```

## Quality Criteria

- [ ] 5 ângulos com drivers genuinamente distintos
- [ ] Cada título tem 50-70 caracteres
- [ ] Hooks são específicos à notícia (não reutilizáveis)
- [ ] Potencial avaliado com coerência
- [ ] Nenhum ângulo repete driver emocional

## Veto Conditions

Reject and redo if ANY are true:
1. Menos de 5 ângulos distintos
2. Dois ângulos com o mesmo driver emocional
3. Hooks genéricos que funcionariam para qualquer notícia
