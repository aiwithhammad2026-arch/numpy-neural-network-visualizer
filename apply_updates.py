# -*- coding: utf-8 -*-
with open('generate_final_page.py', 'r', encoding='utf-8') as f:
    text = f.read()

# 1. Update .credit-badge CSS
old_credit_css = """.credit-badge {
      display: inline-flex;
      align-items: center;
      gap: 6px;
      font-size: clamp(0.72rem, 0.85vw, 0.82rem);
      font-weight: 600;
      text-decoration: none;
      padding: 3px 10px;
      border-radius: 20px;
      background: rgba(255, 255, 255, 0.03);
      border: 1px solid var(--border-subtle);
      white-space: nowrap;
      cursor: pointer;
      transition: border-color 0.15s, background-color 0.15s;
    }

    .credit-badge:hover {
      border-color: var(--border-glow);
      background: rgba(0, 242, 254, 0.05);
    }

    .credit-gradient-text {
      background: linear-gradient(135deg, #00f2fe 0%, #a855f7 50%, #ff007f 100%);
      -webkit-background-clip: text;
      -webkit-text-fill-color: transparent;
      font-weight: 700;
    }"""

new_credit_css = """.credit-badge {
      display: inline-flex;
      align-items: center;
      gap: 8px;
      font-size: clamp(0.74rem, 0.88vw, 0.84rem);
      font-weight: 600;
      text-decoration: none;
      padding: 4px 12px;
      border-radius: 20px;
      background: rgba(255, 255, 255, 0.04);
      border: 1px solid var(--border-subtle);
      white-space: nowrap;
      cursor: pointer;
      transition: all 0.2s ease;
    }

    .credit-badge:hover {
      border-color: var(--cyan);
      background: rgba(0, 242, 254, 0.08);
      box-shadow: 0 0 15px rgba(0, 242, 254, 0.25);
    }

    .credit-gradient-text {
      background: linear-gradient(135deg, #00f2fe 0%, #c084fc 50%, #ff007f 100%);
      -webkit-background-clip: text;
      -webkit-text-fill-color: transparent;
      font-weight: 700;
      letter-spacing: -0.01em;
    }

    .credit-email-tag {
      font-size: 0.72rem;
      font-family: var(--font-mono);
      color: var(--cyan);
      opacity: 0.95;
      padding-left: 8px;
      border-left: 1px solid rgba(255, 255, 255, 0.18);
    }

    @media (max-width: 900px) {
      .credit-email-tag { display: none; }
    }"""

assert old_credit_css in text, "old_credit_css not found"
text = text.replace(old_credit_css, new_credit_css)

# 2. Update Header Brand & Right Badge
old_header_block = """    <div class="brand-group">
      <div class="brand-title">
        <span class="logo-dot"></span>
        <span>Neural Network from Scratch</span>
      </div>
      <div class="brand-subtitle">No PyTorch. No TensorFlow. Just math.</div>
    </div>

    <nav class="nav-links">
      <a href="#studio-section" class="nav-btn active" id="nav-studio">Studio</a>
      <a href="#draw-section" class="nav-btn" id="nav-draw">Draw & Test</a>
      <a href="#how-it-works-section" class="nav-btn" id="nav-how">How It Works</a>
    </nav>

    <div class="header-right">
      <a href="mailto:aiwithhammad2026@gmail.com" class="credit-badge" title="Contact Hammad, AI Engineer (aiwithhammad2026@gmail.com)">
        <span class="pulsing-dot"></span>
        <span class="credit-gradient-text">By Hammad, AI Engineer</span>
        <span style="opacity:0.75; font-size:0.7rem; font-family:var(--font-mono); margin-left:4px;">• aiwithhammad2026@gmail.com</span>
      </a>
      <div class="fps-badge" id="fps-counter">60 FPS</div>
    </div>"""

new_header_block = """    <div class="brand-group">
      <div class="brand-title">
        <span class="logo-dot"></span>
        <span>Neural Network from Scratch</span>
      </div>
      <div class="brand-subtitle">
        By <strong style="color:var(--cyan)">Hammad, AI Engineer</strong> &bull; <a href="mailto:aiwithhammad2026@gmail.com" style="color:var(--text-muted); text-decoration:none;">aiwithhammad2026@gmail.com</a>
      </div>
    </div>

    <nav class="nav-links">
      <a href="#studio-section" class="nav-btn active" id="nav-studio">Studio</a>
      <a href="#draw-section" class="nav-btn" id="nav-draw">Draw & Test</a>
      <a href="#how-it-works-section" class="nav-btn" id="nav-how">How It Works</a>
    </nav>

    <div class="header-right">
      <a href="mailto:aiwithhammad2026@gmail.com" class="credit-badge" title="Contact Hammad, AI Engineer (aiwithhammad2026@gmail.com)">
        <span class="pulsing-dot"></span>
        <span class="credit-gradient-text">By Hammad | AI Engineer</span>
        <span class="credit-email-tag">aiwithhammad2026@gmail.com</span>
      </a>
      <div class="fps-badge" id="fps-counter">60 FPS</div>
    </div>"""

assert old_header_block in text, "old_header_block not found"
text = text.replace(old_header_block, new_header_block)

# 3. Update Footer
old_footer = """  <!-- Footer -->
  <footer>
    <div>
      Designed &amp; built by <strong style="color:var(--cyan)">Hammad, AI Engineer</strong>
      <span style="opacity:0.4; margin:0 8px;">•</span>
      <a href="mailto:aiwithhammad2026@gmail.com" style="color:var(--purple); text-decoration:none;">aiwithhammad2026@gmail.com</a>
    </div>
    <button class="btn btn-sm" id="btn-back-to-top">↑ Back to top</button>
  </footer>"""

new_footer = """  <!-- Footer -->
  <footer>
    <div style="display:flex; align-items:center; justify-content:center; gap:10px; flex-wrap:wrap; font-size:0.88rem;">
      <span>Designed &amp; built by <strong style="color:var(--cyan); font-weight:700;">Hammad, AI Engineer</strong></span>
      <span style="opacity:0.4;">&bull;</span>
      <a href="mailto:aiwithhammad2026@gmail.com" style="color:var(--cyan); font-family:var(--font-mono); font-size:0.84rem; text-decoration:none; display:inline-flex; align-items:center; gap:5px; background:rgba(0,242,254,0.06); padding:3px 10px; border-radius:12px; border:1px solid rgba(0,242,254,0.2);">
        ✉ aiwithhammad2026@gmail.com
      </a>
    </div>
    <div style="font-size:0.75rem; color:var(--text-dim); margin-top:6px;">
      64 Inputs (8×8 digits) &rarr; 32 Hidden (ReLU) &rarr; 10 Outputs (Softmax) &bull; Pure JavaScript Backprop
    </div>
    <button class="btn btn-sm btn-subtle" id="btn-back-to-top" style="margin-top:10px;">↑ Back to top</button>
  </footer>"""

assert old_footer in text, "old_footer not found"
text = text.replace(old_footer, new_footer)

# 4. Update window.nn export
old_nn_init = """    // Instantiate Neural Network
    const nn = new NeuralNetwork();"""

new_nn_init = """    // Instantiate Neural Network
    const nn = new NeuralNetwork();
    window.nn = nn;"""

assert old_nn_init in text, "old_nn_init not found"
text = text.replace(old_nn_init, new_nn_init)

# 5. Update Connection Rendering
old_conn_render = """      // Top 15% strong connections
      const topCount = Math.round(allConns.length * 0.15);
      const topSet = new Set(allConns.slice(0, topCount));

      // Pick top ~250 for wave pulse carrying light
      topLightConnections = allConns.slice(0, Math.min(250, allConns.length));

      // Batch lines into Path2D
      const faintPath = new Path2D();
      const posPath = new Path2D();
      const negPath = new Path2D();

      for (let c of allConns) {
        if (!c.p1 || !c.p2) continue;
        if (topSet.has(c)) {
          if (c.w > 0) {
            posPath.moveTo(c.p1.x, c.p1.y);
            posPath.lineTo(c.p2.x, c.p2.y);
          } else {
            negPath.moveTo(c.p1.x, c.p1.y);
            negPath.lineTo(c.p2.x, c.p2.y);
          }
        } else {
          faintPath.moveTo(c.p1.x, c.p1.y);
          faintPath.lineTo(c.p2.x, c.p2.y);
        }
      }

      // 1. Draw 85% faint lines
      offscreenCtx.strokeStyle = 'rgba(255, 255, 255, 0.04)';
      offscreenCtx.lineWidth = 0.7;
      offscreenCtx.stroke(faintPath);

      // 2. Draw strong positive (Cyan)
      offscreenCtx.strokeStyle = 'rgba(0, 242, 254, 0.55)';
      offscreenCtx.lineWidth = 1.4;
      offscreenCtx.stroke(posPath);

      // 3. Draw strong negative (Pink)
      offscreenCtx.strokeStyle = 'rgba(255, 0, 127, 0.55)';
      offscreenCtx.lineWidth = 1.4;
      offscreenCtx.stroke(negPath);"""

new_conn_render = """      // Top 22% strong connections
      const topCount = Math.round(allConns.length * 0.22);
      const topSet = new Set(allConns.slice(0, topCount));

      // Pick top ~280 for wave pulse carrying light
      topLightConnections = allConns.slice(0, Math.min(280, allConns.length));

      // Batch lines into Path2D
      const faintPath = new Path2D();
      const posPath = new Path2D();
      const negPath = new Path2D();

      for (let c of allConns) {
        if (!c || !c.p1 || !c.p2) continue;
        if (topSet.has(c)) {
          if (c.w > 0) {
            posPath.moveTo(c.p1.x, c.p1.y);
            posPath.lineTo(c.p2.x, c.p2.y);
          } else {
            negPath.moveTo(c.p1.x, c.p1.y);
            negPath.lineTo(c.p2.x, c.p2.y);
          }
        } else {
          faintPath.moveTo(c.p1.x, c.p1.y);
          faintPath.lineTo(c.p2.x, c.p2.y);
        }
      }

      // 1. Draw baseline synaptic web (subtle crisp lines)
      offscreenCtx.strokeStyle = 'rgba(148, 163, 184, 0.12)';
      offscreenCtx.lineWidth = 0.8;
      offscreenCtx.stroke(faintPath);

      // 2. Draw strong positive (Electric Cyan)
      offscreenCtx.strokeStyle = 'rgba(0, 242, 254, 0.72)';
      offscreenCtx.lineWidth = 1.6;
      offscreenCtx.stroke(posPath);

      // 3. Draw strong negative (Neon Pink/Magenta)
      offscreenCtx.strokeStyle = 'rgba(255, 0, 127, 0.72)';
      offscreenCtx.lineWidth = 1.6;
      offscreenCtx.stroke(negPath);"""

assert old_conn_render in text, "old_conn_render not found"
text = text.replace(old_conn_render, new_conn_render)

# 6. Update Layer Headers on Canvas
old_headers = """      // --- DRAW LAYER HEADER BADGES DIRECTLY ON CANVAS ---
      ctx.font = '700 11px "JetBrains Mono", monospace';
      ctx.textBaseline = 'top';
      ctx.textAlign = 'center';
      if (inputPos.length > 0) {
        ctx.fillStyle = 'rgba(0, 242, 254, 0.75)';
        ctx.fillText('INPUT (64)', inputPos[0].x, 14);
      }
      if (hiddenPos.length > 0) {
        ctx.fillStyle = 'rgba(168, 85, 247, 0.75)';
        ctx.fillText('HIDDEN (32)', hiddenPos[0].x, 14);
      }
      if (outputPos.length > 0) {
        ctx.fillStyle = 'rgba(16, 185, 129, 0.75)';
        ctx.fillText('OUTPUT (10)', outputPos[0].x, 14);
      }"""

new_headers = """      // --- DRAW LAYER HEADER BADGES DIRECTLY ON CANVAS ---
      ctx.textAlign = 'center';
      ctx.textBaseline = 'middle';
      ctx.font = '700 11px "JetBrains Mono", monospace';

      if (inputPos.length > 0) {
        const x = inputPos[0].x;
        ctx.fillStyle = 'rgba(0, 242, 254, 0.14)';
        ctx.fillRect(x - 44, 10, 88, 20);
        ctx.strokeStyle = 'rgba(0, 242, 254, 0.5)';
        ctx.lineWidth = 1;
        ctx.strokeRect(x - 44, 10, 88, 20);
        ctx.fillStyle = '#00f2fe';
        ctx.fillText('INPUT (64)', x, 20);
      }
      if (hiddenPos.length > 0) {
        const x = hiddenPos[0].x;
        ctx.fillStyle = 'rgba(168, 85, 247, 0.14)';
        ctx.fillRect(x - 48, 10, 96, 20);
        ctx.strokeStyle = 'rgba(168, 85, 247, 0.5)';
        ctx.lineWidth = 1;
        ctx.strokeRect(x - 48, 10, 96, 20);
        ctx.fillStyle = '#c084fc';
        ctx.fillText('HIDDEN (32)', x, 20);
      }
      if (outputPos.length > 0) {
        const x = outputPos[0].x;
        ctx.fillStyle = 'rgba(16, 185, 129, 0.14)';
        ctx.fillRect(x - 48, 10, 96, 20);
        ctx.strokeStyle = 'rgba(16, 185, 129, 0.5)';
        ctx.lineWidth = 1;
        ctx.strokeRect(x - 48, 10, 96, 20);
        ctx.fillStyle = '#10b981';
        ctx.fillText('OUTPUT (10)', x, 20);
      }

      // --- ARCHITECTURE ANNOTATIONS AT CANVAS BOTTOM ---
      ctx.font = '500 10px "JetBrains Mono", monospace';
      ctx.fillStyle = 'rgba(148, 163, 184, 0.5)';
      if (inputPos.length > 0) {
        ctx.textAlign = 'left';
        ctx.fillText('• 64 Inputs (0–1)', Math.max(10, inputPos[0].x - 30), canvasHeight - 12);
      }
      if (hiddenPos.length > 0) {
        ctx.textAlign = 'center';
        ctx.fillText('• ReLU [max(0,z)]', hiddenPos[0].x, canvasHeight - 12);
      }
      if (outputPos.length > 0) {
        ctx.textAlign = 'left';
        ctx.fillText('• Softmax [0–9]', outputPos[0].x - 15, canvasHeight - 12);
      }"""

assert old_headers in text, "old_headers not found"
text = text.replace(old_headers, new_headers)

# 7. Update Nodes Rendering
old_nodes = """      // --- DRAW INPUT NODES (64) ---
      for (let i = 0; i < 64; i++) {
        const node = inputPos[i];
        if (!node) continue;
        const act = inputPixels[i];
        const trail = inputTrails[i];
        const intensity = Math.max(act, trail);

        ctx.beginPath();
        const r = node.r + intensity * 1.5;
        ctx.arc(node.x, node.y, r, 0, Math.PI * 2);
        if (intensity > 0.05) {
          ctx.fillStyle = `rgba(0, 242, 254, ${0.35 + intensity * 0.65})`;
          ctx.fill();
          ctx.strokeStyle = `rgba(0, 242, 254, ${0.7 + intensity * 0.3})`;
          ctx.lineWidth = 1.2;
          ctx.stroke();

          // Glow sprite
          ctx.save();
          ctx.globalCompositeOperation = 'lighter';
          const gr = (r + 4) * (1 + intensity);
          ctx.drawImage(spriteCyan, node.x - gr, node.y - gr, gr * 2, gr * 2);
          ctx.restore();
        } else {
          ctx.fillStyle = 'rgba(255, 255, 255, 0.12)';
          ctx.fill();
          ctx.strokeStyle = 'rgba(255, 255, 255, 0.2)';
          ctx.lineWidth = 0.8;
          ctx.stroke();
        }
      }

      // --- DRAW HIDDEN NODES (32) ---
      for (let j = 0; j < 32; j++) {
        const node = hiddenPos[j];
        if (!node) continue;
        const act = Math.min(1.0, a1[j] * 0.6);
        const trail = hiddenTrails[j];
        const intensity = Math.max(act, trail);

        ctx.beginPath();
        const r = node.r + intensity * 2.0;
        ctx.arc(node.x, node.y, r, 0, Math.PI * 2);
        if (intensity > 0.05) {
          ctx.fillStyle = `rgba(168, 85, 247, ${0.45 + intensity * 0.55})`;
          ctx.fill();
          ctx.strokeStyle = `rgba(192, 132, 252, ${0.7 + intensity * 0.3})`;
          ctx.lineWidth = 1.4;
          ctx.stroke();

          ctx.save();
          ctx.globalCompositeOperation = 'lighter';
          const gr = (r + 6) * (1 + intensity);
          ctx.drawImage(spritePurple, node.x - gr, node.y - gr, gr * 2, gr * 2);
          ctx.restore();
        } else {
          ctx.fillStyle = 'rgba(255, 255, 255, 0.14)';
          ctx.fill();
          ctx.strokeStyle = 'rgba(255, 255, 255, 0.22)';
          ctx.lineWidth = 0.8;
          ctx.stroke();
        }
      }

      // --- DRAW OUTPUT NODES (10) & LIVE LABELS ---
      ctx.textBaseline = 'middle';

      for (let k = 0; k < 10; k++) {
        const node = outputPos[k];
        if (!node) continue;
        const p = probs[k];
        const isPredicted = (k === predictedDigit);
        const isTarget = (k === targetDigit);
        const trail = outputTrails[k];
        const intensity = Math.max(p, trail);

        // Target ring
        if (isTarget) {
          ctx.beginPath();
          ctx.arc(node.x, node.y, node.r + 6, 0, Math.PI * 2);
          ctx.strokeStyle = '#10b981';
          ctx.lineWidth = 2.5;
          ctx.stroke();
        }

        // Main node circle
        ctx.beginPath();
        ctx.arc(node.x, node.y, node.r, 0, Math.PI * 2);
        if (isPredicted) {
          ctx.fillStyle = '#00f2fe';
        } else if (isTarget) {
          ctx.fillStyle = 'rgba(16, 185, 129, 0.75)';
        } else {
          ctx.fillStyle = `rgba(255, 255, 255, ${0.15 + intensity * 0.65})`;
        }
        ctx.fill();
        ctx.strokeStyle = isPredicted ? '#ffffff' : (isTarget ? '#10b981' : 'rgba(255, 255, 255, 0.3)');
        ctx.lineWidth = 1.5;
        ctx.stroke();

        // Glowing prediction aura
        if (isPredicted || intensity > 0.25) {
          ctx.save();
          ctx.globalCompositeOperation = 'lighter';
          const gr = (node.r + 14) * (1 + intensity * 0.5);
          ctx.drawImage(isPredicted ? spriteCyan : spriteGreen, node.x - gr, node.y - gr, gr * 2, gr * 2);
          ctx.restore();
        }

        // Output digit text inside node
        ctx.fillStyle = isPredicted ? '#07080d' : '#f8fafc';
        ctx.textAlign = 'center';
        ctx.font = '700 11px "JetBrains Mono", monospace';
        ctx.fillText(k.toString(), node.x, node.y);

        // Output Label [k]  XX.X%
        ctx.textAlign = 'left';
        const labelX = node.x + node.r + 10;
        const pctStr = (p * 100).toFixed(1) + '%';
        ctx.font = isPredicted ? '700 12px "JetBrains Mono", monospace' : '500 11px "JetBrains Mono", monospace';
        ctx.fillStyle = isPredicted ? '#00f2fe' : (isTarget ? '#10b981' : 'rgba(148, 163, 184, 0.85)');
        ctx.fillText(`[${k}]  ${pctStr}`, labelX, node.y);
      }"""

new_nodes = """      // --- DRAW INPUT NODES (64) ---
      for (let i = 0; i < 64; i++) {
        const node = inputPos[i];
        if (!node) continue;
        const act = inputPixels[i];
        const trail = inputTrails[i];
        const intensity = Math.max(act, trail);

        ctx.beginPath();
        const r = node.r + intensity * 1.5;
        ctx.arc(node.x, node.y, r, 0, Math.PI * 2);
        if (intensity > 0.05) {
          ctx.fillStyle = '#00f2fe';
          ctx.fill();
          ctx.strokeStyle = '#ffffff';
          ctx.lineWidth = 1.5;
          ctx.stroke();

          // Glow sprite
          ctx.save();
          ctx.globalCompositeOperation = 'lighter';
          const gr = (r + 4) * (1 + intensity * 0.8);
          ctx.drawImage(spriteCyan, node.x - gr, node.y - gr, gr * 2, gr * 2);
          ctx.restore();
        } else {
          ctx.fillStyle = 'rgba(15, 23, 42, 0.9)';
          ctx.fill();
          ctx.strokeStyle = 'rgba(148, 163, 184, 0.45)';
          ctx.lineWidth = 1.0;
          ctx.stroke();
        }
      }

      // --- DRAW HIDDEN NODES (32) ---
      for (let j = 0; j < 32; j++) {
        const node = hiddenPos[j];
        if (!node) continue;
        const act = Math.min(1.0, a1[j] * 0.6);
        const trail = hiddenTrails[j];
        const intensity = Math.max(act, trail);

        ctx.beginPath();
        const r = node.r + intensity * 2.0;
        ctx.arc(node.x, node.y, r, 0, Math.PI * 2);
        if (intensity > 0.05) {
          ctx.fillStyle = '#a855f7';
          ctx.fill();
          ctx.strokeStyle = '#f8fafc';
          ctx.lineWidth = 1.6;
          ctx.stroke();

          ctx.save();
          ctx.globalCompositeOperation = 'lighter';
          const gr = (r + 6) * (1 + intensity * 0.8);
          ctx.drawImage(spritePurple, node.x - gr, node.y - gr, gr * 2, gr * 2);
          ctx.restore();
        } else {
          ctx.fillStyle = 'rgba(25, 20, 45, 0.9)';
          ctx.fill();
          ctx.strokeStyle = 'rgba(168, 85, 247, 0.45)';
          ctx.lineWidth = 1.0;
          ctx.stroke();
        }
      }

      // --- DRAW OUTPUT NODES (10) & LIVE LABELS ---
      ctx.textBaseline = 'middle';

      for (let k = 0; k < 10; k++) {
        const node = outputPos[k];
        if (!node) continue;
        const p = probs[k];
        const isPredicted = (k === predictedDigit);
        const isTarget = (k === targetDigit);
        const trail = outputTrails[k];
        const intensity = Math.max(p, trail);

        // Target ring (Emerald)
        if (isTarget) {
          ctx.beginPath();
          ctx.arc(node.x, node.y, node.r + 6, 0, Math.PI * 2);
          ctx.strokeStyle = '#10b981';
          ctx.lineWidth = 2.5;
          ctx.stroke();
        }

        // Main node circle
        ctx.beginPath();
        ctx.arc(node.x, node.y, node.r, 0, Math.PI * 2);
        if (isPredicted) {
          ctx.fillStyle = '#00f2fe';
        } else if (isTarget) {
          ctx.fillStyle = '#10b981';
        } else {
          ctx.fillStyle = `rgba(30, 41, 59, ${0.85 + intensity * 0.15})`;
        }
        ctx.fill();
        ctx.strokeStyle = isPredicted ? '#ffffff' : (isTarget ? '#34d399' : 'rgba(148, 163, 184, 0.5)');
        ctx.lineWidth = 1.8;
        ctx.stroke();

        // Glowing prediction aura
        if (isPredicted || intensity > 0.25) {
          ctx.save();
          ctx.globalCompositeOperation = 'lighter';
          const gr = (node.r + 14) * (1 + intensity * 0.5);
          ctx.drawImage(isPredicted ? spriteCyan : spriteGreen, node.x - gr, node.y - gr, gr * 2, gr * 2);
          ctx.restore();
        }

        // Output digit text inside node
        ctx.fillStyle = isPredicted ? '#07080d' : '#f8fafc';
        ctx.textAlign = 'center';
        ctx.font = '800 12px "JetBrains Mono", monospace';
        ctx.fillText(k.toString(), node.x, node.y);

        // Output Label [k]  XX.X%
        ctx.textAlign = 'left';
        const labelX = node.x + node.r + 12;
        const pctStr = (p * 100).toFixed(1) + '%';
        ctx.font = isPredicted ? '700 13px "JetBrains Mono", monospace' : '600 11px "JetBrains Mono", monospace';
        ctx.fillStyle = isPredicted ? '#00f2fe' : (isTarget ? '#10b981' : 'rgba(203, 213, 225, 0.9)');
        ctx.fillText(`[${k}]  ${pctStr}`, labelX, node.y);
      }"""

assert old_nodes in text, "old_nodes not found"
text = text.replace(old_nodes, new_nodes)

# 8. Save updated generate_final_page.py
with open('generate_final_page.py', 'w', encoding='utf-8') as f:
    f.write(text)

print("generate_final_page.py updated successfully!")
