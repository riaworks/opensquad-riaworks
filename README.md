# Opensquad

Crie squads de agentes de IA que trabalham juntos — direto do seu IDE.

```
 ╔═══╗ ╔═══╗ ╔═══╗ ╔═══╗
 ║ $ ║ ║ $ ║ ║ $ ║ ║ $ ║   100% GRATUITO
 ╚═╤═╝ ╚═╤═╝ ╚═╤═╝ ╚═╤═╝   Zero custo. Zero licenca. Zero pegadinha.
   │     │     │     │
   ╵     ╵     ╵     ╵       Mas cada squad roda com os SEUS tokens.
```

> [!IMPORTANT]
> **Este projeto e 100% gratuito e open source.**
> Voce so gasta os tokens da sua propria API (Claude, Gemini, etc).
> Nos nao cobramos nada. Nunca.

```
        ( (
         ) )
      .───────.
      │       │]
       \     /    Se esse projeto te economizou horas de trabalho,
        `───'     considere pagar um cafe com tokens reais :)
```

<h3 align="center">
  <img src="https://img.shields.io/badge/Pix-pix%40riaworks.com.br-FF6600?style=for-the-badge&logo=pix&logoColor=white" alt="Pix: pix@riaworks.com.br" />
</h3>
<p align="center"><i>Qualquer valor ajuda a manter o projeto vivo e cafeinado.</i></p>

---

## Como Usar

### 1. Instale o Opensquad

Se ainda nao tem o Opensquad instalado, clone o framework base:

```bash
git clone https://github.com/renatoasse/opensquad.git
cd opensquad
npm install
```

> [!TIP]
> Saiba mais sobre o Opensquad em [github.com/renatoasse/opensquad](https://github.com/renatoasse/opensquad)

### 2. Instale este squad pack

Abra o projeto Opensquad no seu IDE com uma LLM que tenha acesso ao terminal — recomendamos o [Claude Code](https://claude.ai/claude-code).

Cole este prompt:

```
Clone o repositorio https://github.com/riaworks/opensquad-riaworks.git
em uma pasta temporaria e copie para dentro do meu projeto Opensquad:
  - squads/         → squads/
  - skills/         → skills/
  - materiais/      → materiais/
  - _opensquad/_memory/ → _opensquad/_memory/
Depois registre os squads com /opensquad e remova a pasta temporaria.
```

A LLM vai fazer o merge automaticamente: clonar, copiar os squads e skills, e registrar tudo no seu Opensquad.

### 3. Configure suas APIs

Preencha o `.env` na raiz do projeto com suas chaves:

```env
GEMINI_API_KEY=sua-chave-aqui
INSTAGRAM_ACCESS_TOKEN=seu-token-aqui
INSTAGRAM_USER_ID=seu-id-aqui
IMGBB_API_KEY=sua-chave-aqui
```

### 4. Use

Abra o projeto no seu IDE e digite:

```
/opensquad
```

Isso abre o menu principal. De la voce pode criar squads, executa-los e mais.

Voce tambem pode ser direto — descreva o que quer em linguagem natural:

```
/opensquad crie um squad para escrever posts no LinkedIn sobre IA
/opensquad execute o squad meu-squad
```

## Criar um Squad

Digite `/opensquad` e escolha "Criar squad" no menu, ou seja direto:

```
/opensquad crie um squad para [o que voce precisa]
```

O Arquiteto fara algumas perguntas, projetara o squad e configurara tudo automaticamente.

## Executar um Squad

Digite `/opensquad` e escolha "Executar squad" no menu, ou seja direto:

```
/opensquad execute o squad <nome-do-squad>
```

O squad executa automaticamente, pausando apenas nos checkpoints de decisao.

## Escritorio Virtual

O Escritorio Virtual e uma interface visual 2D que mostra seus agentes trabalhando em tempo real.

**Passo 1 — Gere o dashboard** (no seu IDE):

```
/opensquad dashboard
```

**Passo 2 — Sirva localmente** (no terminal):

```bash
npx serve squads/<nome-do-squad>/dashboard
```

**Passo 3 —** Abra `http://localhost:3000` no seu navegador.

---

# Opensquad (English)

Create AI squads that work together — right from your IDE.

```
 ╔═══╗ ╔═══╗ ╔═══╗ ╔═══╗
 ║ $ ║ ║ $ ║ ║ $ ║ ║ $ ║   100% FREE
 ╚═╤═╝ ╚═╤═╝ ╚═╤═╝ ╚═╤═╝   No cost. No license. No catch.
   │     │     │     │
   ╵     ╵     ╵     ╵       But each squad runs on YOUR tokens.
```

> [!IMPORTANT]
> **This project is 100% free and open source.**
> You only spend your own API tokens (Claude, Gemini, etc).
> We charge nothing. Ever.

```
        ( (
         ) )
      .───────.
      │       │]
       \     /    If this project saved you hours of work,
        `───'     consider buying us a coffee with real tokens :)
```

<h3 align="center">
  <img src="https://img.shields.io/badge/Pix-pix%40riaworks.com.br-FF6600?style=for-the-badge&logo=pix&logoColor=white" alt="Pix: pix@riaworks.com.br" />
</h3>
<p align="center"><i>Any amount helps keep the project alive and caffeinated.</i></p>

---

## How to Use

### 1. Install Opensquad

If you don't have Opensquad installed yet, clone the base framework:

```bash
git clone https://github.com/renatoasse/opensquad.git
cd opensquad
npm install
```

> [!TIP]
> Learn more about Opensquad at [github.com/renatoasse/opensquad](https://github.com/renatoasse/opensquad)

### 2. Install this squad pack

Open the Opensquad project in your IDE with an LLM that has terminal access — we recommend [Claude Code](https://claude.ai/claude-code).

Paste this prompt:

```
Clone the repository https://github.com/riaworks/opensquad-riaworks.git
into a temporary folder and copy into my Opensquad project:
  - squads/         → squads/
  - skills/         → skills/
  - materiais/      → materiais/
  - _opensquad/_memory/ → _opensquad/_memory/
Then register the squads with /opensquad and remove the temporary folder.
```

The LLM will handle the merge automatically: clone, copy squads and skills, and register everything in your Opensquad.

### 3. Configure your APIs

Fill in the `.env` at the project root with your keys:

```env
GEMINI_API_KEY=your-key-here
INSTAGRAM_ACCESS_TOKEN=your-token-here
INSTAGRAM_USER_ID=your-id-here
IMGBB_API_KEY=your-key-here
```

### 4. Use it

Open the project in your IDE and type:

```
/opensquad
```

This opens the main menu. From there you can create squads, run them, and more.

You can also be direct — describe what you want in plain language:

```
/opensquad create a squad for writing LinkedIn posts about AI
/opensquad run my-squad
```

## Create a Squad

Type `/opensquad` and choose "Create squad" from the menu, or be direct:

```
/opensquad create a squad for [what you need]
```

The Architect will ask a few questions, design the squad, and set everything up automatically.

## Run a Squad

Type `/opensquad` and choose "Run squad" from the menu, or be direct:

```
/opensquad run the <squad-name> squad
```

The squad runs automatically, pausing only at decision checkpoints.

## Virtual Office

The Virtual Office is a 2D visual interface that shows your agents working in real time.

**Step 1 — Generate the dashboard** (in your IDE):

```
/opensquad dashboard
```

**Step 2 — Serve it locally** (in terminal):

```bash
npx serve squads/<squad-name>/dashboard
```

**Step 3 —** Open `http://localhost:3000` in your browser.

---

## License

MIT License — see [LICENSE](LICENSE) for details.
