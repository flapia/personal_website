const fs = require('fs');
const path = require('path');

const teaching = [
    {"id": "uba-jtp-estructural", "title": "Geología Estructural, Geotectónica y Fundamentos de Tectónica", "institution": "Universidad de Buenos Aires (FCEN-UBA)", "role": "Jefe de Trabajos Prácticos (JTP)", "year": "2020-Actualidad", "category": "Course", "link": "https://flapia.github.io/Geologia_estructural/README.html", "lang": "es"},
    {"id": "uba-ayudante", "title": "Geología General, Regional y Geoestadística", "institution": "Universidad de Buenos Aires (FCEN-UBA)", "role": "Ayudante de 1°", "year": "2016-2020", "category": "Course", "lang": "es"},
    {"id": "uchile-auxiliar", "title": "Procesos Geodinámicos, Trabajo de campo, Geología Estructural", "institution": "Universidad de Chile", "role": "Profesor auxiliar", "year": "2009-2013", "category": "Course", "lang": "es"},
    {"id": "tesis-menschik", "title": "TFL: Agustina Menschik", "institution": "UBA", "role": "Director", "year": "2025 (En curso)", "category": "Mentorship", "lang": "es"},
    {"id": "tesis-lorenzo", "title": "TFL: Facundo Lorenzo", "institution": "UBA", "role": "Director", "year": "2025 (En curso)", "category": "Mentorship", "lang": "es"},
    {"id": "tesis-rivera", "title": "TFL: Sofía Rivera", "institution": "Universidad de Chile", "role": "Co-Director", "year": "2025 (En curso)", "category": "Mentorship", "lang": "es"},
    {"id": "tesis-insaurralde-doc", "title": "Tesis Doctoral: Lic. Fiorella Insaurralde", "institution": "UBA / CONICET", "role": "Director", "year": "2024 (En curso)", "category": "Mentorship", "lang": "es"},
    {"id": "tesis-arevalo", "title": "TFL: Ernesto Arevalo", "institution": "UBA", "role": "Co-Director", "year": "2024 (En curso)", "category": "Mentorship", "lang": "es"},
    {"id": "tesis-veraguas", "title": "TFL: Gabriel Veraguas Lema", "institution": "Universidad Andres Bello", "role": "Director", "year": "2024 (En curso)", "category": "Mentorship", "lang": "es"},
    {"id": "tesis-miranda", "title": "TFL: Juan Ignacio Miranda", "institution": "UBA", "role": "Director", "year": "2024 (En curso)", "category": "Mentorship", "lang": "es"},
    {"id": "tesis-hovsepian", "title": "TFL: Mariano Hovsepian", "institution": "UBA", "role": "Director", "year": "2024 (En curso)", "category": "Mentorship", "lang": "es"},
    {"id": "tesis-insaurralde-lic", "title": "TFL: Fiorella Insaurralde", "institution": "UBA", "role": "Director", "year": "2024 (Finalizado)", "category": "Mentorship", "lang": "es"},
    {"id": "tesis-diaz", "title": "TFL: Alfredo Díaz", "institution": "Universidad Andres Bello", "role": "Co-Director", "year": "2022 (Finalizado)", "category": "Mentorship", "lang": "es"},
    {"id": "tesis-silva", "title": "TFL: Diego Silva", "institution": "UBA", "role": "Director", "year": "2021 (Finalizado)", "category": "Mentorship", "lang": "es"},
    {"id": "tesis-lopaso", "title": "TFL: Ailín Lopaso", "institution": "UBA", "role": "Director", "year": "2020 (Finalizado)", "category": "Mentorship", "lang": "es"},
    {"id": "tesis-helman", "title": "TFL: Ariel Helman", "institution": "UBA", "role": "Director", "year": "2019 (Finalizado)", "category": "Mentorship", "lang": "es"},
    {"id": "tesis-feal", "title": "TFL: Román Feal", "institution": "UBA", "role": "Director", "year": "2018 (Finalizado)", "category": "Mentorship", "lang": "es"}
];

teaching.forEach(t => {
    let frontmatter = `---
title: "${t.title.replace(/"/g, '\\"')}"
institution: "${t.institution}"
role: "${t.role}"
year: "${t.year}"
category: "${t.category}"
lang: "${t.lang}"
`;
    if (t.link) {
        frontmatter += `link: "${t.link}"\n`;
    }
    frontmatter += `---
${t.role} - ${t.title}.
`;
    const filepath = path.join(__dirname, '..', 'src', 'content', 'teaching', `${t.id}.md`);
    fs.writeFileSync(filepath, frontmatter, 'utf8');
});
console.log("Teaching Done");
