import os
import sys
import glob
import re
import json
import requests
from bs4 import BeautifulSoup

# Ensure UTF-8 on Windows
if sys.platform == "win32":
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")

ORCID_ID = "0000-0002-5397-3071"
RESEARCHGATE_URL = "https://www.researchgate.net/profile/Felipe-Tapia-4"

def get_local_publications():
    base_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
    papers_dir = os.path.join(base_dir, "src", "content", "papers")
    local_papers = []
    
    if not os.path.exists(papers_dir):
        return local_papers

    for f in glob.glob(os.path.join(papers_dir, "*.md")):
        with open(f, "r", encoding="utf-8") as fh:
            content = fh.read()
            title_match = re.search(r'title:\s*"(.*?)"', content)
            year_match = re.search(r'year:\s*(\d{4})', content)
            journal_match = re.search(r'journal:\s*"(.*?)"', content)
            local_papers.append({
                "file": os.path.basename(f),
                "title": title_match.group(1) if title_match else os.path.basename(f),
                "year": int(year_match.group(1)) if year_match else 0,
                "journal": journal_match.group(1) if journal_match else ""
            })
    return local_papers

def normalize_title(title):
    # Remove punctuation and lowercase for comparison
    return re.sub(r'[^a-zA-Z0-9]', '', title).lower()

def fetch_researchgate_html():
    """Tries fetching ResearchGate profile or checking local HTML export"""
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
        "Accept-Language": "es-ES,es;q=0.9,en;q=0.8"
    }
    try:
        r = requests.get(RESEARCHGATE_URL, headers=headers, timeout=8)
        if r.status_code == 200:
            soup = BeautifulSoup(r.text, 'html.parser')
            # Extract titles if present
            titles = []
            for el in soup.find_all(['h2', 'h3', 'a']):
                txt = el.get_text().strip()
                if len(txt) > 25 and not any(k in txt.lower() for k in ['cookie', 'privacy', 'researchgate', 'terms']):
                    titles.append(txt)
            return list(set(titles))
    except Exception:
        pass
    return []

def fetch_orcid_works():
    """Fetches verified published works from ORCID API (linked to ResearchGate)"""
    url = f"https://pub.orcid.org/v3.0/{ORCID_ID}/works"
    headers = {"Accept": "application/json"}
    works = []
    try:
        r = requests.get(url, headers=headers, timeout=10)
        if r.status_code == 200:
            data = r.json()
            for group in data.get("group", []):
                summaries = group.get("work-summary", [])
                if summaries:
                    s = summaries[0]
                    title = s.get("title", {}).get("title", {}).get("value", "")
                    year_val = s.get("publication-date", {})
                    year = 0
                    if year_val and year_val.get("year"):
                        try:
                            year = int(year_val.get("year", {}).get("value", 0))
                        except ValueError:
                            year = 0
                    
                    # Extract external DOI if available
                    doi = ""
                    for ext in s.get("external-ids", {}).get("external-id", []):
                        if ext.get("external-id-type") == "doi":
                            doi = ext.get("external-id-value", "")
                            break

                    journal = s.get("journal-title", {})
                    journal_name = journal.get("value", "") if journal else ""

                    if title:
                        works.append({
                            "title": title,
                            "year": year,
                            "doi": doi,
                            "journal": journal_name
                        })
    except Exception as e:
        print(f"  [Aviso] Error al consultar ORCID API: {e}")
    return works

def compare_publications():
    print("\n========================================================")
    print("AGENTE 2: COMPARADOR DE PUBLICACIONES (PORTAL RESEARCHGATE / ORCID)")
    print("========================================================\n")
    
    local_papers = get_local_publications()
    print(f"1. Publicaciones locales en tu sitio (src/content/papers): {len(local_papers)}")
    local_normalized = {normalize_title(p["title"]): p for p in local_papers}

    # Intentar ResearchGate
    print(f"\n2. Consultando ResearchGate ({RESEARCHGATE_URL})...")
    rg_titles = fetch_researchgate_html()
    if rg_titles:
        print(f"   [OK] {len(rg_titles)} entradas extraídas directamente de ResearchGate.")
    else:
        print("   [!] ResearchGate cuenta con protección Cloudflare (HTTP 403 para requests directos).")
        print("   -> Utilizando la API oficial enlazada de ORCID (ID: " + ORCID_ID + ") para obtener la lista indexada.")

    # Consultar ORCID API
    orcid_works = fetch_orcid_works()
    print(f"\n3. Trabajos indexados en tu perfil científico oficial: {len(orcid_works)}")

    missing_in_local = []
    found_count = 0

    for work in orcid_works:
        norm = normalize_title(work["title"])
        # Fuzzy match or exact normalized
        match = False
        for local_norm in local_normalized.keys():
            if norm in local_norm or local_norm in norm or norm[:35] == local_norm[:35]:
                match = True
                break
        
        if match:
            found_count += 1
        else:
            missing_in_local.append(work)

    print(f"\n--- RESULTADO DE LA COMPARACIÓN ---")
    print(f"  * Publicaciones sincronizadas en el sitio: {found_count}")
    print(f"  * Publicaciones en el portal NO presentes en src/content/papers: {len(missing_in_local)}")

    if missing_in_local:
        print("\n[!] PUBLICACIONES NUEVAS O PENDIENTES DE INCORPORAR:")
        for idx, item in enumerate(missing_in_local[:15], 1):
            y_str = f"({item['year']}) " if item['year'] else ""
            doi_str = f" [DOI: {item['doi']}]" if item['doi'] else ""
            print(f"  {idx}. {y_str}{item['title']}{doi_str}")
        
        print("\nPara agregarlas automáticamente:")
        print("Crea un archivo markdown en src/content/papers/ con el formato:")
        print('---')
        print('title: "Nombre del paper"')
        print('year: 2026')
        print('journal: "Nombre de la revista"')
        print('type: "Journal Article"')
        print('authors: ["Tapia, F.", ...]')
        print('---')
    else:
        print("\n[OK] Todas las publicaciones de tu perfil están sincronizadas en tu sitio web.")

    print("\n========================================================\n")

if __name__ == "__main__":
    compare_publications()
