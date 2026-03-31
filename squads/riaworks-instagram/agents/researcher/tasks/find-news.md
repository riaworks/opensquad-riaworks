---
task: find-news
order: 1
input:
  - research_focus: "Foco de pesquisa definido no checkpoint step-01"
  - research_brief: "pipeline/data/research-brief.md"
output:
  - research_raw: "output/research-raw.yaml"
---

## Process

### Step 1 — Varredura Ampla (Broad Sweep)
Realizar buscas em pelo menos 10 fontes distintas usando `web_search`. Cobrir obrigatoriamente:
- Blogs oficiais de empresas de IA (Anthropic, OpenAI, Google DeepMind, Meta AI, Microsoft)
- Midia tech internacional (The Verge, TechCrunch, Ars Technica, Wired)
- Midia tech brasileira (Canaltech, Olhar Digital, TecMundo)
- Repositorios e benchmarks (GitHub trending, LMSYS Chatbot Arena, arXiv)

Usar termos de busca variados: combinar o foco de pesquisa com palavras-chave como "AI", "LLM", "machine learning", "tech news today", "inteligencia artificial".

### Step 2 — Coleta e Verificacao
Para cada noticia encontrada, usar `web_fetch` para acessar a fonte primaria e extrair:
- Titulo original e data de publicacao
- Resumo factual em ate 3 frases
- Fonte primaria (URL do anuncio/paper/blog oficial)
- Fonte secundaria de confirmacao quando disponivel

Descartar noticias com mais de 72 horas, a menos que sejam tendencias relevantes ao foco.

### Step 3 — Estruturacao
Organizar todas as noticias coletadas no formato de saida padrao. Atribuir nivel de confianca baseado na qualidade das fontes:
- **alta**: fonte primaria oficial + pelo menos 1 confirmacao independente
- **media**: fonte confiavel mas sem confirmacao cruzada
- **baixa**: rumor, vazamento ou fonte unica nao oficial

## Output Format

```yaml
research_date: "YYYY-MM-DD"
focus: "<foco definido no checkpoint>"
total_found: <numero>
stories:
  - id: 1
    title: "<titulo descritivo em portugues>"
    summary: "<resumo factual em 2-3 frases>"
    source_primary:
      name: "<nome da fonte>"
      url: "<url>"
    source_secondary:
      name: "<nome da fonte ou null>"
      url: "<url ou null>"
    published_at: "YYYY-MM-DD"
    confidence: "alta|media|baixa"
    tags: ["<tag1>", "<tag2>"]
```

## Output Example

```yaml
research_date: "2026-03-13"
focus: "lancamentos e atualizacoes de modelos de IA"
total_found: 8
stories:
  - id: 1
    title: "Anthropic lanca Claude 5 com capacidade de raciocinio avancado"
    summary: "A Anthropic anunciou o Claude 5, novo modelo com melhorias significativas em raciocinio matematico e programacao. O modelo superou o GPT-5 em 7 dos 10 benchmarks principais. Disponivel via API e plataforma web a partir de hoje."
    source_primary:
      name: "Anthropic Blog"
      url: "https://blog.anthropic.com/claude-5-launch"
    source_secondary:
      name: "The Verge"
      url: "https://theverge.com/2026/3/13/anthropic-claude-5"
    published_at: "2026-03-13"
    confidence: "alta"
    tags: ["LLM", "Anthropic", "lancamento", "benchmarks"]
  - id: 2
    title: "Google DeepMind apresenta novo modelo multimodal para video"
    summary: "O DeepMind revelou Gemini Video, capaz de entender e gerar videos de ate 5 minutos com coerencia narrativa. A demonstracao inclui edicao por instrucoes em linguagem natural. Lancamento previsto para o segundo trimestre."
    source_primary:
      name: "Google DeepMind Blog"
      url: "https://deepmind.google/gemini-video"
    source_secondary:
      name: "TechCrunch"
      url: "https://techcrunch.com/2026/03/13/deepmind-gemini-video"
    published_at: "2026-03-13"
    confidence: "alta"
    tags: ["multimodal", "Google", "video", "geracao"]
```

## Quality Criteria

- [ ] Minimo de 5 noticias coletadas por rodada de pesquisa
- [ ] Todas as noticias possuem fonte primaria com URL acessivel
- [ ] Nivel de confianca atribuido corretamente segundo os criterios definidos
- [ ] Nenhuma noticia sem data de publicacao identificada

## Veto Conditions

- **Rejeitar** qualquer noticia baseada exclusivamente em posts de redes sociais sem confirmacao de fonte jornalistica ou oficial.
- **Rejeitar** noticias que sejam puramente opinativas ou editoriais sem novidade factual verificavel.
