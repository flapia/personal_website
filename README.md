# Felipe Tapia - Sitio Web Académico & Profesional

Sitio web académico, docente e investigativo bilingüe (Español / Inglés) desarrollado con [Astro](https://astro.build/) y Tailwind CSS.

## 🚀 Características
- **Bilingüe completo**: Rutas en Español (`/es/`) e Inglés (`/en/`) con selector interactivo y persistencia.
- **Modo Claro / Oscuro**: Detección de tema del sistema operativo y alternador dinámico con persistencia (`localStorage`).
- **Secciones especializadas**:
  - `Publicaciones`: Filtrables por año y tipo, con enlaces DOI y visualización de autoría.
  - `Proyectos`: Fondos de investigación vigentes y finalizados (FONDECYT, etc.).
  - `Docencia`: Tesis de pregrado, magíster, doctorado e investigación postdoctoral organizadas cronológicamente y por estado (en curso / finalizadas).
  - `Herramientas`: Modelamiento cinemático/dinámico, termocronología, sensores remotos e instrumentación de campo.
  - `Galería`: Fotografías geológicas de terreno organizadas por expediciones (Andes Fueguinos, Cuenca de Abanico, Puna Austral, etc.) con soporte multi-imagen por etiqueta.
  - `Contacto`: Enlaces actualizados a ResearchGate, ORCID, Google Scholar, GitHub y formulario directo.
- **Micro-Agentes de automatización**:
  - `npm run sync:cv`: Audita y compara tus PDFs de CV con los contenidos del sitio.
  - `npm run sync:papers`: Sincroniza y detecta publicaciones nuevas desde el portal oficial de ResearchGate / ORCID.

## 💻 Desarrollo local

```bash
# Instalar dependencias
npm install

# Iniciar servidor de desarrollo
npm run dev

# Compilar para producción
npm run build
```

## 🤖 Comandos de Sincronización

```bash
# Auditar actualizaciones en CV
npm run sync:cv

# Consultar nuevas publicaciones en ResearchGate / ORCID
npm run sync:papers
```

## 🚢 Despliegue automático

El proyecto incluye un flujo de trabajo de **GitHub Actions** (`.github/workflows/deploy.yml`) listo para desplegarse automáticamente en **GitHub Pages** con cada `git push` a la rama `main`.
