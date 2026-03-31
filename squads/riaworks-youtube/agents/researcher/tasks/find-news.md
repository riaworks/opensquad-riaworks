---
task: "Find News"
order: 1
input: |
  - research_focus: Tema e período definidos pelo usuário
output: |
  - raw_sources: Lista de 15-30 fontes candidatas com URLs e resumos
---

# Find News

Busca ampla por notícias e desenvolvimentos relevantes sobre o tema definido pelo usuário, priorizando fontes primárias e frescor.

## Process

1. Ler tema e período de research-focus.md
2. Executar 5-8 queries de WebSearch variando termos e idiomas (pt-BR e en):
   - "{tema} news {período}" (inglês)
   - "{tema} notícias {período}" (português)
   - "{tema} announcement official" (fonte primária)
   - "{tema} analysis deep dive" (análise aprofundada)
   - "{tema} Brasil impacto" (relevância local)
3. Para cada resultado: registrar URL, título, data de publicação, fonte, e resumo de 1 frase
4. Remover duplicatas e fontes não-confiáveis (sem autoria, sem data, conteúdo gerado por IA sem verificação)
5. Manter 15-30 fontes candidatas para fase de ranking

## Output Format

```yaml
sources:
  - url: "https://..."
    title: "..."
    source: "The Verge"
    date: "2026-03-25"
    summary: "..."
    language: "en"
    type: "primary" | "secondary" | "opinion"
```

## Output Example

```yaml
sources:
  - url: "https://www.anthropic.com/news/claude-4"
    title: "Introducing Claude 4"
    source: "Anthropic Blog"
    date: "2026-03-24"
    summary: "Anthropic lança Claude 4 com raciocínio em cadeia 3x mais longo e melhorias em código."
    language: "en"
    type: "primary"

  - url: "https://theverge.com/2026/3/24/claude-4-review"
    title: "Claude 4 review: Anthropic's best model yet"
    source: "The Verge"
    date: "2026-03-24"
    summary: "Review independente confirma melhorias em raciocínio e código, mas aponta limitações em contexto longo."
    language: "en"
    type: "secondary"

  - url: "https://tecnoblog.net/noticias/2026/03/25/claude-4-novidades/"
    title: "Claude 4: tudo sobre o novo modelo da Anthropic"
    source: "Tecnoblog"
    date: "2026-03-25"
    summary: "Resumo em português das novidades do Claude 4 com contexto para público brasileiro."
    language: "pt"
    type: "secondary"
```

## Quality Criteria

- [ ] Mínimo 15 fontes candidatas coletadas
- [ ] Mix de fontes primárias e secundárias
- [ ] Mix de idiomas (pt-BR e en)
- [ ] Cada fonte tem URL, data, e tipo classificados
- [ ] Duplicatas removidas

## Veto Conditions

Reject and redo if ANY are true:
1. Menos de 10 fontes candidatas encontradas
2. Zero fontes primárias na lista
