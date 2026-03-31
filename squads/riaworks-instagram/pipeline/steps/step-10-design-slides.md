---
execution: inline
agent: designer
inputFile: squads/riaworks-instagram/output/instagram-feed-content.md
outputFile: squads/riaworks-instagram/output/carousel-slides/
---

# Step 10: Design Visual dos Slides

## Context Loading

Load these files before executing:
- `squads/riaworks-instagram/output/instagram-feed-content.md` — Conteudo textual do carrossel
- `squads/riaworks-instagram/pipeline/data/domain-framework.md` — Pilares visuais do canal
- `_opensquad/_memory/company.md` — Contexto visual da marca
- Skill instructions: image-creator, image-fetcher

## Instructions

### Process
1. Ler o conteudo textual do carrossel (slides, headlines, supporting text).
2. Definir o design system: cores, fontes, espacamento, grid (1080x1440px, ratio 3:4).
3. Usar image-fetcher para buscar fotos editoriais relevantes ao tema (tech, IA, codigo).
4. Criar HTML/CSS auto-contido para cada slide seguindo as best practices de image-design.
5. Renderizar slide 1 (cover) usando image-creator e verificar visualmente.
6. Apos aprovacao do slide 1, renderizar os demais slides em batch.
7. Salvar todas as imagens renderizadas em squads/riaworks-instagram/output/carousel-slides/.

## Output Format

Para cada slide:
- Design system documentado
- Arquivo HTML auto-contido
- Imagem renderizada (PNG, 1080x1440px)

## Output Example

[Seguir o formato de Design System + HTML do best-practice image-design.md. Viewport 1080x1440, fontes minimas: Hero 58px, Heading 43px, Body 34px, Caption 24px.]

## Veto Conditions

Reject and redo if ANY are true:
1. Algum texto usa fonte menor que 34px para body ou 58px para hero
2. Slides nao seguem o mesmo design system (cores/fontes inconsistentes)
3. Imagem renderizada tem texto cortado ou ilegivel

## Quality Criteria

- [ ] Design system documentado antes dos slides
- [ ] Viewport exato de 1080x1440px
- [ ] Fontes respeitam minimos da plataforma
- [ ] Contraste WCAG AA (4.5:1) em todo texto
- [ ] HTML auto-contido (sem dependencias externas exceto Google Fonts)
- [ ] Cores alternam entre slides para ritmo visual
- [ ] Slide 1 verificado visualmente antes do batch
