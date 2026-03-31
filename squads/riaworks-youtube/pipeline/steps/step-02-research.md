---
execution: subagent
agent: researcher
inputFile: squads/riaworks-youtube/pipeline/data/research-focus.md
outputFile: squads/riaworks-youtube/output/research-results.md
model_tier: powerful
---

# Step 02: Pesquisa de Tendências

## Context Loading

Load these files before executing:
- `squads/riaworks-youtube/pipeline/data/research-focus.md` — Tema e período selecionados pelo usuário
- `squads/riaworks-youtube/pipeline/data/research-brief.md` — Frameworks e técnicas de pesquisa
- `squads/riaworks-youtube/pipeline/data/domain-framework.md` — Framework operacional do squad

## Instructions

### Process
1. Ler o tema e período definidos em research-focus.md
2. Executar busca ampla com WebSearch: 15-30 fontes candidatas sobre o tema
3. Filtrar por relevância para público tech brasileiro e frescor da informação
4. Selecionar as 5 principais notícias/desenvolvimentos, ranqueados por potencial de conteúdo YouTube
5. Para cada notícia: extrair título, fonte, data, resumo de 2-3 frases, e potencial de hook
6. Cross-referenciar dados entre fontes para verificar precisão
7. Compilar no formato de output abaixo

## Output Format

```markdown
# Pesquisa: {tema}

**Período:** {período selecionado}
**Data da pesquisa:** {YYYY-MM-DD}
**Total de fontes consultadas:** {N}

---

## Notícia 1: {Título}
**Fonte:** {nome da fonte} | **Data:** {YYYY-MM-DD}
**URL:** {link}
**Resumo:** {2-3 frases descrevendo a notícia}
**Potencial de hook:** {por que isso funciona como conteúdo YouTube — 1-2 frases}
**Dados-chave:** {números, estatísticas, quotes relevantes}
**Confiança:** Alta/Média/Baixa (baseado em corroboração de fontes)

## Notícia 2: {Título}
[mesma estrutura]

## Notícia 3: {Título}
[mesma estrutura]

## Notícia 4: {Título}
[mesma estrutura]

## Notícia 5: {Título}
[mesma estrutura]

---

## Fontes Consultadas
| # | Fonte | URL | Data acesso | Relevância |
|---|-------|-----|-------------|------------|
| 1 | {nome} | {url} | {data} | Alta/Média/Baixa |
```

## Output Example

```markdown
# Pesquisa: novidades de IA da semana

**Período:** Últimos 7 dias
**Data da pesquisa:** 2026-03-26
**Total de fontes consultadas:** 22

---

## Notícia 1: Anthropic Lança Claude 4 com Raciocínio em Cadeia 3x Mais Longo
**Fonte:** The Verge | **Data:** 2026-03-24
**URL:** https://theverge.com/...
**Resumo:** A Anthropic lançou o Claude 4 com melhorias significativas em raciocínio longo e código. O novo modelo supera o GPT-5 em 4 de 7 benchmarks principais e introduz uma nova capacidade de análise multi-arquivo.
**Potencial de hook:** Altíssimo — lançamento de modelo novo é trending, permite comparativo prático, teste ao vivo, e opinião forte.
**Dados-chave:** 3x mais contexto, 87% de precisão em código complexo (vs 71% do antecessor), disponível via API desde 24/03.
**Confiança:** Alta (confirmado por Anthropic, The Verge, TechCrunch)

## Notícia 2: Google DeepMind Revela Gemini 3 com Capacidade de Vídeo Nativa
**Fonte:** Google Blog | **Data:** 2026-03-22
**URL:** https://blog.google/...
**Resumo:** O Gemini 3 introduz processamento nativo de vídeo em tempo real, permitindo análise e geração de vídeo sem pré-processamento.
**Potencial de hook:** Forte — visual, demonstrável, permite comparativo com outros modelos.
**Dados-chave:** Processa 2h de vídeo em tempo real, 45% de redução em custo de API vs Gemini 2.
**Confiança:** Alta (fonte primária Google)
```

## Veto Conditions

Reject and redo if ANY are true:
1. Menos de 3 notícias encontradas sobre o tema no período especificado
2. Nenhuma fonte verificável citada (todas low confidence)
3. Notícias não são relevantes para público tech brasileiro

## Quality Criteria

- [ ] Mínimo 5 notícias ranqueadas com potencial de hook avaliado
- [ ] Cada notícia tem fonte, data, URL verificável
- [ ] Dados-chave incluem números específicos (não vagos)
- [ ] Nível de confiança atribuído a cada notícia
- [ ] Fontes primárias priorizadas sobre secundárias
