# Task: Gerar Slides Completos via Nano Banana

## Task Config

```yaml
order: 1
```

## Objetivo

Gerar TODOS os slides do carrossel como imagens completas via Nano Banana (Google Gemini). Cada slide inclui texto, layout, dados e design — tudo renderizado como uma única imagem IA.

## Processo

### 1. Definir Design System (texto para prompts)

Antes de gerar qualquer slide, criar um bloco de texto `DESIGN_SYSTEM` que será incluído em TODOS os prompts para garantir consistência:

```
DESIGN_SYSTEM = """
DESIGN SYSTEM (apply consistently to ALL slides):
- Primary accent: #FF6600 (Riaworks Orange)
- Dark background: #0D0D0D (near black)
- Light background: #F5F5F5 (off white)
- Positive data: #28A745 (green)
- Negative data: #DC3545 (red)
- Font: Modern sans-serif (Inter for headings, Outfit for body style), clean, professional
- Header: "@your_handle" left, "[DATE]" right, subtle gray text
- Safe margins: 60px on all sides
- Fill ENTIRE 1080x1440 canvas — no empty areas
- Professional editorial/infographic style
"""
```

Criar também a regra de acentuação:

```
ACCENT_RULE = """
CRITICAL — Brazilian Portuguese accents:
All text MUST use correct PT-BR UTF-8 accents: ã, õ, é, ê, í, ó, ú, ç, à, â, ô.
Missing or incorrect accents are a BLOCKING ERROR.
Double-check every Portuguese word for correct diacritics.
Render all text clearly and legibly.
"""
```

### 2. Montar Prompts por Slide

Para cada slide do carrossel, criar um prompt detalhado contendo:

- **Dimensões:** "Create a 3:4 portrait image (1080x1440 pixels)"
- **Design system:** Incluir `DESIGN_SYSTEM` completo
- **Tipo de background:** Dark (#0D0D0D), Light (#F5F5F5) ou Accent (#FF6600)
- **Layout específico:** Descrever posição de cada elemento (headline no topo, cards no meio, fonte embaixo)
- **Texto exato:** Copiar o texto EXATO do conteúdo do carrossel, com todos os acentos
- **Elementos visuais:** Data cards, progress bars, numbered lists, comparison tables — descrever visualmente
- **Regra de acentuação:** Incluir `ACCENT_RULE`
- **Slide 1 especial:** "Position content in UPPER portion (top 50%)"

#### Exemplo de prompt para slide de dados:

```
Create a 3:4 portrait image (1080x1440 pixels) for an Instagram carousel slide.

DESIGN SYSTEM:
[incluir DESIGN_SYSTEM]

BACKGROUND: #0D0D0D (dark)

LAYOUT:
- Header at top: "@your_handle" left, "31.03.2026" right, gray (#777)
- Bold white headline below header
- 4 data cards in 2x2 grid (red border for negative, green border for positive)
- Each card: label on top (gray), large number (colored), sub-label below
- Insight callout box with orange border at bottom
- Source citation in small gray text at very bottom
- Fill the ENTIRE canvas top to bottom

EXACT TEXT TO RENDER:
- Headline: "Se você tem entre 22 e 25 anos, já está sentindo o impacto."
- Card 1: label "Jovens 22-25 anos", number "-16%", sub "emprego em áreas IA" (red)
- Card 2: label "Experientes 30+", number "+6% a +12%", sub "crescimento" (green)
- Card 3: label "Vagas automatizáveis", number "-13%", sub "pós-ChatGPT" (red)
- Card 4: label "Vagas analíticas/criativas", number "+20%", sub "crescimento" (green)
- Callout: "A IA não elimina todos os empregos. Elimina os de entrada."
- Source: "Fonte: Stanford Digital Economy Lab, 2024"

[incluir ACCENT_RULE]
Professional infographic design. High contrast. Bold numbers. Clean layout.
```

### 3. Gerar Slides via Script Python

Criar um script `generate_slides.py` que:

```python
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os, json, base64, time, urllib.request

# API config
GEMINI_API_KEY = os.environ.get("GEMINI_API_KEY")
if not GEMINI_API_KEY:
    with open(".env") as f:
        for line in f:
            if line.startswith("GEMINI_API_KEY="):
                GEMINI_API_KEY = line.split("=", 1)[1].strip()
                break

API_URL = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-3.1-flash-image-preview:generateContent?key={GEMINI_API_KEY}"
OUTPUT_DIR = "[output path]/carousel-slides/png"
os.makedirs(OUTPUT_DIR, exist_ok=True)

def generate(prompt, output_path, retries=2):
    payload = json.dumps({
        "contents": [{"parts": [{"text": prompt}]}],
        "generationConfig": {"responseModalities": ["TEXT", "IMAGE"]}
    }).encode()
    for attempt in range(retries + 1):
        try:
            req = urllib.request.Request(API_URL, data=payload,
                headers={"Content-Type": "application/json"})
            resp = urllib.request.urlopen(req, timeout=120)
            data = json.loads(resp.read())
            for p in data.get("candidates", [{}])[0].get("content", {}).get("parts", []):
                if "inlineData" in p:
                    img = base64.b64decode(p["inlineData"]["data"])
                    with open(output_path, "wb") as f:
                        f.write(img)
                    print(f"  ✓ {output_path} ({len(img)//1024}KB)")
                    return True
            print(f"  ✗ No image in response")
        except Exception as e:
            print(f"  ✗ Error: {e}")
        if attempt < retries:
            time.sleep(5)
    return False

# Define all slide prompts
SLIDES = [
    {"num": 1, "prompt": "..."},
    {"num": 2, "prompt": "..."},
    # ... all slides
]

for slide in SLIDES:
    path = os.path.join(OUTPUT_DIR, f"slide-{slide['num']:02d}.png")
    print(f"\nSlide {slide['num']}...")
    if not generate(slide["prompt"], path):
        print(f"  FALHOU — verificar manualmente")
    time.sleep(3)
```

### 4. Verificação (OBRIGATÓRIO)

Após gerar todos os slides, verificar CADA um:

- [ ] Acentuação PT-BR correta em todos os textos
- [ ] Todo texto legível (não borrado, não cortado)
- [ ] Área 1080x1440 totalmente preenchida
- [ ] Números e dados corretos
- [ ] Cores consistentes com design system
- [ ] Estilo visual consistente entre todos os slides
- [ ] Slide 1 com conteúdo no topo

Para slides que falharem na verificação:
1. Identificar o problema
2. Ajustar o prompt (ser mais específico sobre o erro)
3. Regenerar o slide individual
4. Verificar novamente

### 5. Conversão para JPEG (para publicação)

Instagram aceita JPEG. Converter PNGs para JPEG com qualidade 92:

```python
from PIL import Image
for png in sorted(os.listdir(PNG_DIR)):
    if png.endswith('.png'):
        img = Image.open(os.path.join(PNG_DIR, png)).convert('RGB')
        img.save(os.path.join(JPEG_DIR, png.replace('.png', '.jpg')), 'JPEG', quality=92)
```

## Formato de Entrega

```
output/
  [run-id]/
    generate_slides.py       # Script de geração
    carousel-slides/
      png/
        slide-01.png          # Slides gerados pelo Gemini
        slide-02.png
        ...
      jpeg/
        slide-01.jpg          # Versão JPEG para publicação
        slide-02.jpg
        ...
```

## Critérios de Conclusão

- Todos os slides gerados via Nano Banana (Gemini)
- Script Python de geração criado e funcional
- Acentuação PT-BR verificada em todos os slides
- Todos os slides preenchem 100% da área
- Consistência visual entre todos os slides
- Slide 1 com conteúdo no topo
- PNGs e JPEGs salvos no diretório correto
- Máximo 10 slides
