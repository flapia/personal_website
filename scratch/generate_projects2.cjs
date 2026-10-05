const fs = require('fs');
const path = require('path');

const projects = [
    {"id": "pict-2021-01210", "title": "Estructuras oblicuas al orógeno andino en Mendoza y San Juan: controles en la deformación y rol en la actividad magmática y sísmica", "category": "Academic", "role": "Colaborador", "year": "2021", "location": "Mendoza y San Juan, Argentina", "lang": "es"},
    {"id": "pict-2019-00997", "title": "Aportes para la resolución de problemas tectónicos y estructurales", "category": "Academic", "role": "Grupo Responsable", "year": "2019", "location": "Argentina", "lang": "es"},
    {"id": "pict-2019-01018", "title": "Análisis de las estructuras neotectónicas entre los 35º y 36ºS: estudio sobre la distribución y desarrollo de estructuras activas dentro de una cuña orogénica", "category": "Academic", "role": "Grupo Colaborador", "year": "2019", "location": "Argentina (35º-36ºS)", "lang": "es"},
    {"id": "fondecyt-1210475", "title": "THE EFFECTS OF SOUTHWARD INCREASED EXTENSION IN THE ABANICO BASIN STAGE: THE MAULE PROFILE (36°S) AND THE RECONFIGURATION OF A CONTINENTAL RIFT SYSTEM", "category": "Academic", "role": "Colaborador", "year": "2021", "location": "Chile (36°S)", "lang": "en"},
    {"id": "pict-2020-a02085", "title": "Modelos de redes de fracturas sintéticas en reservorios geotérmicos: Una herramienta para la planificación de la exploración profunda", "category": "Academic", "role": "Grupo Responsable", "year": "2020", "location": "Argentina", "lang": "es"},
    {"id": "pict-2017-2657", "title": "Evolución de la cuenca de antepaís neógena de los Andes Centrales del sur a los 35°S: Entendiendo los procesos profundos y superficiales en un sistema orogénico", "category": "Academic", "role": "Investigador Principal", "year": "2017", "location": "Argentina", "lang": "es"},
    {"id": "pict-2016-1407", "title": "Aplicación de modelos análogos y numéricos a problemas tectónicos-estructurales", "category": "Academic", "role": "Grupo Responsable", "year": "2016", "location": "Argentina", "lang": "es"},
    {"id": "pict-2015-1181", "title": "Evolución tecto-magmática de la faja plegada y corrida de Malargüe: hacia una mejor comprensión de la relación entre deformación, campo de esfuerzos y actividad magmática en los Andes", "category": "Academic", "role": "Colaborador", "year": "2015", "location": "Malargüe, Argentina", "lang": "es"},
    {"id": "pict-2016-2069", "title": "Modelización numérica de la evolución térmica de la litosfera oceánica", "category": "Academic", "role": "Colaborador", "year": "2016", "location": "Argentina", "lang": "es"},
    {"id": "pict-2013-1309", "title": "Modelado análogo y numérico tectónico-estructural", "category": "Academic", "role": "Colaborador", "year": "2013", "location": "Argentina", "lang": "es"},
    {"id": "fondecyt-1161806", "title": "From top to bottom: Deciphering the controlling mechanism for Andean building in Central Chile-Argentina", "category": "Academic", "role": "Colaborador", "year": "2016", "location": "Chile-Argentina", "lang": "en"},
    {"id": "stan-2017", "title": "Servicios Tecnológicos de alto nivel (STAND) para GEOANDINA S.A.", "category": "Industry", "role": "Grupo Responsable", "year": "2017", "location": "Cuenca Neuquina, Argentina", "lang": "es"},
    {"id": "stan-2018-2019", "title": "Servicios Tecnológicos de alto nivel (STAND) para GEOANDINA S.A.", "category": "Industry", "role": "Grupo Responsable", "year": "2018-2019", "location": "Cuenca Neuquina, Argentina", "lang": "es"},
    {"id": "stan-2019", "title": "Servicios Tecnológicos de alto nivel (STAND) para GEOANDINA S.A.", "category": "Industry", "role": "Grupo Responsable", "year": "2019", "location": "Cuenca Neuquina, Argentina", "lang": "es"},
    {"id": "stan-2021", "title": "Servicios Tecnológicos de alto nivel (STAND) para GEOANDINA S.A.", "category": "Industry", "role": "Grupo Responsable", "year": "2021", "location": "Cuenca Neuquina, Argentina", "lang": "es"},
    {"id": "stan-2025-marzo", "title": "Servicios Tecnológicos de alto nivel (STAND) para GEOANDINA S.A.", "category": "Industry", "role": "Grupo Responsable", "year": "2025", "location": "Cuenca Neuquina, Argentina", "lang": "es"},
    {"id": "stan-2025-octubre", "title": "Servicios Tecnológicos de alto nivel (STAND) para GEOANDINA S.A.", "category": "Industry", "role": "Grupo Responsable", "year": "2025", "location": "Cuenca Neuquina, Argentina", "lang": "es"}
];

projects.forEach(p => {
    const content = `---
title: "${p.title.replace(/"/g, '\\"')}"
category: "${p.category}"
role: "${p.role}"
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
