const fs = require('fs');
eval(fs.readFileSync('digits_dataset_b64.js', 'utf-8'));

// Decode base64 in node / browser
const binaryStr = Buffer.from(DIGITS_B64, 'base64');
const N = 1797;
const X = new Float32Array(N * 64);
const y = new Int32Array(N);

let ptr = 0;
for (let s = 0; s < N; s++) {
  y[s] = binaryStr[ptr++];
  for (let i = 0; i < 64; i++) {
    X[s * 64 + i] = binaryStr[ptr++] / 16.0;
  }
}

console.log('Decoded dataset: N =', N, 'y[0] =', y[0], 'X[0, 2] =', X[2]);

// Gaussian random normal generator
function randn() {
  let u = 0, v = 0;
  while (u === 0) u = Math.random();
  while (v === 0) v = Math.random();
  return Math.sqrt(-2.0 * Math.log(u)) * Math.cos(2.0 * Math.PI * v);
}

// Weights: normal std 0.1
const W1 = new Float32Array(64 * 32);
const b1 = new Float32Array(32);
const W2 = new Float32Array(32 * 10);
const b2 = new Float32Array(10);

for (let i = 0; i < W1.length; i++) W1[i] = randn() * 0.1;
for (let i = 0; i < W2.length; i++) W2[i] = randn() * 0.1;

// Pre-allocate buffers for full-batch to avoid any GC or memory overhead
const Z1 = new Float32Array(N * 32);
const A1 = new Float32Array(N * 32);
const Z2 = new Float32Array(N * 10);
const Probs = new Float32Array(N * 10);
const dZ2 = new Float32Array(N * 10);
const dA1 = new Float32Array(N * 32);
const dZ1 = new Float32Array(N * 32);

const dW1 = new Float32Array(64 * 32);
const db1 = new Float32Array(32);
const dW2 = new Float32Array(32 * 10);
const db2 = new Float32Array(10);

function trainStep(lr = 0.5) {
  // 1. Z1 = X @ W1 + b1
  for (let s = 0; s < N; s++) {
    const xOff = s * 64;
    const zOff = s * 32;
    for (let j = 0; j < 32; j++) {
      let sum = b1[j];
      for (let i = 0; i < 64; i++) {
        sum += X[xOff + i] * W1[i * 32 + j];
      }
      Z1[zOff + j] = sum;
      A1[zOff + j] = sum > 0 ? sum : 0; // ReLU
    }
  }

  // 2. Z2 = A1 @ W2 + b2 & Softmax
  let totalLoss = 0;
  let correct = 0;

  for (let s = 0; s < N; s++) {
    const aOff = s * 32;
    const z2Off = s * 10;
    let maxZ = -Infinity;
    for (let k = 0; k < 10; k++) {
      let sum = b2[k];
      for (let j = 0; j < 32; j++) {
        sum += A1[aOff + j] * W2[j * 10 + k];
      }
      Z2[z2Off + k] = sum;
      if (sum > maxZ) maxZ = sum;
    }

    let sumExp = 0;
    for (let k = 0; k < 10; k++) {
      const e = Math.exp(Z2[z2Off + k] - maxZ);
      Probs[z2Off + k] = e;
      sumExp += e;
    }

    const invSum = 1.0 / sumExp;
    let maxP = -1, pred = 0;
    const target = y[s];
    for (let k = 0; k < 10; k++) {
      const p = Probs[z2Off + k] * invSum;
      Probs[z2Off + k] = p;
      if (p > maxP) { maxP = p; pred = k; }
      dZ2[z2Off + k] = (p - (k === target ? 1 : 0)) / N;
    }
    if (pred === target) correct++;
    totalLoss += -Math.log(Math.max(Probs[z2Off + target], 1e-15));
  }

  // 3. Gradients for W2 and b2: dW2 = A1.T @ dZ2, db2 = sum(dZ2)
  dW2.fill(0);
  db2.fill(0);
  for (let s = 0; s < N; s++) {
    const aOff = s * 32;
    const dzOff = s * 10;
    for (let k = 0; k < 10; k++) {
      const dzk = dZ2[dzOff + k];
      db2[k] += dzk;
      for (let j = 0; j < 32; j++) {
        dW2[j * 10 + k] += A1[aOff + j] * dzk;
      }
    }
  }

  // 4. Backprop to hidden: dA1 = dZ2 @ W2.T, dZ1 = dA1 * (Z1 > 0)
  // And dW1 = X.T @ dZ1, db1 = sum(dZ1)
  dW1.fill(0);
  db1.fill(0);
  for (let s = 0; s < N; s++) {
    const dzOff = s * 10;
    const xOff = s * 64;
    const zOff = s * 32;
    for (let j = 0; j < 32; j++) {
      if (Z1[zOff + j] <= 0) continue; // ReLU derivative is 0
      let dz1_val = 0;
      for (let k = 0; k < 10; k++) {
        dz1_val += dZ2[dzOff + k] * W2[j * 10 + k];
      }
      db1[j] += dz1_val;
      for (let i = 0; i < 64; i++) {
        const xi = X[xOff + i];
        if (xi !== 0) {
          dW1[i * 32 + j] += xi * dz1_val;
        }
      }
    }
  }

  // 5. Update weights
  for (let i = 0; i < W1.length; i++) W1[i] -= lr * dW1[i];
  for (let j = 0; j < b1.length; j++) b1[j] -= lr * db1[j];
  for (let i = 0; i < W2.length; i++) W2[i] -= lr * dW2[i];
  for (let k = 0; k < b2.length; k++) b2[k] -= lr * db2[k];

  return { loss: totalLoss / N, accuracy: correct / N };
}

console.log('Testing speed of 300 steps...');
const t0 = Date.now();
for (let step = 1; step <= 300; step++) {
  const res = trainStep(0.5);
  if (step % 50 === 0 || step === 300 || step === 1) {
    console.log(`Step ${step}: Loss = ${res.loss.toFixed(4)}, Accuracy = ${(res.accuracy*100).toFixed(2)}%`);
  }
}
const dt = Date.now() - t0;
console.log(`300 steps finished in ${dt} ms (${(dt / 300).toFixed(2)} ms/step)!`);
