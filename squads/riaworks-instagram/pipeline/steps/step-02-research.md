---
execution: subagent
agent: researcher
inputFile: squads/riaworks-instagram/pipeline/data/research-focus.md
outputFile: squads/riaworks-instagram/output/research-results.md
model_tier: powerful
---

# Step 02: Pesquisa de Noticias Tech/IA

## Context Loading

Load these files before executing:
- `squads/riaworks-instagram/pipeline/data/research-focus.md` — Tema e periodo definidos pelo usuario
- `squads/riaworks-instagram/pipeline/data/research-brief.md` — Fontes recomendadas e frameworks de pesquisa
- `squads/riaworks-instagram/pipeline/data/domain-framework.md` — Pilares de conteudo do canal
- `_opensquad/_memory/company.md` — Contexto da empresa

## Instructions

### Process
1. Ler o foco de pesquisa definido pelo usuario (tema + periodo de tempo).
2. Conduzir broad sweep usando WebSearch: buscar o tema em 4-6 fontes diferentes (blogs oficiais, midia tech, repositorios, papers). Coletar 15-20 resultados candidatos.
3. Para cada resultado relevante, usar web_fetch para extrair detalhes: titulo, data, fonte, resumo do conteudo, dados quantitativos ou benchmarks mencionados.
4. Filtrar por relevancia ao publico do Canal Riaworks (entusiastas de tech brasileiros) e por qualidade da fonte.
5. Ranquear as top 5 noticias/tendencias por potencial de engajamento no Instagram (controversia, novidade, impacto pratico, dados surpresa).
6. Para cada noticia ranqueada, escrever: titulo, fonte com URL, data, resumo de 3-5 linhas, dado-chave (numero, benchmark, metrica), e potencial de angulo.

## Output Format

```
RESEARCH RESULTS
Topic: [tema pesquisado]
Time Range: [periodo]
Date: [data da pesquisa]

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

TOP 5 NOTICIAS/TENDENCIAS

1. [Titulo]
   Fonte: [nome] | URL: [link]
   Data: [data publicacao]
   Resumo: [3-5 linhas]
   Dado-chave: [numero, benchmark ou metrica principal]
   Potencial: [por que seria bom conteudo para Instagram]

2. [...]
...

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

SOURCES
| # | Source | Type | Relevance | Date |
|---|--------|------|-----------|------|
| 1 | ...    | ...  | .../10    | ...  |
...

GAPS
- [o que nao foi encontrado]
```

## Output Example

```
RESEARCH RESULTS
Topic: Lancamento do Claude 4 e agentes autonomos
Time Range: Ultimos 7 dias
Date: 2026-03-13

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

TOP 5 NOTICIAS/TENDENCIAS

1. Claude 4 lanca com capacidade de agentes de longa duracao
   Fonte: Anthropic Blog | URL: https://blog.anthropic.com/claude-4
   Data: 2026-03-10
   Resumo: A Anthropic lancou o Claude 4 com suporte nativo a agentes que podem executar tarefas complexas por horas sem supervisao. O modelo alcancou 94.1% no MMLU, superando o GPT-5 por 2.3 pontos. Destaque para a janela de contexto de 500K tokens e a capacidade de usar ferramentas em cadeia.
   Dado-chave: 94.1% MMLU, 500K tokens de contexto, agentes de ate 8 horas de execucao
   Potencial: Alto — tema quente, dados concretos, impacta diretamente como devs trabalham

2. OpenAI responde com GPT-5 Turbo focado em velocidade
   Fonte: The Verge | URL: https://theverge.com/2026/3/11/gpt5-turbo
   Data: 2026-03-11
   Resumo: Menos de 24h apos o lancamento do Claude 4, a OpenAI liberou o GPT-5 Turbo com latencia 3x menor que o GPT-5 padrao. Benchmark MMLU de 91.8%. Foco em aplicacoes real-time e API para agentes.
   Dado-chave: Latencia 3x menor, 91.8% MMLU
   Potencial: Alto — rivalidade IA gera engajamento, comparacao direta com Claude 4

3. Cursor 2.0 integra agentes autonomos de codigo
   Fonte: TechCrunch | URL: https://techcrunch.com/2026/03/12/cursor-2
   Data: 2026-03-12
   Resumo: O Cursor lancou a versao 2.0 com agentes de codigo que podem trabalhar em background por horas. Integracao com Claude 4 e GPT-5 como backends. Usuarios reportam reducao de 70% no tempo de desenvolvimento para projetos padrao.
   Dado-chave: Reducao de 70% no tempo de dev
   Potencial: Muito alto — ferramenta que o publico usa, resultado pratico mensuravel

4. Meta lanca Llama 4 open-source com 405B parametros
   Fonte: Meta AI Blog | URL: https://ai.meta.com/llama-4
   Data: 2026-03-09
   Resumo: O Llama 4 de 405B parametros foi liberado como open-source sob licenca comercial. Performance competitiva com modelos closed-source em varios benchmarks. Comunidade ja esta fazendo fine-tuning para casos especificos.
   Dado-chave: 405B parametros, open-source, licenca comercial
   Potencial: Alto — debate open vs closed, impacto no ecossistema

5. Estudo mostra que 60% dos devs ja usam IA diariamente
   Fonte: Stack Overflow Developer Survey 2026 | URL: https://survey.stackoverflow.co/2026
   Data: 2026-03-08
   Resumo: A pesquisa anual do Stack Overflow revela que 60% dos desenvolvedores usam ferramentas de IA como assistentes de codigo no dia a dia, contra 44% em 2025. O dado mais surpreendente: 23% dizem que nao conseguiriam mais programar sem IA.
   Dado-chave: 60% usam IA diariamente (vs 44% em 2025), 23% se consideram dependentes
   Potencial: Alto — dados surpresa sobre dependencia geram debate

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

SOURCES
| # | Source | Type | Relevance | Date |
|---|--------|------|-----------|------|
| 1 | Anthropic Blog | Official | 10/10 | 2026-03-10 |
| 2 | The Verge | Media | 8/10 | 2026-03-11 |
| 3 | TechCrunch | Media | 9/10 | 2026-03-12 |
| 4 | Meta AI Blog | Official | 9/10 | 2026-03-09 |
| 5 | Stack Overflow | Survey | 8/10 | 2026-03-08 |

GAPS
- Nao encontrado benchmark comparativo direto Claude 4 vs GPT-5 em coding tasks
- Dados de adocao de IA por devs brasileiros especificamente nao disponiveis
```

## Veto Conditions

Reject and redo if ANY are true:
1. Menos de 3 noticias encontradas com fontes verificaveis
2. Nenhum dado quantitativo (numeros, benchmarks, metricas) em nenhuma noticia

## Quality Criteria

- [ ] Todas as noticias tem URL de fonte verificavel
- [ ] Pelo menos 4 das 5 noticias tem dados quantitativos
- [ ] Resumos tem entre 3-5 linhas cada
- [ ] Potencial de engajamento e justificado para cada noticia
- [ ] Tabela de sources preenchida com tipo e relevancia
- [ ] Gaps documentados
