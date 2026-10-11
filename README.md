# Neural Network from Scratch

> **No PyTorch. No TensorFlow. Just NumPy, plus an interactive visualizer.**

[![Live Demo](https://img.shields.io/badge/Live_Demo-GitHub_Pages-00f2fe?style=for-the-badge)](https://<username>.github.io/neural-network-from-scratch/)
[![License: MIT](https://img.shields.io/badge/License-MIT-10b981?style=for-the-badge)](LICENSE)
[![Python: 3.8+](https://img.shields.io/badge/Python-3.8+-8b5cf6?style=for-the-badge)](https://www.python.org/)

---

## 🌐 Live Demo
Experience the real-time neural network learning in your browser:
👉 **[Launch Interactive Visualizer](https://<username>.github.io/neural-network-from-scratch/)** *(Placeholder)*

---

## 🧠 What It Does
- **Architecture**: **64 Inputs** $\to$ **32 Hidden Neurons (ReLU)** $\to$ **10 Outputs (Softmax)**
- **Dataset**: Built-in scikit-learn digits dataset containing **1,797 handwritten 8×8 pixel images** (scaled to [0.0, 1.0]).
- **Optimization**: Full-batch Gradient Descent with learning rate $\eta = 0.5$, normal weight initialization ($\sigma = 0.1$), and biases initialized to 0.
- **Learning Performance**: Advances from **~10.1% untrained baseline** to **~98.3% accuracy** within **300 steps** (crossing 95% milestone around step ~100).
- **Interactive Visualizer (`index.html`)**: Single-file, zero-dependency browser application featuring:
  - Real-time 60–240 FPS canvas rendering of synaptic weights and active neurons.
  - Forward pulse energy packet waves and Backprop weight update animations.
  - Interactive 8×8 drawing canvas to sketch your own digits and test network predictions live.
  - Syntax-highlighted Python NumPy reference code and learning curves.

---

## 🚀 Getting Started

### 1. Run the Python Model (NumPy)
Clone this repository and run the standalone training script:

```bash
git clone https://github.com/<username>/neural-network-from-scratch.git
cd neural-network-from-scratch

# Install dependencies
pip install -r requirements.txt

# Run training
python network.py
```

#### Sample Terminal Output:
```text
Training on 1797 samples (64 -> 32 -> 10) for 300 steps at lr=0.5...

Step   1: Loss = 2.3157, Accuracy = 11.07%
Step  50: Loss = 0.4570, Accuracy = 91.32%
Step 100: Loss = 0.2054, Accuracy = 95.66%
Step 150: Loss = 0.1472, Accuracy = 96.88%
Step 200: Loss = 0.1171, Accuracy = 97.55%
Step 250: Loss = 0.0982, Accuracy = 97.94%
Step 300: Loss = 0.0846, Accuracy = 98.27%
```

---

### 2. Run the Interactive Web Visualizer (`index.html`)
The interactive studio is completely self-contained with zero external dependencies and runs 100% offline:

- **Option A (Direct)**: Double-click `index.html` to open it in your browser.
- **Option B (Local Web Server)**:
  ```bash
  python -m http.server 8080
  ```
  Then navigate to `http://localhost:8080/index.html`.

---

## 📁 Repository Structure
```text
├── index.html          # Complete standalone animated visualizer (HTML5, Canvas, CSS, vanilla JS)
├── network.py          # Pure NumPy neural network implementation with full-batch backprop
├── requirements.txt    # Python requirements (numpy, scikit-learn)
├── LICENSE             # MIT License
├── README.md           # Documentation & guides
└── .gitignore          # Git ignore rules
```

---

## 👨‍💻 Author & Credits
**Built by Hammad, AI Engineer**
- Email: [aiwithhammad2026@gmail.com](mailto:aiwithhammad2026@gmail.com)
