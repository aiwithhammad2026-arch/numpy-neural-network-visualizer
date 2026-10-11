const fs = require('fs');
const html = fs.readFileSync('index.html', 'utf-8');
const scriptMatch = html.match(/<script>([\s\S]*?)<\/script>/);

if (scriptMatch) {
  const code = scriptMatch[1];
  const lines = code.split('\n');
  lines.forEach((line, i) => {
    try {
      // test compiling incrementally or find unexpected token
      if (line.includes('var(') || line.includes('var--') || line.includes('var ') || line.includes('statusPill.style.borderColor = var(')) {
        console.log('Suspicious line ' + (i+1) + ': ' + line);
      }
    } catch(e) {}
  });

  // let us run a vm script to get exact line and column
  const vm = require('vm');
  try {
    new vm.Script(code);
  } catch (err) {
    console.log('Exact VM error:', err.message, err.stack);
  }
}
