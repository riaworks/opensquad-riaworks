# Task: Gerar Relatorio de Feedback Estruturado

## Task Config

```yaml
order: 2
```

## Objetivo

Transformar a pontuacao da task anterior em um relatorio de feedback estruturado com veredito claro, mudancas obrigatorias, sugestoes opcionais, reconhecimento de pontos fortes e caminho para aprovacao.

## Processo

### 1. Determinacao do Veredito

Com base na pontuacao e classificacao da task anterior:

- **APROVADO:** Media >= 7/10 e nenhum criterio bloqueante abaixo de 5/10
- **REVISAO NECESSARIA:** Media entre 4-6.9/10 ou criterio bloqueante abaixo de 5/10, E ciclo atual < 3
- **REJEITADO:** Media abaixo de 4/10, OU terceiro ciclo sem atingir aprovacao

Registrar o veredito com justificativa baseada nos numeros.

### 2. Mudancas Obrigatorias (Bloqueantes)

Listar APENAS os problemas que impedem publicacao:

- Problemas de acessibilidade (contraste, legibilidade)
- Erros factuais ou de informacao
- Problemas tecnicos (renderizacao, dimensoes)
- Violacoes de regras da plataforma
- Criterios com nota abaixo de 5/10

Para cada problema bloqueante:
- **O que esta errado:** Descricao especifica com referencia ao slide/segundo
- **Por que e bloqueante:** Qual criterio viola e qual o impacto
- **Como corrigir:** Instrucao tecnica precisa e acionavel
- **Criterio de aceite:** Como verificar que a correcao foi feita corretamente

### 3. Sugestoes de Melhoria (Nao-Bloqueantes)

Listar melhorias desejaveis que elevariam a qualidade:

- Ajustes de design que melhorariam a experiencia
- Alternativas de copy ou CTA mais eficazes
- Otimizacoes de hashtags ou caption
- Refinamentos de timing ou transicao

Para cada sugestao:
- **Sugestao:** O que poderia ser melhorado
- **Impacto estimado:** Quanto isso melhoraria a nota (ex: "+0.5 em engajamento")
- **Esforco:** Baixo / Medio / Alto

### 4. Reconhecimento de Pontos Fortes

Listar explicitamente o que esta funcionando bem:

- Criterios com nota >= 8/10
- Elementos criativos que se destacam
- Decisoes que demonstram compreensao do publico
- Evolucoes em relacao a versoes anteriores (se revisao)

### 5. Caminho para Aprovacao

Se o veredito nao for APROVADO:

- Resumir as X mudancas bloqueantes que devem ser feitas
- Estimar quantos criterios mudariam de nota com as correcoes
- Projetar a media esperada apos correcoes
- Indicar quantos ciclos de revisao restam (maximo 3)
- Se ultimo ciclo, alertar que rejeicao e permanente

## Formato de Entrega

```markdown
## Feedback: [Tipo de Conteudo] — [Tema]

### Veredito: [APROVADO / REVISAO NECESSARIA / REJEITADO]
[Justificativa em 1-2 frases]

### Pontos Fortes
- [ponto forte com evidencia]
- ...

### Mudancas Obrigatorias
1. **[Problema]** (Slide X / Segundo Xs)
   - Situacao: [o que esta errado]
   - Correcao: [como consertar]
   - Aceite: [como verificar]

### Sugestoes de Melhoria
1. **[Sugestao]** — Impacto: [estimativa] | Esforco: [nivel]

### Caminho para Aprovacao
- Mudancas obrigatorias: X itens
- Media projetada apos correcoes: X.X/10
- Ciclos restantes: X de 3
```

## Criterios de Conclusao

- Veredito claro com justificativa baseada em criterios numericos
- Mudancas bloqueantes listadas com descricao, correcao e criterio de aceite
- Sugestoes nao-bloqueantes separadas com estimativa de impacto e esforco
- Pontos fortes reconhecidos com evidencias especificas
- Caminho para aprovacao claro (se aplicavel)
- Feedback organizado e facilmente acionavel como checklist
- Ciclo de revisao registrado e limite de 3 respeitado
- Tom profissional e construtivo em todo o relatorio
