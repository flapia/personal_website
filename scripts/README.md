# Agentes de Sincronización y Mantenimiento del Sitio

Este directorio contiene dos micro-agentes / scripts creados para ayudarte a mantener el contenido de tu sitio web actualizado de manera sencilla.

---

## 1. Agente de Auditoría de CV (`cv_sync_agent.py`)

### ¿Cuándo ejecutarlo?
Cada vez que actualices o agregues una nueva versión de tu CV (PDF) en la carpeta `public/` o en la raíz del proyecto.

### ¿Qué hace?
- Escanea automáticamente los archivos PDF de tu currículum (por ejemplo `public/Tapia_Felipe_CV.pdf` o `CV-may_2026 (1).pdf`).
- Extrae el texto del documento y revisa:
  - **Publicaciones**: coteja los títulos y años registrados en `src/content/papers/` con las citas detectadas en el CV.
  - **Proyectos**: verifica que tus proyectos de investigación vigentes o concluidos (`src/content/projects/`) estén reflejados.
  - **Docencia y Tesis**: compara tesistas y supervisiones (`src/content/teaching/`).
  - **Menciones de años recientes** (2024, 2025, 2026) en el CV para alertarte sobre posibles entradas nuevas que no estén en la web.

### ¿Cómo ejecutarlo?
Puedes correrlo de cualquiera de las siguientes dos formas en tu terminal:

```bash
npm run sync:cv
```
o directamente con Python:
```bash
python scripts/cv_sync_agent.py
```

---

## 2. Agente de Publicaciones ResearchGate / ORCID (`researchgate_sync_agent.py`)

### ¿Cuándo ejecutarlo?
Cada vez que publiques un nuevo artículo o cargues una nueva publicación, capítulo de libro o pre-print en tu perfil de **ResearchGate** o **ORCID**.

### ¿Qué hace?
- Analiza todos tus artículos locales existentes en `src/content/papers/` (títulos, años, DOIs).
- Consulta de forma directa y oficial tu registro académico enlazado mediante la API de ORCID (`0000-0002-5397-3071`) y ResearchGate.
- Realiza una comparación difusa inteligente (*fuzzy matching* y normalización de texto) entre tus publicaciones locales y las registradas en el portal.
- Te muestra una lista ordenada de **artículos nuevos o faltantes** con su año, título y enlace DOI para que puedas agregarlos con un par de clics a `src/content/papers/`.

### ¿Cómo ejecutarlo?
En tu terminal:

```bash
npm run sync:papers
```
o directamente con Python:
```bash
python scripts/researchgate_sync_agent.py
```

---

## Cómo agregar una nueva publicación al sitio

Cuando el agente te avise de un artículo nuevo, simplemente crea un archivo `.md` dentro de `src/content/papers/` (por ejemplo `src/content/papers/mi-nuevo-articulo-2026.md`) con la siguiente estructura:

```markdown
---
title: "Título de la publicación"
year: 2026
journal: "Nombre del Journal o Revista"
type: "Journal Article"
authors:
  - "Tapia, F."
  - "Coautor, A."
doi: "https://doi.org/10.xxxx/xxxxx"
url: "https://doi.org/10.xxxx/xxxxx"
featured: false
---

Resumen o abstract del artículo (opcional).
```
