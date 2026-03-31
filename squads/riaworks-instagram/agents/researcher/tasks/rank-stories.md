---
task: rank-stories
order: 2
input:
  - research_raw: "output/research-raw.yaml"
  - research_brief: "pipeline/data/research-brief.md"
output:
  - research_ranked: "output/research-ranked.yaml"
---

## Process

### Step 1 — Avaliacao por Criterios
Para cada noticia do `research-raw.yaml`, atribuir pontuacao de 1 a 5 em quatro dimensoes:
- **Novidade**: quao inedita e a informacao (5 = primeira vez reportada, 1 = reciclagem de noticia antiga)
- **Impacto**: relevancia para o publico tech brasileiro (5 = afeta diretamente usuarios, 1 = nicho muito restrito)
- **Visual**: potencial para conteudo visual no Instagram (5 = demo/comparacao/antes-depois, 1 = puramente textual/abstrato)
- **Timing**: urgencia e atualidade (5 = aconteceu hoje, 1 = mais de 48h e sem relevancia duradoura)

### Step 2 — Classificacao e Corte
Calcular score total (soma das 4 dimensoes, max 20). Ordenar do maior para o menor score.
Aplicar filtros de corte:
- Remover noticias com score total abaixo de 10
- Remover noticias com confianca "baixa" e score abaixo de 14
- Limitar saida final a no maximo 5 noticias ranqueadas

### Step 3 — Recomendacao de Formato
Para cada noticia que passou no corte, recomendar o formato Instagram mais adequado:
- **carrossel**: noticias com multiplos pontos, comparacoes, listas ou explicacoes passo-a-passo
- **reel**: noticias com elemento de demonstracao, reacao, ou narrativa curta e impactante
- **ambos**: noticias com potencial para os dois formatos

Incluir justificativa breve para a recomendacao.

## Output Format

```yaml
ranked_date: "YYYY-MM-DD"
input_total: <total de noticias avaliadas>
output_total: <total apos corte>
ranked_stories:
  - rank: 1
    story_id: <id do research-raw>
    title: "<titulo>"
    scores:
      novidade: <1-5>
      impacto: <1-5>
      visual: <1-5>
      timing: <1-5>
      total: <4-20>
    confidence: "alta|media|baixa"
    recommended_format: "carrossel|reel|ambos"
    format_justification: "<justificativa em 1 frase>"
```

## Output Example

```yaml
ranked_date: "2026-03-13"
input_total: 8
output_total: 3
ranked_stories:
  - rank: 1
    story_id: 1
    title: "Anthropic lanca Claude 5 com capacidade de raciocinio avancado"
    scores:
      novidade: 5
      impacto: 5
      visual: 4
      timing: 5
      total: 19
    confidence: "alta"
    recommended_format: "carrossel"
    format_justification: "Comparacao de benchmarks e features funciona melhor em slides sequenciais com dados visuais."
  - rank: 2
    story_id: 2
    title: "Google DeepMind apresenta novo modelo multimodal para video"
    scores:
      novidade: 5
      impacto: 4
      visual: 5
      timing: 4
      total: 18
    confidence: "alta"
    recommended_format: "reel"
    format_justification: "Demonstracao de geracao de video tem alto impacto visual e funciona como reel de reacao."
  - rank: 3
    story_id: 5
    title: "Brasil entra no top 10 de paises com mais startups de IA"
    scores:
      novidade: 3
      impacto: 5
      visual: 3
      timing: 3
      total: 14
    confidence: "media"
    recommended_format: "carrossel"
    format_justification: "Dados estatisticos e ranking funcionam bem em formato listicle com graficos."
```

## Quality Criteria

- [ ] Todas as 4 dimensoes de pontuacao preenchidas para cada noticia avaliada
- [ ] Noticias ordenadas corretamente por score total decrescente
- [ ] Filtros de corte aplicados conforme regras definidas
- [ ] Recomendacao de formato inclui justificativa coerente com os scores

## Veto Conditions

- **Rejeitar** qualquer ranking que inclua mais de 5 noticias na saida final (manter foco para o squad).
- **Rejeitar** noticias com score de impacto igual a 1 independente do score total (sem relevancia para o publico-alvo).
