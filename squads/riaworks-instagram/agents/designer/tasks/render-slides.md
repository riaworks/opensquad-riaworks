# Task: Renderizar HTML em Imagens PNG

## Task Config

```yaml
order: 2
```

## Objetivo

Renderizar cada arquivo HTML de slide em imagem PNG de alta qualidade usando a skill image-creator, com verificacao de qualidade antes do batch completo.

## Processo

### 1. Preparacao para Renderizacao

- Listar todos os arquivos HTML criados na task anterior
- Confirmar que cada HTML esta completo e autocontido
- Verificar que o diretorio de output existe e esta acessivel
- Organizar a ordem de renderizacao (slide-01 primeiro, depois sequencial)

### 2. Renderizacao do Primeiro Slide (Verificacao)

Renderizar APENAS o primeiro slide antes do batch:

- Usar image-creator para converter o HTML do slide 01 em PNG
- Viewport: 1080x1440 pixels
- Verificar o resultado:
  - Textos legiveis e sem corte
  - Cores corretas conforme design system
  - Margens de seguranca respeitadas
  - Elementos posicionados corretamente
  - Sem artefatos visuais ou sobreposicoes
- Se houver problemas, voltar ao HTML, corrigir e re-renderizar
- So prosseguir para o batch quando o primeiro slide estiver perfeito

### 3. Batch Render dos Demais Slides

Apos aprovacao do primeiro slide:

- Renderizar cada slide restante sequencialmente
- Usar as mesmas configuracoes de viewport (1080x1440)
- Para cada slide renderizado, fazer verificacao rapida:
  - Dimensoes corretas
  - Texto legivel
  - Consistencia visual com o primeiro slide
- Nomear arquivos de saida: `slide-01.png`, `slide-02.png`, etc.

### 4. Verificacao Final do Conjunto

Apos renderizar todos os slides:

- Revisar o conjunto completo em sequencia
- Verificar consistencia visual entre todos os PNGs
- Confirmar que a narrativa visual flui da capa ao CTA
- Validar que nenhum slide ficou com problemas de renderizacao
- Contar total de slides (maximo 10)

### 5. Organizacao dos Arquivos

Estruturar o output final:

```
output/
  carrossel-[tema]/
    design-system.md
    html/
      slide-01-capa.html
      slide-02-conteudo.html
      ...
    png/
      slide-01.png
      slide-02.png
      ...
```

## Configuracao da Skill image-creator

Parametros de renderizacao:

- **Viewport width:** 1080
- **Viewport height:** 1440
- **Device scale factor:** 1 (para output 1080x1440 real)
- **Format:** PNG
- **Full page:** false (viewport fixo)

## Criterios de Conclusao

- Primeiro slide renderizado e verificado antes do batch
- Todos os slides renderizados em PNG 1080x1440
- Verificacao visual de cada slide individual
- Consistencia visual confirmada no conjunto completo
- Arquivos organizados na estrutura de output correta
- Maximo de 10 PNGs no carrossel final
- Nenhum artefato visual, texto cortado ou problema de renderizacao
