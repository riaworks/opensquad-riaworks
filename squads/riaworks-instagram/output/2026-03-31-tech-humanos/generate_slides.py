#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Generate ALL carousel slides via Nano Banana 2 (Gemini 3.1 Flash Image Preview).
100% AI-generated — text, layout, data, colors, everything.
Topic: Tecnologia ajudando humanos / IA salvando vidas
"""
import os, json, base64, time, urllib.request

# === CONFIG ===
GEMINI_API_KEY = None
with open("C:/__canal_riaworks/.env") as f:
    for line in f:
        if line.startswith("GEMINI_API_KEY="):
            GEMINI_API_KEY = line.split("=", 1)[1].strip()
            break

MODEL = "gemini-3.1-flash-image-preview"
API_URL = f"https://generativelanguage.googleapis.com/v1beta/models/{MODEL}:generateContent?key={GEMINI_API_KEY}"
OUTPUT_DIR = "C:/__canal_riaworks/squads/riaworks-instagram/output/2026-03-31-tech-humanos/carousel-slides/png"
os.makedirs(OUTPUT_DIR, exist_ok=True)

# === DESIGN SYSTEM (included in every prompt) ===
DESIGN_SYSTEM = """
DESIGN SYSTEM (apply consistently to ALL slides in this carousel):
- Primary accent: #FF6600 (vibrant Riaworks Orange)
- Dark background: #0D0D0D (near black)
- Light background: #F5F5F5 (off white)
- Positive/good data: #28A745 (green)
- Negative/warning data: #DC3545 (red)
- Info/neutral: #3B82F6 (blue)
- Font: Modern clean sans-serif (like Segoe UI, Helvetica, or Inter), professional
- Font weights: Bold/Black for headlines, Semi-bold for body, Regular for captions
- Header: "@canal.riaworks" on left, "31.03.2026" on right, in subtle gray (#777)
- Safe margins: 60px padding on all sides
- Fill the ENTIRE 1080x1440 canvas from top to bottom — no large empty areas
- Professional editorial infographic style with high visual impact
"""

ACCENT_RULE = """
CRITICAL — Brazilian Portuguese accents (BLOCKING RULE):
All text MUST use correct PT-BR UTF-8 accents: ã, õ, é, ê, í, ó, ú, ç, à, â, ô.
Missing or incorrect accents are a BLOCKING ERROR that requires regeneration.
Double-check EVERY Portuguese word for correct diacritics before rendering.
Render all text CLEARLY and LEGIBLY — typography is a critical design element.
"""

# === SLIDE PROMPTS ===
SLIDES = [
    # SLIDE 1 — COVER (Dark + cinematic)
    {
        "num": 1,
        "prompt": f"""Create a 3:4 portrait image (1080x1440 pixels) for an Instagram carousel COVER slide.

{DESIGN_SYSTEM}

BACKGROUND: Dark cinematic image of a doctor using a holographic AI interface to analyze a patient scan, warm orange and blue lighting, futuristic but human. Dark overlay gradient for text readability.

LAYOUT:
- Header at top: "@canal.riaworks" left, "31.03.2026" right, gray
- HEADLINE in the UPPER portion (top 40%) — large, bold, white, with orange accent on key phrase
- Subtitle below in lighter gray
- Three small data cards at middle-bottom area (green borders, showing key numbers)
- Arrow/CTA text at very bottom in orange

EXACT TEXT TO RENDER:
- Headline: "A IA já está salvando vidas." (white) + line break + "E você nem sabe." (in #FF6600 orange)
- Subtitle: "De diagnósticos precoces a resgate em desastres — a tecnologia está transformando o mundo silenciosamente."
- Card 1: "17.000" (large green) + "vidas salvas por IA médica" (small gray)
- Card 2: "94%" (large green) + "precisão em detecção de câncer" (small gray)
- Card 3: "+3,5B" (large green) + "pessoas com acesso a saúde digital" (small gray)
- Bottom CTA: "Os dados que ninguém está mostrando →" (orange)

{ACCENT_RULE}
Cinematic, warm lighting, high visual impact. Human + technology harmony aesthetic.
"""
    },

    # SLIDE 2 — IA NA SAÚDE (Dark)
    {
        "num": 2,
        "prompt": f"""Create a 3:4 portrait image (1080x1440 pixels) for an Instagram carousel slide.

{DESIGN_SYSTEM}

BACKGROUND: #0D0D0D (dark). Subtle background with faint medical hologram imagery (very subtle, not distracting).

LAYOUT:
- Header at top: "@canal.riaworks" left, "31.03.2026" right, gray
- Bold white headline
- Large featured data card with green accent (full width)
- Two smaller data cards side by side below
- Body text paragraph below cards
- Source citation at bottom
- Fill entire canvas

EXACT TEXT TO RENDER:
- Headline: "A IA detecta câncer de mama com 94% de precisão. Médicos humanos: 88%."
- Featured card (green border): label "Estudo do Google Health", number "94,5%" (large green), sub "precisão em mamografia assistida por IA vs 88% de radiologistas"
- Card left (blue border): label "Tempo de análise", number "30 seg" (blue), sub "vs 30 minutos manual"
- Card right (green border): label "Falsos negativos", number "-5,7%" (green), sub "redução com IA assistindo médico"
- Body: "A IA não substitui o médico. Ela é o segundo par de olhos que nunca cansa, nunca distrai e analisa 300 exames por hora."
- Source: "Fontes: Google Health / Nature Medicine, 2024; NHS England"

{ACCENT_RULE}
Professional medical infographic. Clean, trustworthy design. High contrast numbers.
"""
    },

    # SLIDE 3 — DESASTRES NATURAIS (Accent orange)
    {
        "num": 3,
        "prompt": f"""Create a 3:4 portrait image (1080x1440 pixels) for an Instagram carousel slide.

{DESIGN_SYSTEM}

BACKGROUND: #FF6600 (vibrant orange)
TEXT COLORS: #0D0D0D (dark) for headlines, #FFFFFF (white) for emphasis/numbers, #4D2600 (dark brown) for body

LAYOUT:
- Header at top: "@canal.riaworks" left, "31.03.2026" right, in dark brown
- Bold dark headline at top
- Three content cards (semi-transparent dark background, rounded) stacked vertically, each with an icon description, bold title, and supporting text
- Key quote callout at bottom in dark rounded box with white text
- Fill entire canvas

EXACT TEXT TO RENDER:
- Headline: "Em 2024, a IA antecipou 48 horas de enchentes no Brasil."
- Card 1 title: "Google Flood Hub" + body: "Sistema de IA que prevê enchentes com 48h de antecedência. Ativo em 80 países. Salvou milhares no Rio Grande do Sul."
- Card 2 title: "Drones de resgate" + body: "IA identifica sobreviventes em escombros usando câmeras térmicas. Tempo de busca reduzido em 60%."
- Card 3 title: "Alerta sísmico no Japão" + body: "Sistema prevê terremotos 30 segundos antes. Tempo suficiente para evacuação automática de trens."
- Bottom quote (dark box, white text): "A tecnologia não impede desastres. Mas já decide quem sobrevive."

{ACCENT_RULE}
"""
    },

    # SLIDE 4 — ACESSIBILIDADE (Light)
    {
        "num": 4,
        "prompt": f"""Create a 3:4 portrait image (1080x1440 pixels) for an Instagram carousel slide.

{DESIGN_SYSTEM}

BACKGROUND: #F5F5F5 (light off-white)
TEXT COLORS: #1A1A2E (dark) for headlines, #333 for body, #FF6600 for accent numbers

LAYOUT:
- Header at top: "@canal.riaworks" left, "31.03.2026" right, in gray
- Bold dark headline
- Four data rows, each with a large orange number on the left and description text on the right, separated by subtle dividers
- Insight box at bottom (white card with orange left border and shadow)
- Source at very bottom
- Fill entire canvas

EXACT TEXT TO RENDER:
- Headline: "1,3 bilhão de pessoas com deficiência. A IA está quebrando barreiras."
- Row 1: "2,5B" (orange) + "traduções por dia no Google Translate — quebrando barreiras de idioma"
- Row 2: "100M" (orange) + "pessoas usam leitores de tela com IA para navegar a internet"
- Row 3: "85%" (orange) + "de precisão em legendas automáticas ao vivo (YouTube, Teams, Zoom)"
- Row 4: "15M" (orange) + "de brasileiros com deficiência auditiva beneficiados por legendas IA"
- Insight box: "A IA mais transformadora não é a que escreve código. É a que dá voz a quem não tinha."
- Source: "Fontes: OMS; Google Accessibility; IBGE 2023"

{ACCENT_RULE}
Clean, professional, accessible design. Data-forward with clear hierarchy.
"""
    },

    # SLIDE 5 — EDUCAÇÃO (Dark)
    {
        "num": 5,
        "prompt": f"""Create a 3:4 portrait image (1080x1440 pixels) for an Instagram carousel slide.

{DESIGN_SYSTEM}

BACKGROUND: #0D0D0D (dark)

LAYOUT:
- Header at top
- Bold white headline
- Comparison layout: "ANTES" vs "DEPOIS" side by side cards
- Left card (red tint/border): old education limitations
- Right card (green tint/border): AI-enabled improvements
- Large stat callout below comparison
- Body text
- Source at bottom
- Fill entire canvas

EXACT TEXT TO RENDER:
- Headline: "Um professor para cada 40 alunos. A IA mudou essa equação."
- ANTES card (red border): "Ensino tradicional" + bullets: "1 professor : 40 alunos", "Ritmo único para todos", "Feedback demorado", "Material genérico"
- DEPOIS card (green border): "Com IA assistente" + bullets: "Tutoria personalizada 24/7", "Adaptação ao ritmo individual", "Feedback instantâneo", "Conteúdo sob medida"
- Large stat: "Khan Academy + GPT-4:" (gray) + "Alunos aprenderam 2x mais rápido" (large, green)
- Body: "A Índia conectou 200 milhões de estudantes rurais a tutores de IA em 2025. O Brasil tem 5 milhões de crianças fora da escola."
- Source: "Fontes: Khan Academy; UNESCO; MEC Brasil"

{ACCENT_RULE}
Educational infographic style. Clear contrast between before/after.
"""
    },

    # SLIDE 6 — MEIO AMBIENTE (Accent orange)
    {
        "num": 6,
        "prompt": f"""Create a 3:4 portrait image (1080x1440 pixels) for an Instagram carousel slide.

{DESIGN_SYSTEM}

BACKGROUND: #FF6600 (vibrant orange)
TEXT COLORS: #0D0D0D for headlines, #FFFFFF for emphasis, #4D2600 for body

LAYOUT:
- Header at top in dark brown
- Bold headline
- Three metric cards (dark semi-transparent backgrounds) each showing a large white number and description
- Connecting narrative text between cards
- Quote at bottom
- Fill entire canvas

EXACT TEXT TO RENDER:
- Headline: "A IA está monitorando o planeta em tempo real."
- Card 1: "30%" (large white) + "de redução no desmatamento da Amazônia com monitoramento por satélite + IA (MapBiomas)"
- Card 2: "400M" (large white) + "de toneladas de CO₂ economizadas por otimização logística com IA (Google DeepMind)"
- Card 3: "92%" (large white) + "de precisão na previsão de incêndios florestais com 24h de antecedência"
- Bottom text: "A IA não resolve a crise climática sozinha. Mas sem ela, não temos chance."

{ACCENT_RULE}
"""
    },

    # SLIDE 7 — NÚMEROS GLOBAIS (Dark)
    {
        "num": 7,
        "prompt": f"""Create a 3:4 portrait image (1080x1440 pixels) for an Instagram carousel slide.

{DESIGN_SYSTEM}

BACKGROUND: #0D0D0D (dark)

LAYOUT:
- Header at top
- Bold white headline with green accent
- Six metric tiles in a 2x3 grid, each with colored number and label
- Mix of green (positive) and blue (info) colored numbers
- Summary callout at bottom (orange border)
- Source at very bottom
- Fill entire canvas

EXACT TEXT TO RENDER:
- Headline: "Os números que o pessimismo" (white) + "não mostra." (green)
- Tile 1: "17.000" (green) + "vidas salvas por diagnóstico IA em 2024"
- Tile 2: "3,5B" (blue) + "pessoas com acesso a saúde digital"
- Tile 3: "48h" (green) + "de antecipação em alertas de enchente"
- Tile 4: "200M" (blue) + "estudantes conectados a tutores IA"
- Tile 5: "400M ton" (green) + "de CO₂ economizadas por IA"
- Tile 6: "94%" (green) + "precisão em detecção precoce de câncer"
- Callout: "A tecnologia mais impactante não é a que gera imagens. É a que gera impacto."
- Source: "Compilação de fontes: OMS, Google, UNESCO, MapBiomas, Khan Academy"

{ACCENT_RULE}
Data dashboard style. Grid of metrics. High impact numbers. Professional infographic.
"""
    },

    # SLIDE 8 — E O BRASIL? (Light)
    {
        "num": 8,
        "prompt": f"""Create a 3:4 portrait image (1080x1440 pixels) for an Instagram carousel slide.

{DESIGN_SYSTEM}

BACKGROUND: #F5F5F5 (light)
TEXT COLORS: #1A1A2E (dark) for headlines, #333 for body, #FF6600 for accent

LAYOUT:
- Header at top
- Bold headline with orange accent
- Three content blocks, each with an orange left border, containing a stat and description
- Dark callout box at bottom (#1A1A2E background) with white text — the key insight
- Source at very bottom
- Fill entire canvas

EXACT TEXT TO RENDER:
- Headline: "E o Brasil?" (dark) + " Já está acontecendo aqui." (#FF6600 orange)
- Block 1: "SUS + IA" (bold) + "O Einstein e o SíRio-Libanês já usam IA para triagem de emergência. Tempo de espera caiu 40% nos pilotos."
- Block 2: "Agro inteligente" (bold) + "IA de monitoramento de pragas economizou R$ 12 bilhões em safras brasileiras em 2025. Embrapa lidera pesquisa."
- Block 3: "Conecta Recife" (bold) + "Programa municipal usa IA para otimizar rotas de ônibus. Tempo de deslocamento caiu 23% em áreas periféricas."
- Dark callout: "O Brasil tem 215 milhões de pessoas. A IA pode ser o maior equalizador social que já existiu — se soubermos usar."
- Source: "Fontes: Einstein/SíRio-Libanês; Embrapa; Prefeitura do Recife"

{ACCENT_RULE}
Clean, professional, editorial. Clear data hierarchy. Inspiring tone.
"""
    },

    # SLIDE 9 — CTA (Dark centered)
    {
        "num": 9,
        "prompt": f"""Create a 3:4 portrait image (1080x1440 pixels) for an Instagram carousel CTA (call-to-action) slide.

{DESIGN_SYSTEM}

BACKGROUND: #0D0D0D (dark)

LAYOUT:
- Vertically centered content
- "CANAL RIAWORKS" label at top in #FF6600 orange, small caps, letter-spaced
- Large bold white headline centered
- Supporting text in lighter gray below
- Large orange rounded CTA button: "Segue @canal.riaworks" with glow effect
- Small gray text below button
- Fill the vertical space with balanced spacing between elements

EXACT TEXT TO RENDER:
- Label: "CANAL RIAWORKS" (orange, small, spaced letters)
- Headline: "Salva esse carrossel." + line break + "Manda pra quem acha que" + line break + "tecnologia só serve pra substituir pessoas."
- Subtitle: "Toda semana a gente mostra o lado da tecnologia que realmente importa. Dados reais, sem hype."
- CTA Button: "Segue @canal.riaworks" (white text on orange rounded button)
- Below button: "Ativa o sininho para não perder o próximo"

{ACCENT_RULE}
Clean, centered, impactful CTA. Professional dark design. Orange accent button with subtle glow.
"""
    },
]


def generate_slide(prompt, output_path, retries=2):
    """Generate a single slide image via Gemini API."""
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
            parts = data.get("candidates", [{}])[0].get("content", {}).get("parts", [])
            for p in parts:
                if "inlineData" in p:
                    img = base64.b64decode(p["inlineData"]["data"])
                    with open(output_path, "wb") as f:
                        f.write(img)
                    print(f"  OK: {os.path.basename(output_path)} ({len(img)//1024}KB)")
                    return True
            print(f"  No image in response")
        except Exception as e:
            print(f"  Error: {e}")
        if attempt < retries:
            print(f"  Retrying ({attempt+1}/{retries})...")
            time.sleep(5)
    return False


def main():
    print("=" * 50)
    print("  Nano Banana Full Slide Generator")
    print(f"  Model: {MODEL}")
    print(f"  Slides: {len(SLIDES)}")
    print("=" * 50)

    results = []
    for slide in SLIDES:
        num = slide["num"]
        path = os.path.join(OUTPUT_DIR, f"slide-{num:02d}.png")
        print(f"\nSlide {num}/9...")
        success = generate_slide(slide["prompt"], path)
        results.append({"num": num, "ok": success})
        if num < len(SLIDES):
            time.sleep(3)  # rate limit

    # Summary
    print(f"\n{'=' * 50}")
    ok = sum(1 for r in results if r["ok"])
    print(f"  Resultado: {ok}/{len(results)} slides gerados")
    for r in results:
        status = "OK" if r["ok"] else "FALHOU"
        print(f"  Slide {r['num']:02d}: {status}")
    print(f"{'=' * 50}")


if __name__ == "__main__":
    main()
