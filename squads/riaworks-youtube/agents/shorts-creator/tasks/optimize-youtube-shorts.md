---
task: "Optimize YouTube Shorts"
order: 2
input: |
  - shorts_drafts: 2 variantes de Shorts criadas
output: |
  - optimized_shorts: 2 variantes otimizadas com notas de melhoria
---

# Optimize YouTube Shorts

Revisão e otimização das 2 variantes de Shorts para maximizar completion rate e loop replays.

## Process

1. Para cada variante, verificar:
   - Hook prende em 2 segundos? (test: se eu visse isso no feed, pararia de scrollar?)
   - Duração estimada é 15-45 segundos?
   - Apenas 1 takeaway? (se tem mais, cortar)
   - Text overlays em todos os momentos-chave?
   - Loop design é natural? (final realmente conecta ao início?)
   - Título é curiosity-driven e conciso?
   - #Shorts presente?
   - Acentuação correta?
2. Calcular word count e estimar duração (200 palavras ≈ 1 minuto falado rápido)
3. Cortar qualquer filler word: "basicamente", "então", "na verdade", "tipo"
4. Verificar ritmo de cortes: deve ter mudança visual a cada 3-5 segundos
5. Verificar se variantes são genuinamente diferentes (não apenas reworded)
6. Aplicar correções e reescrever trechos necessários

## Output Format

Shorts otimizados no mesmo formato + notas de otimização:

```
=== OPTIMIZATION NOTES ===
Variante A:
- Duração estimada: Xs (Y palavras)
- Mudanças: [lista]
- Completion rate prediction: Alto/Médio/Baixo

Variante B:
- Duração estimada: Xs (Y palavras)
- Mudanças: [lista]
- Completion rate prediction: Alto/Médio/Baixo
```

## Output Example

```
=== OPTIMIZATION NOTES ===

Variante A: "3 Minutos vs 3 Dias"
- Duração estimada: 38s (95 palavras)
- Word count check: 95 palavras / 200 wpm rápido = ~28s falado + 10s pausas visuais = 38s ✅
- Checklist:
  ✅ Hook prende em 2s (text overlay "3 MINUTOS vs 3 DIAS" é scroll-stop)
  ✅ Apenas 1 takeaway (IA resolve tarefa de API mais rápido e melhor)
  ✅ Text overlays em 4/4 cuts
  ✅ Loop natural (volta para tela de código = mesma cena do hook)
  ✅ #Shorts presente na descrição
  ✅ Acentuação correta
  ⚠️ Cut 4 não tinha text overlay — adicionado
- Mudanças: Cortado "basicamente" do cut 2, adicionado text overlay "QUEM USA IA VENCE" no cut 4
- Filler words removidos: 1 ("basicamente")
- Completion rate prediction: Alto (hook forte, loop visual natural, 38s é sweet spot)

Variante B: "200 Endpoints"
- Duração estimada: 33s (82 palavras)
- Word count check: 82 palavras / 200 wpm = ~24s falado + 9s visuais = 33s ✅
- Checklist:
  ✅ Hook prende em 2s (contador numérico em fast-forward é visualmente hipnótico)
  ✅ Apenas 1 takeaway
  ✅ Text overlays em 3/3 cuts
  ✅ Loop numérico (contador reinicia = conecta ao hook)
  ✅ #Shorts presente
  ✅ Acentuação correta
- Mudanças: Reescrito hook para "200 endpoints. 3 minutos. Zero erros." (mais impactante que original), removido cut intermediário redundante
- Filler words removidos: 0 (já limpo)
- Completion rate prediction: Alto (split-screen engaging, loop numérico criativo, 33s compacto)

Diferenciação confirmada: A usa narrativa linear + loop visual | B usa split-screen + loop numérico ✅
```

## Quality Criteria

- [ ] Ambas as variantes otimizadas
- [ ] Duração estimada calculada para cada
- [ ] Filler words removidos
- [ ] Cortes a cada 3-5 segundos verificados
- [ ] Variantes são genuinamente distintas

## Veto Conditions

Reject and redo if ANY are true:
1. Short >60 segundos após otimização
2. Filler words ainda presentes
3. Text overlays ausentes em algum momento-chave
