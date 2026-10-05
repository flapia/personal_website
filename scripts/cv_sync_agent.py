import os
import sys
import glob
import re

# Ensure UTF-8 output on Windows consoles
if sys.platform == "win32":
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")

try:
    from pypdf import PdfReader
except ImportError:
    try:
        from PyPDF2 import PdfReader
    except ImportError:
        PdfReader = None

def extract_pdf_text(filepath):
    if not os.path.exists(filepath):
        return None
    if PdfReader is not None:
        try:
            reader = PdfReader(filepath)
            text = ""
            for page in reader.pages:
                t = page.extract_text()
                if t:
                    text += t + "\n"
            return text
        except Exception as e:
            print(f"  [Aviso] No se pudo leer {filepath} con pypdf: {e}")
    
    # Fallback to pdf-parse via node if python pypdf is not installed
    import subprocess
    cmd = ["node", "-e", f"""
        const fs = require('fs');
        const pdf = require('pdf-parse');
        pdf(fs.readFileSync({repr(filepath)})).then(d => process.stdout.write(d.text)).catch(e => {{}});
    """]
    try:
        res = subprocess.run(cmd, capture_output=True, text=True, encoding="utf-8")
        if res.returncode == 0 and res.stdout.strip():
            return res.stdout
    except Exception as e:
        pass
    return None

def find_cv_files():
    base_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
    public_dir = os.path.join(base_dir, "public")
    
    cv_candidates = []
    # Search in public and root
    patterns = [
        os.path.join(public_dir, "*.pdf"),
        os.path.join(base_dir, "*.pdf")
    ]
    for p in patterns:
        for f in glob.glob(p):
            if "cv" in os.path.basename(f).lower():
                cv_candidates.append(f)
    return list(set(cv_candidates))

def get_current_content(collection_dir):
    items = []
    if not os.path.exists(collection_dir):
        return items
    for f in glob.glob(os.path.join(collection_dir, "*.md")):
        with open(f, "r", encoding="utf-8") as fh:
            content = fh.read()
            # extract title
            title_match = re.search(r'title:\s*"(.*?)"', content)
            year_match = re.search(r'year:\s*"?(\d{4})"?', content)
            items.append({
                "file": os.path.basename(f),
                "title": title_match.group(1) if title_match else os.path.basename(f),
                "year": year_match.group(1) if year_match else ""
            })
    return items

def analyze_cv_updates():
    base_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
    content_dir = os.path.join(base_dir, "src", "content")
    
    print("\n========================================================")
    print("AGENTE 1: AUDITOR Y SINCRONIZADOR DE ARCHIVOS CV")
    print("========================================================\n")
    
    cv_files = find_cv_files()
    if not cv_files:
        print("[!] No se encontraron archivos de CV (.pdf) en public/ ni en la raiz del proyecto.")
        return
    
    print(f"Archivos de CV encontrados ({len(cv_files)}):")
    for f in cv_files:
        print(f"  * {os.path.basename(f)} ({os.path.relpath(f, base_dir)})")
    
    full_cv_text = ""
    for f in cv_files:
        print(f"\nExtrayendo contenido de: {os.path.basename(f)}...")
        txt = extract_pdf_text(f)
        if txt:
            print(f"  [OK] {len(txt)} caracteres leidos exitosamente.")
            full_cv_text += "\n" + txt
        else:
            print(f"  [!] No se pudo extraer texto de {os.path.basename(f)}.")
    
    if not full_cv_text.strip():
        print("\n[Error]: No se pudo extraer texto de los archivos CV.")
        return

    # 1. Comparar Publicaciones
    papers = get_current_content(os.path.join(content_dir, "papers"))
    print(f"\n--- Publicaciones registradas en el sitio ({len(papers)}) ---")
    papers_in_cv = 0
    missing_in_cv = []
    for p in papers:
        snippet = p["title"][:30].lower()
        if snippet in full_cv_text.lower():
            papers_in_cv += 1
        else:
            missing_in_cv.append(p)
    print(f"  * Publicaciones confirmadas en el CV: {papers_in_cv}/{len(papers)}")

    # 2. Deteccion de anios recientes
    recent_years = ["2024", "2025", "2026"]
    print(f"\n--- Busqueda de menciones recientes ({', '.join(recent_years)}) en el CV ---")
    for y in recent_years:
        count = len(re.findall(r'\b' + y + r'\b', full_cv_text))
        print(f"  * Anio {y}: {count} menciones encontradas.")

    # 3. Comparar Proyectos
    projects = get_current_content(os.path.join(content_dir, "projects"))
    print(f"\n--- Proyectos registrados en el sitio ({len(projects)}) ---")
    for prj in projects[:5]:
        found = prj["title"][:25].lower() in full_cv_text.lower()
        status = "[Detectado en CV]" if found else "[No literal]"
        print(f"  * {prj['title'][:50]}... {status}")

    # 4. Comparar Docencia y Tesis
    teaching = get_current_content(os.path.join(content_dir, "teaching"))
    print(f"\n--- Docencia y Tesis registradas ({len(teaching)}) ---")
    for t in teaching[:6]:
        snippet = t["title"].replace("TFL:", "").replace("Tesis Doctoral:", "").strip()
        found = snippet[:15].lower() in full_cv_text.lower()
        status = "[Encontrado]" if found else "[No literal]"
        print(f"  * {t['title']} ({t['year']}): {status}")

    print("\n========================================================")
    print("REPORTE COMPLETADO:")
    print("Para incorporar nuevos elementos detectados en tu CV:")
    print("1. Crea o modifica los archivos en src/content/(papers|projects|teaching)/")
    print("2. Ejecuta 'npm run build' para actualizar el sitio web.")
    print("========================================================\n")

if __name__ == "__main__":
    analyze_cv_updates()
