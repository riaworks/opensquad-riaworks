---
name: nano-banana
description: >
  Generates complete Instagram carousel slides via Google Gemini (Nano Banana 2) API.
  Creates full slides with text, layout, data visualizations, and design — all rendered
  as a single AI-generated image. Also supports background-only generation.
description_pt-BR: >
  Gera slides completos de carrossel Instagram via Google Gemini (Nano Banana 2) API.
  Cria slides inteiros com texto, layout, visualizações de dados e design — tudo
  renderizado como uma única imagem gerada por IA. Também suporta geração apenas de backgrounds.
type: native
version: "3.0.0"
categories: [design, ai, images, generation]
requires:
  env:
    - GEMINI_API_KEY
---

# Nano Banana — AI Slide & Image Generator

## When to use

Use this skill to generate **slides completos** para carrosséis Instagram — incluindo texto, layout, dados e elementos visuais — tudo como uma única imagem IA. Este é o modo principal de criação de slides.

**Usar para:**
- Geração de slides completos (texto + design + layout) para carrossel Instagram
- Cover slides com imagens cinematográficas e texto integrado
- Slides de dados com números, gráficos e visualizações
- Slides de CTA com branding integrado
- Backgrounds cinematográficos (modo legado)

**NÃO usar para:** renderizar HTML existente (use `image-creator`), buscar imagens da web (use `image-fetcher`).

## Instructions

### API Configuration

- **Model**: `gemini-3.1-flash-image-preview` (Nano Banana 2 — melhor para texto em imagens)
- **API Key**: Environment variable `GEMINI_API_KEY`
- **Cost**: ~$0.02 per image
- **Output**: PNG image (base64 encoded in API response)
- **Timeout**: Mínimo 90000ms (90 segundos) — geração leva 15-60s

### How to Generate a Slide

Use um script Python para gerar cada slide. **NUNCA use curl direto no bash** — o output base64 é grande demais.

**IMPORTANTE — Logo como input:** O logo da marca (`materiais/logomarca.png`) DEVE ser enviado como `inline_data` no request junto com o prompt de texto. Isso permite que o Gemini aplique o logo EXATO no slide, sem redesenhar. No prompt, instruir: "Use the attached logo exactly as-is in the top-left corner (~120px wide)."

```python
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import json, base64, os, urllib.request

GEMINI_API_KEY = os.environ.get("GEMINI_API_KEY") or open(".env").read().split("GEMINI_API_KEY=")[1].split("\n")[0]
API_URL = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-3.1-flash-image-preview:generateContent?key={GEMINI_API_KEY}"

# Load logo as base64 to send with every request
with open("materiais/logomarca.png", "rb") as f:
    LOGO_B64 = base64.b64encode(f.read()).decode()

def generate_slide(prompt, output_path, retries=2):
    """Generate a complete slide image from prompt. Sends logo as inline_data."""
    payload = json.dumps({
        "contents": [{"parts": [
            {"inline_data": {"mime_type": "image/png", "data": LOGO_B64}},
            {"text": prompt}
        ]}],
        "generationConfig": {"responseModalities": ["TEXT", "IMAGE"]}
    }).encode()

    for attempt in range(retries + 1):
        try:
            req = urllib.request.Request(API_URL, data=payload, headers={"Content-Type": "application/json"})
            resp = urllib.request.urlopen(req, timeout=120)
            data = json.loads(resp.read())
            parts = data.get("candidates", [{}])[0].get("content", {}).get("parts", [])
            for p in parts:
                if "inlineData" in p:
                    img = base64.b64decode(p["inlineData"]["data"])
                    with open(output_path, "wb") as f:
                        f.write(img)
                    print(f"  Saved: {output_path} ({len(img)//1024}KB)")
                    return True
            print(f"  No image in response, retrying...")
        except Exception as e:
            print(f"  Error: {e}")
            if attempt < retries:
                import time; time.sleep(5)
    return False
```

### Modo Full Slide (PRINCIPAL)

Neste modo, o Gemini gera o slide **completo** — texto, layout, cores, dados, tudo integrado na imagem.

#### Regras obrigatórias para prompts de slides completos

1. **Português BR com acentuação perfeita (BLOQUEANTE):**
   - Todo texto no prompt DEVE estar com acentuação correta: ã, õ, é, ê, í, ó, ú, ç, à, â, ô
   - Incluir instrução explícita: "All text MUST be in Brazilian Portuguese with correct UTF-8 accents (ã, õ, é, ê, í, ó, ú, ç, à, â, ô). Missing accents are a blocking error."
   - Verificar CADA slide gerado para acentuação correta. Se errado, regenerar.

2. **Aspecto e dimensões:**
   - "Create a 3:4 portrait image (1080x1440 pixels)"
   - "Fill the ENTIRE canvas — no empty areas, but with elegant spacing between elements"

3. **Texto exato no prompt:**
   - Fornecer o texto EXATO que deve aparecer no slide, entre aspas
   - Especificar hierarquia: "headline in semibold text", "body in regular weight", "caption in small light text"
   - Especificar posicionamento: "headline at the top", "data cards in the middle", "source at the bottom"

4. **Design system no prompt:**
   - Sempre incluir as cores exatas: "#FF6600 orange accent", "#0D0D0D dark background", "#F5F5F5 light background"
   - Especificar estilo de fonte: "clean geometric sans-serif (Inter for headings, Outfit for body)"
   - Especificar peso: "semibold headings (600 weight), regular body (400 weight), bold (700) ONLY for hero numbers and key emphasis"

5. **Preencher toda a área com espaçamento elegante:**
   - "Fill the entire 1080x1440 canvas with content"
   - "Use generous spacing between sections (48-60px gaps)"
   - "Content should extend from top to bottom with refined breathing room"

6. **Consistência entre slides:**
   - Usar o MESMO design system description em todos os prompts do carrossel
   - Manter padrão de cores consistente (alternância dark/light/accent)
   - Mesma família tipográfica descrita em cada prompt

7. **Header com branding (logo + @your_handle):**
   - Incluir no prompt: "Small header at top: orange Riaworks logo (small 3D cube icon in orange/gray + 'RIAworks' wordmark, ~120px wide) on the left, '@your_handle' in small subtle gray next to it, and date 'DD.MM.YYYY' on the right in subtle gray"
   - Para slides CTA: usar logo centralizado no topo, sem header lateral

8. **Slide 1 (Cover) — conteúdo no topo:**
   - "Position the headline and main content in the UPPER portion of the image (top 60%)"
   - Motivo: preview do WhatsApp corta em quadrado 1080x1080 a partir do topo

### Prompt Template — Full Slide

```
Create a 3:4 portrait image (1080x1440 pixels) for an Instagram carousel slide.

DESIGN SYSTEM:
- Background: [#0D0D0D dark / #F5F5F5 light / #FF6600 orange accent]
- Accent color: #FF6600 (Riaworks Orange)
- Typography: Clean geometric sans-serif (Inter for headings, Outfit for body). Refined, editorial, NOT aggressive.
- Font weights: Semibold (600) for headings, Regular (400) to Medium (500) for body, Bold (700) ONLY for hero numbers and key emphasis. Never Black/800/900.
- Text colors: [#FFFFFF white on dark / #1A1A2E dark on light / as specified]
- Style: Sophisticated editorial design. Sober, refined aesthetic. Emphasis through scale and spacing, not weight.
- Spacing: generous gaps between sections (48-60px), breathing room between elements (24-32px)

LAYOUT:
- Small header at top: orange Riaworks logo (3D cube icon in orange/gray + 'RIAworks' wordmark, ~120px) on left, "@your_handle" in small gray (#777) next to it, "[DATE]" on right in gray
- [Describe the specific layout: headline position, data cards, body text areas, etc.]
- Fill the ENTIRE 1080x1440 canvas with elegant spacing — no large empty areas
- 60px safe margins on all sides

CONTENT (exact text to render):
- Headline: "[EXACT HEADLINE TEXT WITH ACCENTS]"
- Body: "[EXACT BODY TEXT WITH ACCENTS]"
- Data: "[EXACT NUMBERS AND LABELS]"
- Source: "[EXACT SOURCE TEXT]"

All text MUST be in Brazilian Portuguese with correct UTF-8 accents (ã, õ, é, ê, í, ó, ú, ç, à, â, ô). Missing accents are a blocking error.
Render all text clearly and legibly — typography is a critical part of this image.
Sophisticated editorial design. Refined, sober aesthetic. Clean geometric typography with generous spacing.
```

### Prompt Templates por Tipo de Slide

#### Cover (Slide 1) — Dark + Image Background
```
Create a 3:4 portrait image (1080x1440 pixels) for an Instagram carousel COVER slide.

DESIGN SYSTEM:
- Background: Cinematic dark scene with [describe visual metaphor]
- Dark overlay gradient ensuring text readability
- Accent color: #FF6600 (Riaworks Orange)
- Typography: Clean geometric sans-serif (Inter/Outfit), semibold for headline, regular for body. White text with subtle shadow.

LAYOUT:
- Small header at top: orange Riaworks logo (3D cube icon in orange/gray + 'RIAworks' wordmark) on left, "@your_handle" in small gray, "[DATE]" on right
- HEADLINE positioned in the UPPER portion (top 50% of image) — semibold, not overly large
- Supporting text below headline — regular weight, lighter color, generous line spacing
- Data highlight cards in the lower-middle area with subtle borders
- Fill the ENTIRE canvas — cinematic image covers full background

CONTENT (exact text):
- Headline: "[EXACT TEXT]"
- Subtitle: "[EXACT TEXT]"
- Data cards: [list exact numbers and labels]

All text in Brazilian Portuguese with correct accents (ã, õ, é, ê, í, ó, ú, ç, à, â, ô).
Cinematic, atmospheric lighting. Sophisticated editorial design. Refined, not aggressive.
```

#### Data Slide — Dark Background
```
Create a 3:4 portrait image (1080x1440 pixels) for an Instagram carousel DATA slide.

DESIGN SYSTEM:
- Background: #0D0D0D (near black)
- Accent: #FF6600 (orange) for highlights, #28A745 (green) for positive, #DC3545 (red) for negative
- Typography: Geometric sans-serif (Inter/Outfit), refined weights

LAYOUT:
- Small header: Riaworks logo + "@your_handle" + date
- Semibold headline at top (not overly bold)
- Data visualization cards with generous spacing (subtle borders, clear numbers)
- Key insight callout box
- Source citation at bottom
- Fill the ENTIRE canvas with elegant spacing

CONTENT (exact text):
[provide all text, numbers, labels, sources]

All text in Brazilian Portuguese with correct accents. Clear, well-spaced numbers. Sophisticated editorial infographic.
```

#### Accent Slide — Orange Background
```
Create a 3:4 portrait image (1080x1440 pixels) for an Instagram carousel slide.

DESIGN SYSTEM:
- Background: #FF6600 (vibrant orange)
- Text: #0D0D0D (dark) for headlines, #FFFFFF (white) for emphasis
- Semi-transparent dark cards for content sections
- Typography: Geometric sans-serif, refined weights

LAYOUT:
- Small header: Riaworks logo + "@your_handle" + date in dark brown
- Semibold headline at top
- Comparison cards or numbered list with generous spacing
- Key quote/callout at bottom
- Fill the ENTIRE canvas with elegant spacing

CONTENT (exact text):
[provide all text]

All text in Brazilian Portuguese with correct accents.
Sophisticated editorial design on orange background.
```

#### CTA Slide (Last) — Dark, Centered
```
Create a 3:4 portrait image (1080x1440 pixels) for an Instagram carousel CTA (call-to-action) slide.

DESIGN SYSTEM:
- Background: #0D0D0D (dark)
- Accent: #FF6600 (orange) for CTA button
- Centered layout, elegant spacing

LAYOUT:
- Orange Riaworks logo (3D cube icon in orange/gray + 'RIAworks' wordmark) centered at top
- Semibold headline centered with generous line spacing
- Supporting text below in regular weight, lighter color
- Orange CTA button: "Segue @your_handle" with rounded corners and subtle glow
- Small text below button
- Vertically centered content with balanced spacing

CONTENT (exact text):
[provide all text]

All text in Brazilian Portuguese with correct accents.
Sophisticated, clean, refined CTA design.
```

### Verificação Pós-Geração (OBRIGATÓRIO)

Após gerar cada slide, verificar visualmente:

1. **Acentuação PT-BR:** Todos os acentos estão corretos? (ã, õ, é, ç, etc.)
2. **Texto legível:** Todo texto está legível e não cortado?
3. **Área preenchida:** O slide usa toda a área 1080x1440 com espaçamento elegante?
4. **Dados corretos:** Números e percentuais estão renderizados corretamente?
5. **Consistência:** O estilo visual é consistente com os outros slides do carrossel?
6. **Logo + handle:** O logo Riaworks e @your_handle aparecem no header?
7. **Tipografia sóbria:** As fontes são refinadas, não agressivas/pesadas?

**Se qualquer item falhar, regenerar o slide** com prompt ajustado.

### Batch Generation Script Template

```python
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Generate all carousel slides via Nano Banana 2 (Gemini)."""
import os, json, base64, time, urllib.request

# Config
GEMINI_API_KEY = os.environ.get("GEMINI_API_KEY") or open(".env").read().split("GEMINI_API_KEY=")[1].split("\n")[0].strip()
API_URL = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-3.1-flash-image-preview:generateContent?key={GEMINI_API_KEY}"
OUTPUT_DIR = "slides/png"
os.makedirs(OUTPUT_DIR, exist_ok=True)

# Load logo to send with every request
with open("materiais/logomarca.png", "rb") as f:
    LOGO_B64 = base64.b64encode(f.read()).decode()

DESIGN_SYSTEM = """
DESIGN SYSTEM (apply consistently to ALL slides):
- Accent: [YOUR_ACCENT_COLOR] (e.g. #FF6600 Orange)
- Dark bg: #0D0D0D, Light bg: #F5F5F5
- Positive: #28A745, Negative: #DC3545
- Typography: Clean geometric sans-serif (Inter for headings, Outfit for body). Refined, editorial, NOT aggressive or heavy.
- Font weights: Semibold (600) for headings, Regular (400) to Medium (500) for body, Bold (700) ONLY for hero numbers. Never Black/800/900.
- Header: Your logo (attached as image) left, "@your_handle" small gray, "DD.MM.YYYY" right gray
- Safe margins: 60px all sides
- Section gaps: 48-60px, element gaps: 24-32px
- Fill ENTIRE 1080x1440 canvas with elegant spacing
- Style: Sophisticated editorial, sober, refined. NOT aggressive infographic.
"""

ACCENT_RULE = """
CRITICAL — Brazilian Portuguese accents (BLOCKING RULE):
All text MUST use correct PT-BR UTF-8 accents: ã, õ, é, ê, í, ó, ú, ç, à, â, ô.
Missing or wrong accents are a BLOCKING ERROR. Double-check every word.
Render all text clearly — refined typography is a critical design element.
"""

# Define prompts for each slide
SLIDES = [
    {
        "num": 1,
        "prompt": f"""Create a 3:4 portrait image (1080x1440 pixels) for an Instagram carousel COVER.
{DESIGN_SYSTEM}
LAYOUT: [describe layout]
CONTENT: [exact text]
{ACCENT_RULE}"""
    },
    # ... repeat for slides 2-9
]

def generate_slide(prompt, output_path, retries=2):
    payload = json.dumps({
        "contents": [{"parts": [
            {"inline_data": {"mime_type": "image/png", "data": LOGO_B64}},
            {"text": prompt}
        ]}],
        "generationConfig": {"responseModalities": ["TEXT", "IMAGE"]}
    }).encode()
    for attempt in range(retries + 1):
        try:
            req = urllib.request.Request(API_URL, data=payload, headers={"Content-Type": "application/json"})
            resp = urllib.request.urlopen(req, timeout=120)
            data = json.loads(resp.read())
            for p in data.get("candidates",[{}])[0].get("content",{}).get("parts",[]):
                if "inlineData" in p:
                    img = base64.b64decode(p["inlineData"]["data"])
                    with open(output_path, "wb") as f:
                        f.write(img)
                    return True
        except Exception as e:
            print(f"  Error: {e}")
            if attempt < retries:
                time.sleep(5)
    return False

# Generate all slides
for slide in SLIDES:
    path = os.path.join(OUTPUT_DIR, f"slide-{slide['num']:02d}.png")
    print(f"Generating slide {slide['num']}...")
    generate_slide(slide["prompt"], path)
    time.sleep(3)  # rate limit
```

### Modo Background-Only (Legado)

Para gerar apenas imagens de fundo (sem texto), usar os templates antigos com a instrução "No text, no letters, no words in the image". Útil quando o slide será montado via HTML/CSS com overlay.

### Error Handling

- **429 Too Many Requests**: Aguardar 30s e retry. Free tier tem rate limits.
- **400 Invalid Argument**: Verificar que `responseModalities` inclui `["TEXT", "IMAGE"]`.
- **Safety filter**: Se bloqueado, reformular o prompt para ser menos ambíguo.
- **Texto errado/sem acentos**: Regenerar com prompt mais enfático sobre o texto exato.
- **Imagem não gerada**: Verificar se a resposta contém `inlineData`. Retry se necessário.

## Available Operations

- **Generate full slide** — Criar slide completo com texto, layout e design integrados (MODO PRINCIPAL)
- **Generate slide background** — Criar background cinematográfico para overlay HTML (modo legado)
- **Batch generate carousel** — Gerar todos os slides de um carrossel sequencialmente
- **Verify and regenerate** — Verificar acentuação/qualidade e regenerar slides com problemas
