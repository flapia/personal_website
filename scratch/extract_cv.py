import PyPDF2

with open('../../CV-may_2026 (1).pdf', 'rb') as f:
    reader = PyPDF2.PdfReader(f)
    text = ''
    for page in reader.pages:
        text += page.extract_text() + '\n'
    
with open('cv_full.txt', 'w', encoding='utf-8') as out:
    out.write(text)
print('Done')
