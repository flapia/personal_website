import os

papers = [
    {"id": "2025-munoz", "title": "Resolving crustal and subcrustal dynamic sources in continental arc magmas: The cenozoic andean arc of central chile", "year": 2025, "journal": "Geochemistry, Geophysics, Geosystems", "type": "Journal Article", "authors": "Marcia Muñoz-Gómez, CM Fanning, Tapia, Felipe, I Payacán, Francisco Fuentes, Marcelo Farías, Reynaldo Charrier, Mireille Polvé, Sergio Quiñones, Katja Deckart"},
    {"id": "2025-gonzalez", "title": "Compressional tectonics related to fuegian orogeny: Insights from ams and structural geology in navarino island, chile", "year": 2025, "journal": "Journal of South American Earth Sciences", "type": "Journal Article", "authors": "Roberto González-Vidal, Tapia, Felipe*, Fernando Poblete, Matías Peña, Esteban Salazar, and Valentina Ríos"},
    {"id": "2024-charrier", "title": "The Cenozoic Abanico rift system: Implications of increased southward extension in the southern central Andes, in Chile", "year": 2024, "journal": "Journal of South American Earth Sciences", "type": "Journal Article", "authors": "Charrier, R., Contreras, J. P., Díaz-Bórquez, C., Farías, M., Jara, P., Muñoz-Gómez, M.,Quiñones, S., Rodriguez, M. P., Tapia, F y Villaseñor, T."},
    {"id": "2024-lopasso", "title": "Pleistocene deformation of the Malargüe fold-thrust belt from structural modelling and geochronology of syntectonic sedimentation", "year": 2024, "journal": "Journal of the Geologicla Society", "type": "Journal Article", "authors": "Lopasso, A.; Tapia, F.; Feal, R.; O, R.; Slama, J.; Hlebszevitsch, J.; Giambiagi, L.; Ghiglione, M."},
    {"id": "2023-velasquez", "title": "Magmatic evolution of the Cretaceous-earliest Paleocene intrusive rocks of Navarino Island (55°S): implications for the early-stage development of the Fuegian Andes", "year": 2023, "journal": "Journal of Geological Society", "type": "Journal Article", "authors": "Velásquez, R., Bastías, J., Salazar, E., Poblete, F., González Guillot, M., Chew, D., Peña, M., Tapia, F., Drakou, F."},
    {"id": "2021-guzman", "title": "Lower Jurassic deformation in the eastern Huincul High, Argentina", "year": 2021, "journal": "Journal of South America Earth Sciences", "type": "Journal Article", "authors": "Guzmán, C., Tapia, F., Ambrosio, A., Gutierrez Pleimling, A., Bustos, G., Gómez, C., González, J. M."},
    {"id": "2021-gutierrez", "title": "Sequence-stratigraphic study of Cuyo Group in the Agua del Cajón Block, Neuquén Basin, Argentina", "year": 2021, "journal": "Journal of South America Earth Sciences", "type": "Journal Article", "authors": "Gutierrez Pleimling, A., Ambrosio, A., Gómez, C., Bustos, G., González, J. M., Guzmán, C., Tapia, F."},
    {"id": "2020-munoz", "title": "Eocene Arc Petrogenesis in Central Chile (∼33.5°S) and Implications for the Late Cretaceous-Miocene Andean Setting: Tracking the Evolving Tectonic Regime", "year": 2020, "journal": "Journal of the Geological Society", "type": "Journal Article", "authors": "Muñoz-Gómez, M., Fuentes, C., Fuentes, F., Tapia, F., Benoit, M., Farías, M., Fanning, C. M., Fock, A., Charrier, R., Sellés, D., Bustamante, D."},
    {"id": "2020-tapia", "title": "Middle Jurassic- LateCretaceous deposits on the Chilean Andean side and the paleogeography of western margin of the Neuquén Basin", "year": 2020, "journal": "Springer Earth System Sciences", "type": "Book Chapter", "authors": "Tapia, F., Muñoz, M., Farías, M., Charrier, R., Astaburuaga, D."},
    {"id": "2019-poblete", "title": "Paleomagnetismo y geocronología de isla navarino: Resultados preliminares e implicancias en la evolución tectónica del sistema patagonia-peninsula Antártica", "year": 2019, "journal": "Latinmag Letters", "type": "Journal Article", "authors": "Poblete, F., Velásquez, R., Peña, M., Tapia, F., Salazar, E., Rodrigo, J."},
    {"id": "2018-munoz", "title": "Extensional tectonics during Late Cretaceous evolution of the Southern Central Andes: Evidence from the Chilean Main Range at 35°S", "year": 2018, "journal": "Tectonophysics", "type": "Journal Article", "authors": "Muñoz, M., Tapia, F., Persico, M., Benoit, M., Charrier, R., Farías, M., Rojas, A."},
    {"id": "2015-tapia", "title": "Late Cenozoic contractional evolution of the current arc-volcanic region along the southern Central Andes (35°20´S)", "year": 2015, "journal": "Journal of Geodynamics", "type": "Journal Article", "authors": "Tapia, F; Farías, M.; Naipauer, M.; Puratish, J."},
    {"id": "2016-pavez", "title": "Characterization of the hydrothermal system of the Tinguiririca Volcanic Complex, Central Chile, using structural geology and pasive seismic tomography", "year": 2016, "journal": "J. Volca. and Geothermal Research", "type": "Journal Article", "authors": "Pavez, C., Tapia, F., Comte, D., Gutiérrez, F., Lira, E., Charrier, R., Benavente, O."},
    {"id": "2015-naipauer", "title": "Detrital and volcanic zircon U-Pb ages from southern Mendoza (Argentina): An insight on the sources regions in the northern part of Neuquén Basin", "year": 2015, "journal": "Journal of South American Earth Sciences", "type": "Journal Article", "authors": "Naipauer, M., Tapia, F., Mescua, J., Farías, M., Pimentel, M., Ramos, V."},
    {"id": "2014-charrier", "title": "Tectono-stratigraphic evolution of the Andean Orogen between 31 and 37°S (Chile and Western Argentina)", "year": 2014, "journal": "Geological Society of London, Special Publications", "type": "Journal Article", "authors": "Charrier, R, Ramos, V,A., Tapia, F, Sagripanti, L."},
    {"id": "2014-giambiagi", "title": "Evolution of shallow and deep structures along the Maipo.Tunuyán transect (33°40'S): from the Pacific coast to the Andean foreland", "year": 2014, "journal": "Geological Society of London, Special Publications", "type": "Journal Article", "authors": "Giambiagi, L., Tassara, A., Mescua, J., Tinuk, M., Alvarez, P., Godoy, E., Hoke, G., Pinto, L. Spagnotto, S., Porras, H., Tapia, F., Jara, P., Bechis, F., García, V., Suriano, J., Moreira, S., Pagano, S."},
    {"id": "2014-rossel", "title": "The Upper Jurassic volcanism of the Río Damas-Tordillo Formation (33°-35.5°S): Insights on petrogenesis, chronology, provenance and tectonic implications", "year": 2014, "journal": "Andean Geology", "type": "Journal Article", "authors": "Rossel, P.; Oliveros, V; Mescua, J.; Tapia, F.; Ducea, M.; Calderón, S.; Charrier, R.; Hoffman, D."},
    {"id": "2010-farias", "title": "Crustal scale structural architecture in Central Chile Based on seismicity and surface geology: Implications for Andean mountain building", "year": 2010, "journal": "Tectonics", "type": "Journal Article", "authors": "Farías, M.; Comte, D.; Charrier, R.; Martinod, J.; David, C.; Tassara, A.; Tapia, F.; Fock, A."}
]

for p in papers:
    content = f"""---
title: "{p['title']}"
year: {p['year']}
journal: "{p['journal']}"
type: "{p['type']}"
authors: {str([a.strip() for a in p['authors'].split(',')])}
lang: "en"
---
{p['title']}.
"""
    with open(f"c:/Users/ftapi/.gemini/antigravity-ide/personal_website/src/content/papers/{p['id']}.md", 'w', encoding='utf-8') as f:
        f.write(content)
