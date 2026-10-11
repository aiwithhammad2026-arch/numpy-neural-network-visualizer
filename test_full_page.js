const fs = require('fs');

// Read index.html
const html = fs.readFileSync('index.html', 'utf8');

// 1. Extract all getElementById calls
const idRegex = /document\.getElementById\(['"]([^'"]+)['"]\)/g;
const referencedIds = new Set();
let match;
while ((match = idRegex.exec(html)) !== null) {
  referencedIds.add(match[1]);
}

console.log('Total referenced IDs in JS:', referencedIds.size);

// 2. Verify all referenced IDs exist in HTML
const missingIds = [];
for (const id of referencedIds) {
  const elemRegex = new RegExp(`id=["']${id}["']`);
  if (!elemRegex.test(html)) {
    missingIds.push(id);
  }
}

if (missingIds.length > 0) {
  console.error('MISSING IDs in HTML:', missingIds);
} else {
  console.log('SUCCESS: All', referencedIds.size, 'IDs exist in HTML markup!');
}

// 3. Check for Hammad and email
const hasHammad = html.includes('Hammad, AI Engineer') || html.includes('Hammad | AI Engineer');
const hasEmail = html.includes('aiwithhammad2026@gmail.com');
console.log('Creator Name included:', hasHammad);
console.log('Creator Email included:', hasEmail);

// 4. Extract <script> content and check syntax
const scriptStart = html.indexOf('<script>');
const scriptEnd = html.lastIndexOf('</script>');
const scriptContent = html.substring(scriptStart + 8, scriptEnd);

console.log('Script size:', scriptContent.length, 'characters');

const vm = require('vm');
try {
  new vm.Script(scriptContent);
  console.log('SUCCESS: Script syntax is 100% valid JavaScript!');
} catch (e) {
  console.error('SCRIPT SYNTAX ERROR:', e);
  process.exit(1);
}
