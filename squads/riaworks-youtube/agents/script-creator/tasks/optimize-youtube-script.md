---
task: "Optimize YouTube Script"
order: 3
input: |
  - draft_script: Script criado na task anterior
output: |
  - optimized_script: Script otimizado com melhorias de SEO, retenção, e CTA
---

# Optimize YouTube Script

Revisão e otimização do script criado, focando em SEO, retenção, e conversão.

## Process

1. Verificar título contra checklist SEO:
   - Keyword nos primeiros 40 chars?
   - 50-70 chars total?
   - Power word ou número presente?
   - Complementa (não repete) thumbnail?
2. Verificar hook contra benchmarks de retenção:
   - Cria curiosity gap claro?
   - Estabelece stakes em 30 segundos?
   - Sem saudação ou filler?
3. Verificar corpo:
   - Mini-hooks entre seções?
   - Pattern interrupts a cada 45-90s?
   - Pelo menos 1 demonstração/visual marcado?
   - Transições com curiosidade?
4. Verificar payoff: está nos últimos 30%?
5. Verificar CTA: é contextualizado?
6. Otimizar descrição SEO:
   - Primeiros 160 chars com keyword + promessa?
   - Timestamps corretos?
   - Links e recursos?
7. Verificar tags: 5-10 keywords relevantes
8. Verificar acentuação pt-BR
9. Estimar duração (150 palavras ≈ 1 minuto de fala)
10. Aplicar correções e reescrever trechos que não passam nos checks

## Output Format

O mesmo formato do script original, mas otimizado. Incluir ao final:

```
=== OPTIMIZATION NOTES ===
Duração estimada: X minutos (Y palavras)
Mudanças aplicadas:
1. {mudança 1}
2. {mudança 2}
SEO score: X/10
Retention score: X/10
```

## Output Example

```
=== OPTIMIZATION NOTES ===
Duração estimada: 12 minutos (1,800 palavras)

Checklist SEO:
✅ Keyword "Claude 4" nos primeiros 10 chars do título
✅ Título: 65 chars (dentro de 50-70)
✅ Power word presente: "Assustador"
✅ Título complementa thumbnail (não repete)
✅ Descrição: keyword na primeira frase

Checklist Retenção:
✅ Hook sem saudação — abre com afirmação provocativa
✅ Curiosity gap claro ("capacidade que nenhum outro modelo tem")
✅ Stakes estabelecidas em 25 segundos
✅ Pattern interrupts: seção 1 (comparativo visual), seção 2 (screen recording), seção 3 (tela de erro)
⚠️ Seção 2 tinha gap de 2 min sem interrupt — adicionado gráfico de benchmark

Mudanças aplicadas:
1. Título reduzido de 78 para 65 caracteres (removido "Que Sabíamos Sobre IA")
2. Adicionado pattern interrupt na seção 2 (gráfico de benchmark no min 5:30)
3. Mini-hook da seção 3 reescrito: "Mas a maioria dos reviews esconde isso..." (antes era genérico)
4. Descrição: "Claude 4" movido para primeiras 5 palavras
5. Corrigido 3 acentos: informaçao → informação, codigo → código, tambem → também
6. Timestamp do climax ajustado para 70% do vídeo (min 8:24 de 12:00)
7. CTA especificado: "vídeo sobre workflow com Claude Code" (antes era vago)

SEO score: 8/10
Retention score: 9/10
```

## Quality Criteria

- [ ] Todas as verificações do checklist passam
- [ ] Mudanças aplicadas documentadas
- [ ] Duração estimada calculada (150 palavras/min)
- [ ] SEO score ≥ 7/10
- [ ] Retention score ≥ 7/10

## Veto Conditions

Reject and redo if ANY are true:
1. Script final tem mais de 15 minutos estimados sem justificativa
2. SEO score abaixo de 5/10
3. Acentuação pt-BR ainda incorreta após otimização
