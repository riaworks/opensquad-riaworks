# Opensquad

Crie squads de agentes de IA que trabalham juntos — direto do seu IDE.

<table align="center"><tr><td>
<pre align="center">
  ___  ___  ___  ___
 | $ || $ || $ || $ |   100% GRATUITO
 |___||___||___||___|   Zero custo. Zero licenca. Zero pegadinha.
  | |  | |  | |  | |
  |_|  |_|  |_|  |_|   Mas cada squad roda com os SEUS tokens.
</pre>
</td></tr></table>

> [!IMPORTANT]
> **Este projeto e 100% gratuito e open source.**
> Voce so gasta os tokens da sua propria API (Claude, Gemini, etc).
> Nos nao cobramos nada. Nunca.

<table align="center"><tr><td>
<pre align="center">
       ( (
        ) )
     ._______.
     |       |]
     \       /    Se esse projeto te economizou horas de trabalho,
      '-----'     considere pagar um cafe com tokens reais :)
</pre>
</td></tr></table>

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
```

> [!TIP]
> Saiba mais sobre o Opensquad em [github.com/renatoasse/opensquad](https://github.com/renatoasse/opensquad)

### 2. Instale este squad pack

Abra o projeto Opensquad no seu IDE com uma LLM que tenha acesso ao terminal (recomendamos **Claude Code**) e peca:

```
Acesse https://github.com/riaworks/opensquad-riaworks e faca a
instalacao, merge e registro dos squads no meu projeto Opensquad.
```

A LLM vai clonar este repositorio, copiar os squads, skills e configuracoes para dentro do seu projeto Opensquad e registrar tudo automaticamente.

### 3. Use

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

<table align="center"><tr><td>
<pre align="center">
  ___  ___  ___  ___
 | $ || $ || $ || $ |   100% FREE
 |___||___||___||___|   No cost. No license. No catch.
  | |  | |  | |  | |
  |_|  |_|  |_|  |_|   But each squad runs on YOUR tokens.
</pre>
</td></tr></table>

> [!IMPORTANT]
> **This project is 100% free and open source.**
> You only spend your own API tokens (Claude, Gemini, etc).
> We charge nothing. Ever.

<table align="center"><tr><td>
<pre align="center">
       ( (
        ) )
     ._______.
     |       |]
     \       /    If this project saved you hours of work,
      '-----'     consider buying us a coffee with real tokens :)
</pre>
</td></tr></table>

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
```

> [!TIP]
> Learn more about Opensquad at [github.com/renatoasse/opensquad](https://github.com/renatoasse/opensquad)

### 2. Install this squad pack

Open the Opensquad project in your IDE with an LLM that has terminal access (we recommend **Claude Code**) and ask:

```
Access https://github.com/riaworks/opensquad-riaworks and install,
merge and register the squads into my Opensquad project.
```

The LLM will clone this repository, copy the squads, skills and configurations into your Opensquad project and register everything automatically.

### 3. Use it

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

MIT License

Copyright (c) 2026 Riaworks

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
