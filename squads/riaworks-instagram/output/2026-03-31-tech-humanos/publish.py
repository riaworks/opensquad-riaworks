#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Publish tech-humanos carousel to Instagram via catbox.moe + Graph API."""

import os, json, time, subprocess, sys
from pathlib import Path

BASE = Path("C:/__canal_riaworks/squads/riaworks-instagram/output/2026-03-31-tech-humanos")
PNG_DIR = BASE / "carousel-slides" / "png"
JPEG_DIR = BASE / "carousel-slides" / "jpeg"

# Load env
from dotenv import load_dotenv
load_dotenv("C:/__canal_riaworks/.env")

IG_TOKEN = os.environ["INSTAGRAM_ACCESS_TOKEN"]
IG_USER = os.environ["INSTAGRAM_USER_ID"]
IG_BASE = "https://graph.facebook.com/v21.0"

CAPTION = """A IA já está salvando vidas. E você nem sabe. 👇

De diagnósticos precoces a resgate em desastres — a tecnologia está transformando o mundo silenciosamente.

Os números impressionam:
→ 17.000 vidas salvas por diagnóstico de IA em 2024
→ 94% de precisão na detecção de câncer de mama (vs 88% humana)
→ 48h de antecipação em alertas de enchentes no Brasil
→ 200M de estudantes conectados a tutores de IA
→ 400M de toneladas de CO₂ economizadas por otimização com IA
→ 1,3 bilhão de pessoas com deficiência beneficiadas por acessibilidade IA

E no Brasil?
→ SUS + IA: triagem de emergência com 40% menos espera
→ Agro inteligente: R$ 12 bilhões economizados em safras
→ Conecta Recife: 23% menos tempo de deslocamento

A tecnologia mais impactante não é a que gera imagens. É a que gera impacto.

Salva esse carrossel e manda pra quem acha que tecnologia só serve pra substituir pessoas.

#IA #InteligenciaArtificial #Tecnologia #Saude #IASalvandoVidas #IAparaBem #TechForGood #Inovacao #SaudeDigital #MeioAmbiente #Educacao #Acessibilidade #Brasil #CanalRiaworks"""


def convert_png_to_jpeg():
    """Convert PNGs to JPEGs for Instagram."""
    os.makedirs(JPEG_DIR, exist_ok=True)
    from PIL import Image
    files = sorted([f for f in os.listdir(PNG_DIR) if f.endswith(".png")])
    jpeg_paths = []
    for f in files:
        png_path = os.path.join(PNG_DIR, f)
        jpeg_path = os.path.join(JPEG_DIR, f.replace(".png", ".jpg"))
        img = Image.open(png_path).convert("RGB")
        img.save(jpeg_path, "JPEG", quality=92)
        jpeg_paths.append(jpeg_path)
        print(f"  Converted: {f} -> {f.replace('.png', '.jpg')}")
    return jpeg_paths


def upload_to_catbox(filepath):
    """Upload file to catbox.moe, return public URL."""
    result = subprocess.run(
        ["curl", "-s", "-F", "reqtype=fileupload", "-F", f"fileToUpload=@{filepath}",
         "https://catbox.moe/user/api.php"],
        capture_output=True, text=True, timeout=120
    )
    url = result.stdout.strip()
    if not url.startswith("http"):
        raise Exception(f"Catbox upload failed: {result.stdout} {result.stderr}")
    return url


def ig_api(endpoint, params, method="POST", retries=3):
    """Call Instagram Graph API with retry."""
    import urllib.request, urllib.parse, urllib.error
    url = f"{IG_BASE}/{endpoint}"
    data = urllib.parse.urlencode(params).encode()
    for attempt in range(retries):
        try:
            if method == "GET":
                full_url = f"{url}?{urllib.parse.urlencode(params)}"
                req = urllib.request.Request(full_url)
            else:
                req = urllib.request.Request(url, data=data)
            resp = urllib.request.urlopen(req, timeout=60)
            return json.loads(resp.read())
        except urllib.error.HTTPError as e:
            body = e.read().decode('utf-8', errors='replace')
            print(f"    API Error {e.code}: {body}")
            if attempt < retries - 1:
                wait = 5 * (attempt + 1)
                print(f"    Retry {attempt+1}/{retries} em {wait}s...")
                time.sleep(wait)
            else:
                raise Exception(f"API {e.code}: {body}")
        except Exception as e:
            if attempt < retries - 1:
                wait = 5 * (attempt + 1)
                print(f"    Retry {attempt+1}/{retries} em {wait}s... ({e})")
                time.sleep(wait)
            else:
                raise


def create_child_container(image_url):
    return ig_api(f"{IG_USER}/media", {
        "image_url": image_url,
        "is_carousel_item": "true",
        "access_token": IG_TOKEN,
    })["id"]


def poll_container(container_id, timeout=120):
    deadline = time.time() + timeout
    while time.time() < deadline:
        result = ig_api(f"{container_id}", {
            "fields": "status_code",
            "access_token": IG_TOKEN,
        }, method="GET")
        status = result.get("status_code", "")
        if status == "FINISHED":
            return True
        if status == "ERROR":
            raise Exception(f"Container {container_id} ERROR")
        time.sleep(3)
    raise Exception(f"Container {container_id} timeout")


def create_carousel(child_ids, caption):
    return ig_api(f"{IG_USER}/media", {
        "media_type": "CAROUSEL",
        "children": ",".join(child_ids),
        "caption": caption,
        "access_token": IG_TOKEN,
    })["id"]


def publish_media(container_id):
    return ig_api(f"{IG_USER}/media_publish", {
        "creation_id": container_id,
        "access_token": IG_TOKEN,
    })["id"]


def get_permalink(media_id):
    try:
        result = ig_api(f"{media_id}", {
            "fields": "permalink",
            "access_token": IG_TOKEN,
        }, method="GET")
        return result.get("permalink", "")
    except:
        return ""


def main():
    print("=" * 50)
    print("  Instagram Publisher — Tech Humanos")
    print("=" * 50)

    # 1. Convert PNGs to JPEG
    print("\n[1/6] Convertendo PNGs para JPEG...")
    if os.path.exists(JPEG_DIR) and len(list(JPEG_DIR.glob("*.jpg"))) == 9:
        jpeg_paths = sorted([str(f) for f in JPEG_DIR.glob("*.jpg")])
        print(f"  {len(jpeg_paths)} JPEGs já existem, reutilizando")
    else:
        jpeg_paths = convert_png_to_jpeg()
        print(f"  {len(jpeg_paths)} JPEGs criados")

    # 2. Upload to catbox.moe
    cache_file = BASE / "catbox-urls.json"
    if cache_file.exists():
        with open(cache_file) as f:
            image_urls = json.load(f)
        print(f"\n[2/6] Reutilizando {len(image_urls)} URLs do catbox...")
        for i, url in enumerate(image_urls):
            print(f"  [{i+1}/{len(image_urls)}] {url}")
    else:
        print("\n[2/6] Fazendo upload para catbox.moe...")
        image_urls = []
        for i, jp in enumerate(jpeg_paths):
            url = upload_to_catbox(jp)
            image_urls.append(url)
            print(f"  [{i+1}/{len(jpeg_paths)}] {url}")
        with open(cache_file, "w") as f:
            json.dump(image_urls, f)
        print(f"  URLs salvas em catbox-urls.json")

    # 3. Create child containers
    print("\n[3/6] Criando containers no Instagram...")
    child_ids = []
    for i, url in enumerate(image_urls):
        if i > 0:
            time.sleep(3)
        cid = create_child_container(url)
        child_ids.append(cid)
        print(f"  [{i+1}/{len(image_urls)}] container {cid}")

    # 4. Poll child containers
    print("\n[4/6] Aguardando processamento...")
    for cid in child_ids:
        poll_container(cid)
    print("  Todos os containers prontos!")

    # 5. Create carousel
    print("\n[5/6] Criando carrossel...")
    carousel_id = create_carousel(child_ids, CAPTION)
    poll_container(carousel_id)
    print(f"  Carousel container: {carousel_id}")

    # 6. Publish
    print("\n[6/6] Publicando...")
    post_id = publish_media(carousel_id)
    permalink = get_permalink(post_id)
    print(f"  Post ID: {post_id}")
    if permalink:
        print(f"  URL: {permalink}")

    print(f"\n{'=' * 50}")
    print(f"  PUBLICADO COM SUCESSO!")
    print(f"{'=' * 50}")
    if permalink:
        print(f"  {permalink}")

    # Save result
    result = {"post_id": post_id, "permalink": permalink, "image_urls": image_urls}
    with open(str(BASE / "publish-result.json"), "w") as f:
        json.dump(result, f, indent=2)


if __name__ == "__main__":
    main()
