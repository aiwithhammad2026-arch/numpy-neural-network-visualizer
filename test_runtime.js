const fs = require('fs');
const vm = require('vm');

const html = fs.readFileSync('index.html', 'utf8');
const scriptStart = html.indexOf('<script>');
const scriptEnd = html.lastIndexOf('</script>');
const scriptContent = html.substring(scriptStart + 8, scriptEnd);

// Create canvas mock
function createMockCanvas() {
  const drawCalls = [];
  const ctx = {
    fillStyle: '',
    strokeStyle: '',
    lineWidth: 1,
    font: '',
    textAlign: '',
    textBaseline: '',
    globalCompositeOperation: '',
    globalAlpha: 1,
    imageSmoothingEnabled: true,
    fillRect: (...args) => drawCalls.push(['fillRect', ...args]),
    strokeRect: (...args) => drawCalls.push(['strokeRect', ...args]),
    clearRect: (...args) => drawCalls.push(['clearRect', ...args]),
    beginPath: () => drawCalls.push(['beginPath']),
    arc: (...args) => drawCalls.push(['arc', ...args]),
    fill: () => drawCalls.push(['fill']),
    stroke: () => drawCalls.push(['stroke']),
    moveTo: (...args) => drawCalls.push(['moveTo', ...args]),
    lineTo: (...args) => drawCalls.push(['lineTo', ...args]),
    fillText: (...args) => drawCalls.push(['fillText', ...args]),
    drawImage: (...args) => drawCalls.push(['drawImage', ...args]),
    setTransform: (...args) => drawCalls.push(['setTransform', ...args]),
    save: () => drawCalls.push(['save']),
    restore: () => drawCalls.push(['restore']),
    translate: (...args) => drawCalls.push(['translate', ...args]),
    rotate: (...args) => drawCalls.push(['rotate', ...args]),
    createRadialGradient: () => ({
      addColorStop: () => {}
    }),
    getImageData: () => ({ data: new Uint8ClampedArray(8 * 8 * 4) })
  };

  return {
    width: 800,
    height: 600,
    style: {},
    getContext: () => ctx,
    getBoundingClientRect: () => ({ width: 800, height: 600, top: 0, left: 0, bottom: 600, right: 800 }),
    clientWidth: 800,
    clientHeight: 600,
    parentElement: {
      getBoundingClientRect: () => ({ width: 400, height: 120 })
    },
    addEventListener: () => {},
    removeEventListener: () => {}
  };
}

// Create DOM elements mock
const elements = {};
function getMockElement(id) {
  if (!elements[id]) {
    const isCanvas = id.includes('canvas');
    const base = isCanvas ? createMockCanvas() : {
      style: {},
      classList: {
        add: () => {},
        remove: () => {},
        toggle: () => {},
        contains: () => false
      },
      textContent: '',
      innerHTML: '',
      value: '',
      dataset: {},
      getBoundingClientRect: () => ({ width: 800, height: 600, top: 0, left: 0 }),
      clientWidth: 800,
      clientHeight: 600,
      addEventListener: () => {},
      appendChild: () => {},
      children: [],
      querySelector: () => ({ style: {}, classList: { toggle: () => {} }, textContent: '' }),
      querySelectorAll: () => [],
      parentElement: {
        getBoundingClientRect: () => ({ width: 400, height: 120 })
      }
    };
    elements[id] = base;
  }
  return elements[id];
}

let animationFrameCallback = null;

const sandbox = {
  console: console,
  window: {
    devicePixelRatio: 1.5,
    innerWidth: 1440,
    innerHeight: 900,
    addEventListener: () => {},
    removeEventListener: () => {},
    scrollTo: () => {}
  },
  document: {
    getElementById: (id) => getMockElement(id),
    createElement: (tag) => {
      if (tag === 'canvas') return createMockCanvas();
      return {
        style: {},
        classList: { add: () => {}, remove: () => {}, toggle: () => {} },
        dataset: {},
        appendChild: () => {},
        addEventListener: () => {},
        querySelector: () => ({ style: {}, classList: { toggle: () => {} }, textContent: '' }),
        querySelectorAll: () => []
      };
    },
    querySelectorAll: () => [],
    addEventListener: () => {}
  },
  ResizeObserver: class {
    observe() {}
    unobserve() {}
    disconnect() {}
  },
  requestAnimationFrame: (cb) => {
    animationFrameCallback = cb;
    return 1;
  },
  cancelAnimationFrame: () => {},
  setTimeout: (cb, ms) => setTimeout(cb, ms),
  clearTimeout: (id) => clearTimeout(id),
  performance: {
    now: () => Date.now()
  },
  Path2D: class {
    moveTo() {}
    lineTo() {}
    arc() {}
  },
  Float32Array,
  Uint8ClampedArray,
  Math,
  atob: (b64) => Buffer.from(b64, 'base64').toString('binary'),
  btoa: (str) => Buffer.from(str, 'binary').toString('base64')
};

sandbox.window.document = sandbox.document;
sandbox.global = sandbox;

const context = vm.createContext(sandbox);

try {
  console.log('Running script execution in simulated DOM...');
  vm.runInContext(scriptContent, context);
  console.log('Script executed successfully without throwing!');

  // Now test 10 frames of renderLoop
  if (animationFrameCallback) {
    console.log('Simulating 10 animation frames of renderLoop...');
    for (let f = 1; f <= 10; f++) {
      const cb = animationFrameCallback;
      animationFrameCallback = null;
      cb(Date.now() + f * 16.6);
    }
    console.log('SUCCESS: 10 frames rendered cleanly without error!');

    // Test training steps
    console.log('Testing training steps and animations...');
    const nn = sandbox.window.nn;
    console.log('Found neural network instance:', !!nn);
    console.log('Testing nn.trainStep() for 300 steps...');
    for (let s = 1; s <= 300; s++) {
      const res = nn.trainStep(0.5);
      if (s === 1 || s === 50 || s === 100 || s === 300) {
        console.log(`Step ${res.step}: Loss = ${res.loss.toFixed(4)}, Acc = ${(res.accuracy * 100).toFixed(2)}%`);
      }
      // Render frame during training
      if (animationFrameCallback) {
        const cb = animationFrameCallback;
        animationFrameCallback = null;
        cb(Date.now() + s * 16.6);
      }
    }
    console.log('SUCCESS: Complete 300 steps of training & render loop ran flawlessly!');
  } else {
    console.warn('No requestAnimationFrame callback registered!');
  }
} catch (err) {
  console.error('RUNTIME ERROR IN SCRIPT:', err);
  process.exit(1);
}
