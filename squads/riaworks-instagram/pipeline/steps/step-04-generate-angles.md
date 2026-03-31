---
execution: inline
agent: instagram-feed-creator
inputFile: squads/riaworks-instagram/output/research-results.md
outputFile: squads/riaworks-instagram/output/angles.md
---

# Step 04: Gerar Angulos

## Context Loading

Load these files before executing:
- `squads/riaworks-instagram/output/research-results.md` — Pesquisa completa
- `squads/riaworks-instagram/pipeline/data/domain-framework.md` — Framework de geracao de angulos
- `squads/riaworks-instagram/pipeline/data/output-examples.md` — Exemplos de output
- `_opensquad/_memory/company.md` — Contexto da empresa

## Instructions

### Process
1. Ler a noticia selecionada pelo usuario no checkpoint anterior.
2. Extrair: fato principal, dado-chave, contexto, implicacoes.
3. Gerar 5 angulos usando drivers psicologicos diferentes (Medo, Oportunidade, Educacional, Contrario, Inspiracional).
4. Cada angulo inclui: nome do driver, hook de 1 linha, descricao de 2-3 linhas do que o conteudo cobriria, e formatos recomendados (carrossel e/ou reel).

## Output Format

```
ANGULOS GERADOS
Noticia: [titulo da noticia selecionada]

1. 🔴 MEDO
   Hook: "[hook de 1 linha]"
   Descricao: [2-3 linhas sobre o que o conteudo cobriria]
   Formatos: [carrossel / reel / ambos]

2. 🟢 OPORTUNIDADE
   Hook: "[hook]"
   Descricao: [...]
   Formatos: [...]

3. 📚 EDUCACIONAL
   Hook: "[hook]"
   Descricao: [...]
   Formatos: [...]

4. ↔️ CONTRARIO
   Hook: "[hook]"
   Descricao: [...]
   Formatos: [...]

5. ⭐ INSPIRACIONAL
   Hook: "[hook]"
   Descricao: [...]
   Formatos: [...]
```

## Output Example

```
ANGULOS GERADOS
Noticia: Claude 4 lanca com capacidade de agentes de longa duracao

1. 🔴 MEDO
   Hook: "Em 12 meses, devs sem IA serao substituidos"
   Descricao: Conteudo sobre como o Claude 4 automatiza 70% das tarefas de dev e o que isso significa para quem nao se adaptar. Dados do Stack Overflow sobre dependencia de IA.
   Formatos: carrossel (editorial) + reel

2. 🟢 OPORTUNIDADE
   Hook: "Essa e sua janela de 6 meses antes que todo mundo descubra"
   Descricao: Como usar o Claude 4 para multiplicar produtividade agora, enquanto a maioria ainda nao sabe usar agentes. Cases praticos de projetos acelerados.
   Formatos: carrossel (tutorial) + reel

3. 📚 EDUCACIONAL
   Hook: "Testei o Claude 4 por 48 horas. Os resultados me assustaram."
   Descricao: Review hands-on com testes reais: refatoracao, debug, testes automatizados. O que funciona, o que falha, veredito honesto com dados.
   Formatos: carrossel (editorial) + reel

4. ↔️ CONTRARIO
   Hook: "O hype do Claude 4 vai te decepcionar. Veja por que."
   Descricao: Analise critica das limitacoes: contexto finito, alucinacoes em APIs novas, custos elevados. O que a Anthropic nao fala no anuncio.
   Formatos: carrossel (mito vs realidade)

5. ⭐ INSPIRACIONAL
   Hook: "Imagine 20 agentes de IA trabalhando no seu projeto enquanto voce dorme"
   Descricao: Visao do futuro proximo com agentes autonomos. De onde viemos (GPT-3 em 2020) ate onde estamos (Claude 4 em 2026). A aceleracao exponencial em numeros.
   Formatos: carrossel (storytelling) + reel
```

## Veto Conditions

Reject and redo if ANY are true:
1. Menos de 5 angulos gerados
2. Dois ou mais angulos usam o mesmo driver psicologico
3. Hooks sao genericos e nao mencionam dados ou especificidades da noticia

## Quality Criteria

- [ ] 5 angulos com drivers psicologicos distintos
- [ ] Cada hook tem menos de 15 palavras e para o scroll
- [ ] Descricoes sao especificas a esta noticia (nao genericas)
- [ ] Formatos recomendados fazem sentido para cada angulo
- [ ] Linguagem em portugues brasileiro natural
