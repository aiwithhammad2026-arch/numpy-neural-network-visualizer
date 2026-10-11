import json
import base64

# Read base64 dataset
with open('digits_dataset_b64.js', 'r') as f:
    b64_content = f.read().strip()

# Extract just the raw b64 string
b64_str = b64_content.split('"')[1]

print("Dataset B64 string length:", len(b64_str))

# Python numpy code to embed in How It Works
python_code = '''import numpy as np
from sklearn.datasets import load_digits

# 1. Load 1,797 handwritten 8x8 digit images
digits = load_digits()
X = digits.images.reshape(-1, 64) / 16.0  # Scale pixels [0.0, 1.0]
y = digits.target
N = len(y)

# One-hot encode targets (N x 10)
Y = np.zeros((N, 10))
Y[np.arange(N), y] = 1.0

# 2. Initialize weights: Gaussian normal (std = 0.1), biases = 0
np.random.seed(42)
W1 = np.random.normal(0, 0.1, (64, 32))
b1 = np.zeros(32)
W2 = np.random.normal(0, 0.1, (32, 10))
b2 = np.zeros(10)

lr = 0.5
epochs = 300

# 3. Full-batch Gradient Descent
for step in range(1, epochs + 1):
    # --- Forward Pass ---
    z1 = X @ W1 + b1
    a1 = np.maximum(0, z1)              # ReLU activation
    z2 = a1 @ W2 + b2
    shift_z2 = z2 - np.max(z2, axis=1, keepdims=True)
    probs = np.exp(shift_z2) / np.sum(np.exp(shift_z2), axis=1, keepdims=True)  # Softmax

    # --- Metrics ---
    loss = -np.mean(np.log(probs[np.arange(N), y] + 1e-15))
    preds = np.argmax(probs, axis=1)
    acc = np.mean(preds == y)

    # --- Backpropagation ---
    dz2 = (probs - Y) / N               # Softmax + Cross-Entropy gradient
    dW2 = a1.T @ dz2
    db2 = np.sum(dz2, axis=0)

    da1 = dz2 @ W2.T
    dz1 = da1 * (z1 > 0)                # ReLU derivative
    dW1 = X.T @ dz1
    db1 = np.sum(dz1, axis=0)

    # --- Parameter Update ---
    W1 -= lr * dW1
    b1 -= lr * db1
    W2 -= lr * dW2
    b2 -= lr * db2

    if step % 50 == 0 or step == epochs:
        print(f"Step {step:3d}: Loss = {loss:.4f}, Accuracy = {acc * 100:.2f}%")
'''

print("Python code length:", len(python_code))
