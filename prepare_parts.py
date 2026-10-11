import json
import html

# Read base64 dataset
with open('digits_dataset_b64.js', 'r') as f:
    b64_content = f.read().strip()
b64_str = b64_content.split('"')[1]

# Python code to embed
python_code_raw = '''import numpy as np
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

def highlight_python(code):
    lines = code.split('\n')
    highlighted_lines = []
    keywords = {'import', 'from', 'as', 'def', 'return', 'for', 'in', 'range', 'if', 'else', 'elif', 'while', 'True', 'False', 'None'}
    
    for line in lines:
        stripped = line.strip()
        if stripped.startswith('#'):
            highlighted_lines.append(f'<span class="tok-comment">{html.escape(line)}</span>')
            continue
        
        comment_part = ""
        code_part = line
        if '  #' in line:
            idx = line.find('  #')
            code_part = line[:idx]
            comment_part = f'<span class="tok-comment">{html.escape(line[idx:])}</span>'
        
        tokens = []
        words = code_part.split(' ')
        for w in words:
            clean_w = w.strip('(),:[]')
            if clean_w in keywords:
                w_escaped = html.escape(w)
                clean_escaped = html.escape(clean_w)
                tokens.append(w_escaped.replace(clean_escaped, f'<span class="tok-kw">{clean_escaped}</span>'))
            elif any(c in w for c in '0123456789') and not any(c in w for c in 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ_'):
                tokens.append(f'<span class="tok-num">{html.escape(w)}</span>')
            elif any(fn in w for fn in ['np.', 'load_digits', 'reshape', 'zeros', 'arange', 'random', 'normal', 'maximum', 'max', 'exp', 'sum', 'log', 'mean', 'argmax', 'print']):
                tokens.append(f'<span class="tok-fn">{html.escape(w)}</span>')
            else:
                tokens.append(html.escape(w))
        
        highlighted_lines.append(' '.join(tokens) + comment_part)
        
    return '\n'.join(highlighted_lines)

highlighted_py = highlight_python(python_code_raw)
print("Highlighted Python prepared.")

with open('template_parts.py', 'w') as f:
    f.write('b64_str = """' + b64_str + '"""\n')
    f.write('highlighted_py = """' + highlighted_py.replace('\\', '\\\\').replace('"""', '\\"\\"\\"') + '"""\n')
    f.write('python_code_raw = """' + python_code_raw.replace('\\', '\\\\').replace('"""', '\\"\\"\\"') + '"""\n')
print("Wrote template_parts.py")
