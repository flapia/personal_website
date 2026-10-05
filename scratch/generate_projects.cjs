const fs = require('fs');
const path = require('path');

const projects = [
    {"id": "pict-2021-01210", "title": "Estructuras oblicuas al orógeno andino en Mendoza y San Juan: controles en la deformación y rol en la actividad magmática y sísmica", "category": "Academic", "year": "2021", "location": "Mendoza y San Juan, Argentina", "lang": "es"},
    {"id": "pict-2019-00997", "title": "Aportes para la resolución de problemas tectónicos y estructurales", "category": "Academic", "year": "2019", "location": "Argentina", "lang": "es"},
    {"id": "pict-2019-01018", "title": "Análisis de las estructuras neotectónicas entre los 35º y 36ºS: estudio sobre la distribución y desarrollo de estructuras activas dentro de una cuña orogénica", "category": "Academic", "year": "2019", "location": "Argentina (35º-36ºS)", "lang": "es"},
    {"id": "fondecyt-1210475", "title": "THE EFFECTS OF SOUTHWARD INCREASED EXTENSION IN THE ABANICO BASIN STAGE: THE MAULE PROFILE (36°S) AND THE RECONFIGURATION OF A CONTINENTAL RIFT SYSTEM", "category": "Academic", "year": "2021", "location": "Chile (36°S)", "lang": "en"},
    {"id": "pict-2020-a02085", "title": "Modelos de redes de fracturas sintéticas en reservorios geotérmicos: Una herramienta para la planificación de la exploración profunda", "category": "Academic", "year": "2020", "location": "Argentina", "lang": "es"},
    {"id": "pict-2016-1407", "title": "Aplicación de modelos análogos y numéricos a problemas tectónicos-estructurales", "category": "Academic", "year": "2016", "location": "Argentina", "lang": "es"},
    {"id": "pict-2015-1181", "title": "Evolución tecto-magmática de la faja plegada y corrida de Malargüe", "category": "Academic", "year": "2015", "location": "Malargüe, Argentina", "lang": "es"},
    {"id": "stan-2017", "title": "Servicios Tecnológicos de alto nivel (STAND) para GEOANDINA S.A.", "category": "Industry", "year": "2017", "location": "Cuenca Neuquina, Argentina", "lang": "es"},
    {"id": "stan-2018-2019", "title": "Servicios Tecnológicos de alto nivel (STAND) para GEOANDINA S.A.", "category": "Industry", "year": "2018-2019", "location": "Cuenca Neuquina, Argentina", "lang": "es"},
    {"id": "stan-2019", "title": "Servicios Tecnológicos de alto nivel (STAND) para GEOANDINA S.A.", "category": "Industry", "year": "2019", "location": "Cuenca Neuquina, Argentina", "lang": "es"},
    {"id": "stan-2021", "title": "Servicios Tecnológicos de alto nivel (STAND) para GEOANDINA S.A.", "category": "Industry", "year": "2021", "location": "Cuenca Neuquina, Argentina", "lang": "es"},
    {"id": "stan-2025-marzo", "title": "Servicios Tecnológicos de alto nivel (STAND) para GEOANDINA S.A.", "category": "Industry", "year": "2025", "location": "Cuenca Neuquina, Argentina", "lang": "es"},
    {"id": "stan-2025-octubre", "title": "Servicios Tecnológicos de alto nivel (STAND) para GEOANDINA S.A.", "category": "Industry", "year": "2025", "location": "Cuenca Neuquina, Argentina", "lang": "es"}
];

projects.forEach(p => {
    const content = `---
title: "${p.title.replace(/"/g, '\\"')}"
category: "${p.category}"
year: "${p.year}"
location: "${p.location}"
lang: "${p.lang}"
---
${p.title}.
`;
    const filepath = path.join(__dirname, '..', 'src', 'content', 'projects', `${p.id}.md`);
    fs.writeFileSync(filepath, content, 'utf8');
});
console.log("Done");
