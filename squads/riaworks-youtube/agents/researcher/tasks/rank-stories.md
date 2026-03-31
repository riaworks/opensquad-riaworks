---
task: "Rank Stories"
order: 2
input: |
  - raw_sources: Lista de 15-30 fontes candidatas
output: |
  - ranked_stories: Top 5 notícias ranqueadas com análise completa
---

# Rank Stories

Analisa as fontes candidatas, cross-referencia informações, e produz um ranking das 5 notícias com maior potencial de conteúdo YouTube.

## Process

1. Ler todas as fontes candidatas da fase anterior
2. Agrupar por notícia/tema (múltiplas fontes sobre o mesmo evento)
3. Para cada grupo: cross-referenciar dados para verificar precisão
4. Avaliar cada notícia em 3 dimensões:
   - Relevância para público tech BR (1-5)
   - Potencial de hook provocativo (1-5)
   - Possibilidade de demonstração prática (1-5)
5. Ranquear pelo score total (soma das 3 dimensões)
6. Selecionar top 5 e enriquecer com dados-chave, quotes, e assessment de confiança
7. Compilar output final no formato research-results.md

## Output Format

```yaml
stories:
  - rank: 1
    title: "..."
    source_primary: "..."
    date: "YYYY-MM-DD"
    url: "..."
    summary: "2-3 frases"
    hook_potential: "1 frase sobre por que funciona como conteúdo YouTube"
    key_data: "números, estatísticas, quotes"
    confidence: "Alta/Média/Baixa"
    scores:
      relevance: 5
      hook: 5
      demo: 4
      total: 14
```

## Output Example

```yaml
stories:
  - rank: 1
    title: "Anthropic Lança Claude 4 com Raciocínio 3x Mais Longo"
    source_primary: "Anthropic Blog"
    date: "2026-03-24"
    url: "https://anthropic.com/news/claude-4"
    summary: "A Anthropic lançou o Claude 4 com melhorias de 3x em raciocínio longo e 87% de precisão em código complexo. O modelo supera GPT-5 em 4 de 7 benchmarks."
    hook_potential: "Lançamento de modelo novo + comparativo prático + teste ao vivo = conteúdo altamente demonstrável"
    key_data: "3x mais contexto, 87% precisão código (vs 71% anterior), supera GPT-5 em 4/7 benchmarks"
    confidence: "Alta (Anthropic + The Verge + TechCrunch + Tecnoblog)"
    scores:
      relevance: 5
      hook: 5
      demo: 5
      total: 15
```

## Quality Criteria

- [ ] 5 notícias ranqueadas com scores justificados
- [ ] Cada notícia tem ≥2 fontes corroborando
- [ ] Dados-chave são específicos (números, datas, nomes)
- [ ] Potencial de hook é concreto (não genérico)
- [ ] Confiança atribuída com base em fontes

## Veto Conditions

Reject and redo if ANY are true:
1. Menos de 3 notícias no ranking final
2. Todas as notícias são low confidence
3. Hook potential é genérico ("interessante", "relevante") sem especificidade
