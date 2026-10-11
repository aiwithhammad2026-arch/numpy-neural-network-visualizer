const fs = require('fs');
const datasetCode = fs.readFileSync('dataset_js.txt', 'utf-8');

// evaluate dataset
const sandbox = {};
const fn = new Function(datasetCode + '; return RAW_DIGITS_DATA;');
const rawData = fn();

const DATASET = rawData.map(str => {
  const label = parseInt(str[0], 10);
  const hex = str.slice(2);
  const pixels = new Float32Array(64);
  for (let i = 0; i < 64; i++) {
    pixels[i] = parseInt(hex[i], 16) / 15.0;
  }
  return { label, pixels, hex };
});

console.log('Dataset loaded in JS, total:', DATASET.length);

class NeuralNetwork {
  constructor(inputSize = 64, hiddenSize = 32, outputSize = 10) {
    this.inputSize = inputSize;
    this.hiddenSize = hiddenSize;
    this.outputSize = outputSize;
    this.reset();
  }

  reset() {
    this.step = 0;
    this.history = [];
    const scale1 = Math.sqrt(2.0 / this.inputSize);
    const scale2 = Math.sqrt(2.0 / this.hiddenSize);
    this.W1 = new Float32Array(this.inputSize * this.hiddenSize);
    this.b1 = new Float32Array(this.hiddenSize);
    this.W2 = new Float32Array(this.hiddenSize * this.outputSize);
    this.b2 = new Float32Array(this.outputSize);
    for (let i = 0; i < this.W1.length; i++) this.W1[i] = (Math.random() * 2 - 1) * scale1;
    for (let i = 0; i < this.W2.length; i++) this.W2[i] = (Math.random() * 2 - 1) * scale2;
  }

  forward(x) {
    const z1 = new Float32Array(this.hiddenSize);
    const a1 = new Float32Array(this.hiddenSize);
    for (let j = 0; j < this.hiddenSize; j++) {
      let sum = this.b1[j];
      for (let i = 0; i < this.inputSize; i++) {
        sum += x[i] * this.W1[i * this.hiddenSize + j];
      }
      z1[j] = sum;
      a1[j] = sum > 0 ? sum : 0;
    }
    const z2 = new Float32Array(this.outputSize);
    let maxZ = -Infinity;
    for (let k = 0; k < this.outputSize; k++) {
      let sum = this.b2[k];
      for (let j = 0; j < this.hiddenSize; j++) {
        sum += a1[j] * this.W2[j * this.outputSize + k];
      }
      z2[k] = sum;
      if (sum > maxZ) maxZ = sum;
    }
    const probs = new Float32Array(this.outputSize);
    let sumExp = 0;
    for (let k = 0; k < this.outputSize; k++) {
      const e = Math.exp(z2[k] - maxZ);
      probs[k] = e;
      sumExp += e;
    }
    for (let k = 0; k < this.outputSize; k++) probs[k] /= sumExp;
    return { z1, a1, z2, probs };
  }

  evaluate(dataset) {
    let correct = 0;
    let totalLoss = 0;
    for (let s of dataset) {
      const { probs } = this.forward(s.pixels);
      let pred = 0, maxP = -1;
      for (let k = 0; k < 10; k++) {
        if (probs[k] > maxP) { maxP = probs[k]; pred = k; }
      }
      if (pred === s.label) correct++;
      totalLoss += -Math.log(Math.max(probs[s.label], 1e-15));
    }
    return { accuracy: correct / dataset.length, loss: totalLoss / dataset.length };
  }

  trainStep(dataset, lr = 0.5) {
    const N = dataset.length;
    const dW1 = new Float32Array(this.inputSize * this.hiddenSize);
    const db1 = new Float32Array(this.hiddenSize);
    const dW2 = new Float32Array(this.hiddenSize * this.outputSize);
    const db2 = new Float32Array(this.outputSize);

    let totalLoss = 0;
    let correct = 0;

    for (let s = 0; s < N; s++) {
      const { pixels, label } = dataset[s];
      const { z1, a1, probs } = this.forward(pixels);
      let pred = 0, maxP = -1;
      for (let k = 0; k < 10; k++) {
        if (probs[k] > maxP) { maxP = probs[k]; pred = k; }
      }
      if (pred === label) correct++;
      totalLoss += -Math.log(Math.max(probs[label], 1e-15));

      const dz2 = new Float32Array(10);
      for (let k = 0; k < 10; k++) {
        dz2[k] = probs[k] - (k === label ? 1.0 : 0.0);
      }

      for (let j = 0; j < this.hiddenSize; j++) {
        const aj = a1[j];
        if (aj === 0) continue;
        const rowOffset = j * this.outputSize;
        for (let k = 0; k < 10; k++) {
          dW2[rowOffset + k] += aj * dz2[k];
        }
      }
      for (let k = 0; k < 10; k++) db2[k] += dz2[k];

      const dz1 = new Float32Array(this.hiddenSize);
      for (let j = 0; j < this.hiddenSize; j++) {
        if (z1[j] <= 0) continue;
        let sum = 0;
        const rowOffset = j * this.outputSize;
        for (let k = 0; k < 10; k++) {
          sum += dz2[k] * this.W2[rowOffset + k];
        }
        dz1[j] = sum;
      }

      for (let i = 0; i < this.inputSize; i++) {
        const xi = pixels[i];
        if (xi === 0) continue;
        const rowOffset = i * this.hiddenSize;
        for (let j = 0; j < this.hiddenSize; j++) {
          if (dz1[j] !== 0) dW1[rowOffset + j] += xi * dz1[j];
        }
      }
      for (let j = 0; j < this.hiddenSize; j++) db1[j] += dz1[j];
    }

    const factor = lr / N;
    for (let i = 0; i < this.W1.length; i++) this.W1[i] -= factor * dW1[i];
    for (let j = 0; j < this.b1.length; j++) this.b1[j] -= factor * db1[j];
    for (let i = 0; i < this.W2.length; i++) this.W2[i] -= factor * dW2[i];
    for (let k = 0; k < this.b2.length; k++) this.b2[k] -= factor * db2[k];

    this.step++;
    const avgLoss = totalLoss / N;
    const acc = correct / N;
    this.history.push({ step: this.step, loss: avgLoss, accuracy: acc });
    return { step: this.step, loss: avgLoss, accuracy: acc };
  }
}

const nn = new NeuralNetwork();
console.log('Step 0 (Untrained):', nn.evaluate(DATASET));

const t0 = Date.now();
for (let i = 1; i <= 300; i++) {
  const res = nn.trainStep(DATASET, 0.65);
  if (i % 50 === 0 || i === 300) {
    console.log('Step ' + i + ':', `Accuracy: ${(res.accuracy*100).toFixed(1)}%, Loss: ${res.loss.toFixed(4)}`);
  }
}
console.log('Trained 300 steps in ' + (Date.now() - t0) + ' ms!');
