const fs = require('fs');
const path = require('path');

const outDir = path.join(__dirname, '..', 'dist');
if (!fs.existsSync(outDir)) {
  fs.mkdirSync(outDir);
}

const outFile = path.join(outDir, 'artifact.txt');
fs.writeFileSync(outFile, `Build artifact generated at ${new Date().toISOString()}\n`);

console.log('Build complete, artifact at:', outFile);
