const fs = require('fs');
const path = require('path');

const teaching = [
    {"id": "uba-jtp-estructural", "title": "Geología Estructural, Geotectónica y Fundamentos de Tectónica", "institution": "Universidad de Buenos Aires (FCEN-UBA)", "role": "Jefe de Trabajos Prácticos (JTP)", "year": "2020-Actualidad", "category": "Course", "lang": "es"},
    {"id": "uba-ayudante", "title": "Geología General, Regional y Geoestadística", "institution": "Universidad de Buenos Aires (FCEN-UBA)", "role": "Ayudante de 1°", "year": "2016-2020", "category": "Course", "lang": "es"},
    {"id": "uchile-auxiliar", "title": "Procesos Geodinámicos, Trabajo de campo, Geología Estructural", "institution": "Universidad de Chile", "role": "Profesor auxiliar", "year": "2009-2013", "category": "Course", "lang": "es"},
    {"id": "tesis-menschik", "title": "Trabajo final de licenciatura: Agustina Menschik", "institution": "Universidad de Buenos Aires", "role": "Director", "year": "2025", "category": "Mentorship", "lang": "es"},
    {"id": "tesis-insaurralde", "title": "Tesis Doctoral: Lic. Fiorella Insaurralde", "institution": "Universidad de Buenos Aires", "role": "Director", "year": "2024", "category": "Mentorship", "lang": "es"}
];

teaching.forEach(t => {
    const content = `---
title: "${t.title.replace(/"/g, '\\"')}"
institution: "${t.institution}"
role: "${t.role}"
year: "${t.year}"
category: "${t.category}"
lang: "${t.lang}"
---
${t.role} - ${t.title}.
`;
    const filepath = path.join(__dirname, '..', 'src', 'content', 'teaching', `${t.id}.md`);
    fs.writeFileSync(filepath, content, 'utf8');
});
console.log("Teaching Done");
