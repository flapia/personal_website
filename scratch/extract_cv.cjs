const fs = require('fs');
const pdf = require('pdf-parse');

let dataBuffer = fs.readFileSync('C:/Users/ftapi/.gemini/antigravity-ide/brain/a9d095a8-d991-4a8e-ba3d-af9783c95702/.tempmediaStorage/media_1791138182122.pdf');

pdf(dataBuffer).then(function(data) {
    fs.writeFileSync('cv_full.txt', data.text, 'utf8');
    console.log('Done');
});
