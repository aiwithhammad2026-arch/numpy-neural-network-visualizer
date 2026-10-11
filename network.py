"""
Neural Network from Scratch
===========================
A 64 -> 32 -> 10 Multilayer Perceptron built using pure NumPy with full-batch
backpropagation for handwritten digit classification (scikit-learn load_digits).

Architecture:
- Input: 64 pixels (8x8 digits, normalized to [0, 1])
- Hidden Layer: 32 units with ReLU activation
- Output Layer: 10 units with Softmax probabilities
- Optimizer: Full-batch Gradient Descent (learning rate = 0.5, 300 steps)

Built by Hammad, AI Engineer
Email: aiwithhammad2026@gmail.com
"""

import numpy as np
from sklearn.datasets import load_digits


def train_network(epochs=300, lr=0.5, random_seed=42):
    # 1. Load 1,797 handwritten 8x8 digit images
    digits = load_digits()
    X = digits.images.reshape(-1, 64) / 16.0  # Scale pixels [0.0, 1.0]
    y = digits.target
    N = len(y)

    # One-hot encode targets (N x 10)
    Y = np.zeros((N, 10))
    Y[np.arange(N), y] = 1.0

    # 2. Initialize weights: Gaussian normal (std = 0.1), biases = 0
    np.random.seed(random_seed)
    W1 = np.random.normal(0, 0.1, (64, 32))
    b1 = np.zeros(32)
    W2 = np.random.normal(0, 0.1, (32, 10))
    b2 = np.zeros(10)

    print(f"Training on {N} samples (64 -> 32 -> 10) for {epochs} steps at lr={lr}...\n")

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

        if step % 50 == 0 or step == epochs or step == 1:
            print(f"Step {step:3d}: Loss = {loss:.4f}, Accuracy = {acc * 100:.2f}%")

    return {"W1": W1, "b1": b1, "W2": W2, "b2": b2, "final_loss": loss, "final_acc": acc}


if __name__ == "__main__":
    train_network()
