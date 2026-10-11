import json

# Read the generated dataset
with open('dataset_js.txt', 'r') as f:
    dataset_code = f.read().strip()

html_template = f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Neural Network from Scratch | Interactive Deep Learning Laboratory</title>
  <meta name="description" content="An interactive, browser-based visualizer for a 64->32->10 Neural Network learning handwritten digits with pure JavaScript and backpropagation.">
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=JetBrains+Mono:wght@400;500;700&family=Space+Grotesk:wght@400;500;600;700;800&display=swap" rel="stylesheet">

  <style>
    :root {{
      --bg-dark: #08090f;
      --bg-card: rgba(15, 20, 32, 0.72);
      --bg-card-hover: rgba(22, 29, 46, 0.85);
      --border-subtle: rgba(255, 255, 255, 0.09);
      --border-glow: rgba(0, 242, 254, 0.35);
      
      --cyan: #00f2fe;
      --cyan-glow: rgba(0, 242, 254, 0.35);
      --magenta: #ff007f;
      --magenta-glow: rgba(255, 0, 127, 0.35);
      --purple: #8b5cf6;
      --purple-glow: rgba(139, 92, 246, 0.35);
      --emerald: #10b981;
      --emerald-glow: rgba(16, 185, 129, 0.35);
      --amber: #f59e0b;
      --amber-glow: rgba(245, 158, 11, 0.35);
      
      --text-main: #f8fafc;
      --text-muted: #94a3b8;
      --text-dim: #64748b;
      
      --font-main: 'Space Grotesk', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
      --font-mono: 'JetBrains Mono', monospace;
    }}

    * {{
      box-sizing: border-box;
      margin: 0;
      padding: 0;
    }}

    html {{
      scroll-behavior: smooth;
    }}

    body {{
      background-color: var(--bg-dark);
      color: var(--text-main);
      font-family: var(--font-main);
      line-height: 1.6;
      overflow-x: hidden;
      position: relative;
      background-image: 
        radial-gradient(circle at 20% 15%, rgba(0, 242, 254, 0.07) 0%, transparent 40%),
        radial-gradient(circle at 80% 30%, rgba(139, 92, 246, 0.07) 0%, transparent 45%),
        radial-gradient(circle at 50% 80%, rgba(255, 0, 127, 0.05) 0%, transparent 50%);
    }}

    /* Custom Scrollbar */
    ::-webkit-scrollbar {{
      width: 8px;
      height: 8px;
    }}
    ::-webkit-scrollbar-track {{
      background: rgba(8, 9, 15, 0.8);
    }}
    ::-webkit-scrollbar-thumb {{
      background: rgba(255, 255, 255, 0.15);
      border-radius: 4px;
    }}
    ::-webkit-scrollbar-thumb:hover {{
      background: var(--cyan);
    }}

    /* Hero Background Canvas */
    #hero-canvas {{
      position: absolute;
      top: 0;
      left: 0;
      width: 100%;
      height: 520px;
      pointer-events: none;
      z-index: 0;
      opacity: 0.65;
    }}

    /* Container */
    .container {{
      max-width: 1440px;
      margin: 0 auto;
      padding: 0 24px;
      position: relative;
      z-index: 1;
    }}

    /* Header Nav */
    header {{
      padding: 24px 0;
      border-bottom: 1px solid var(--border-subtle);
      backdrop-filter: blur(12px);
      position: sticky;
      top: 0;
      z-index: 100;
      background: rgba(8, 9, 15, 0.8);
    }}

    .nav-inner {{
      display: flex;
      justify-content: space-between;
      align-items: center;
    }}

    .brand {{
      display: flex;
      align-items: center;
      gap: 12px;
      font-size: 1.25rem;
      font-weight: 700;
      letter-spacing: -0.02em;
      text-decoration: none;
      color: var(--text-main);
    }}

    .brand-icon {{
      width: 32px;
      height: 32px;
      border-radius: 8px;
      background: linear-gradient(135deg, var(--cyan), var(--purple));
      display: flex;
      align-items: center;
      justify-content: center;
      box-shadow: 0 0 15px var(--cyan-glow);
    }}

    .nav-links {{
      display: flex;
      align-items: center;
      gap: 20px;
      list-style: none;
    }}

    .nav-link {{
      color: var(--text-muted);
      text-decoration: none;
      font-size: 0.9rem;
      font-weight: 500;
      transition: color 0.2s ease;
    }}
    .nav-link:hover {{
      color: var(--cyan);
    }}

    .badge-pill {{
      display: inline-flex;
      align-items: center;
      gap: 6px;
      padding: 5px 12px;
      border-radius: 9999px;
      background: rgba(0, 242, 254, 0.08);
      border: 1px solid rgba(0, 242, 254, 0.3);
      color: var(--cyan);
      font-size: 0.75rem;
      font-family: var(--font-mono);
      font-weight: 600;
      letter-spacing: 0.04em;
      text-transform: uppercase;
    }}

    .pulse-dot {{
      width: 6px;
      height: 6px;
      border-radius: 50%;
      background: var(--cyan);
      box-shadow: 0 0 8px var(--cyan);
      animation: pulseDot 1.8s infinite ease-in-out;
    }}

    @keyframes pulseDot {{
      0%, 100% {{ opacity: 0.4; transform: scale(0.85); }}
      50% {{ opacity: 1; transform: scale(1.25); }}
    }}

    /* Hero Section */
    .hero {{
      padding: 60px 0 40px;
      text-align: center;
      position: relative;
    }}

    .hero-title {{
      font-size: clamp(2.4rem, 5.5vw, 4.2rem);
      font-weight: 800;
      letter-spacing: -0.04em;
      line-height: 1.1;
      margin-bottom: 16px;
      background: linear-gradient(135deg, #ffffff 10%, var(--cyan) 50%, var(--magenta) 90%);
      -webkit-background-clip: text;
      -webkit-text-fill-color: transparent;
      text-shadow: 0 0 40px rgba(0, 242, 254, 0.25);
    }}

    .hero-subtitle {{
      font-size: clamp(1.1rem, 2vw, 1.45rem);
      color: var(--text-muted);
      font-weight: 500;
      max-width: 700px;
      margin: 0 auto 28px;
    }}

    .hero-tags {{
      display: flex;
      flex-wrap: wrap;
      justify-content: center;
      gap: 12px;
      margin-bottom: 36px;
    }}

    .hero-tag {{
      display: flex;
      align-items: center;
      gap: 8px;
      padding: 8px 16px;
      border-radius: 8px;
      background: rgba(255, 255, 255, 0.03);
      border: 1px solid var(--border-subtle);
      font-family: var(--font-mono);
      font-size: 0.85rem;
      color: var(--text-muted);
    }}
    .hero-tag strong {{
      color: var(--text-main);
    }}

    /* Main Dashboard Grid */
    .dashboard-grid {{
      display: grid;
      grid-template-columns: 340px 1fr 340px;
      gap: 20px;
      margin-bottom: 40px;
    }}

    @media (max-width: 1280px) {{
      .dashboard-grid {{
        grid-template-columns: 320px 1fr;
      }}
      .dashboard-grid > .col-right {{
        grid-column: span 2;
      }}
    }}

    @media (max-width: 960px) {{
      .dashboard-grid {{
        grid-template-columns: 1fr;
      }}
      .dashboard-grid > .col-right {{
        grid-column: span 1;
      }}
    }}

    /* Card Base */
    .card {{
      background: var(--bg-card);
      border: 1px solid var(--border-subtle);
      border-radius: 16px;
      padding: 20px;
      backdrop-filter: blur(16px);
      box-shadow: 0 8px 32px rgba(0, 0, 0, 0.4);
      transition: border-color 0.25s ease, box-shadow 0.25s ease;
      position: relative;
      overflow: hidden;
    }}

    .card:hover {{
      border-color: rgba(255, 255, 255, 0.16);
    }}

    .card-header {{
      display: flex;
      justify-content: space-between;
      align-items: center;
      margin-bottom: 16px;
      padding-bottom: 12px;
      border-bottom: 1px solid var(--border-subtle);
    }}

    .card-title {{
      font-size: 1rem;
      font-weight: 700;
      letter-spacing: -0.01em;
      display: flex;
      align-items: center;
      gap: 8px;
    }}

    .card-title-icon {{
      color: var(--cyan);
    }}

    /* 8x8 Pixel Grid */
    .grid-8x8-wrapper {{
      display: flex;
      flex-direction: column;
      align-items: center;
      gap: 16px;
    }}

    .grid-8x8 {{
      display: grid;
      grid-template-columns: repeat(8, 1fr);
      gap: 3px;
      width: 220px;
      height: 220px;
      background: rgba(0, 0, 0, 0.6);
      padding: 6px;
      border-radius: 10px;
      border: 1px solid var(--border-subtle);
      box-shadow: inset 0 2px 8px rgba(0, 0, 0, 0.8);
    }}

    .pixel-cell {{
      width: 100%;
      height: 100%;
      border-radius: 2px;
      background: #000;
      transition: background-color 0.15s ease, transform 0.15s ease, box-shadow 0.15s ease;
      cursor: pointer;
      position: relative;
    }}

    .pixel-cell:hover {{
      transform: scale(1.2);
      z-index: 10;
      outline: 2px solid var(--cyan);
      box-shadow: 0 0 10px var(--cyan);
    }}

    /* Sample Selector Controls */
    .sample-controls {{
      display: flex;
      align-items: center;
      justify-content: space-between;
      width: 100%;
      gap: 8px;
    }}

    .btn {{
      display: inline-flex;
      align-items: center;
      justify-content: center;
      gap: 8px;
      padding: 8px 14px;
      border-radius: 8px;
      font-size: 0.85rem;
      font-weight: 600;
      font-family: var(--font-main);
      cursor: pointer;
      transition: all 0.2s ease;
      border: 1px solid var(--border-subtle);
      background: rgba(255, 255, 255, 0.05);
      color: var(--text-main);
      text-decoration: none;
    }}

    .btn:hover {{
      background: rgba(255, 255, 255, 0.12);
      border-color: rgba(255, 255, 255, 0.2);
      transform: translateY(-1px);
    }}

    .btn:active {{
      transform: translateY(0);
    }}

    .btn-primary {{
      background: linear-gradient(135deg, #00f2fe, #4facfe);
      color: #050b14;
      border: none;
      font-weight: 700;
      box-shadow: 0 4px 15px rgba(0, 242, 254, 0.35);
    }}

    .btn-primary:hover {{
      background: linear-gradient(135deg, #38f9d7, #4facfe);
      box-shadow: 0 6px 20px rgba(0, 242, 254, 0.5);
    }}

    .btn-accent {{
      background: linear-gradient(135deg, #ff007f, #7928ca);
      color: #fff;
      border: none;
      box-shadow: 0 4px 15px rgba(255, 0, 127, 0.35);
    }}

    .btn-accent:hover {{
      background: linear-gradient(135deg, #ff3399, #9333ea);
      box-shadow: 0 6px 20px rgba(255, 0, 127, 0.5);
    }}

    .btn-sm {{
      padding: 5px 10px;
      font-size: 0.78rem;
    }}

    .digit-filter-bar {{
      display: flex;
      flex-wrap: wrap;
      gap: 4px;
      justify-content: center;
      width: 100%;
      margin-top: 6px;
    }}

    .digit-pill-btn {{
      width: 26px;
      height: 26px;
      border-radius: 6px;
      background: rgba(255, 255, 255, 0.04);
      border: 1px solid var(--border-subtle);
      color: var(--text-muted);
      font-size: 0.75rem;
      font-family: var(--font-mono);
      font-weight: 600;
      cursor: pointer;
      display: flex;
      align-items: center;
      justify-content: center;
      transition: all 0.15s ease;
    }}

    .digit-pill-btn:hover, .digit-pill-btn.active {{
      background: var(--cyan);
      color: #040810;
      border-color: var(--cyan);
      font-weight: 700;
      box-shadow: 0 0 10px var(--cyan-glow);
    }}

    /* Sample Info Pill */
    .sample-info-hud {{
      display: flex;
      justify-content: space-between;
      width: 100%;
      padding: 8px 12px;
      border-radius: 8px;
      background: rgba(0, 0, 0, 0.4);
      border: 1px solid var(--border-subtle);
      font-family: var(--font-mono);
      font-size: 0.78rem;
    }}

    /* Central Neural Network Visualizer Canvas */
    .network-canvas-container {{
      width: 100%;
      height: 480px;
      position: relative;
      border-radius: 12px;
      background: rgba(4, 6, 12, 0.85);
      border: 1px solid var(--border-subtle);
      overflow: hidden;
    }}

    #network-canvas {{
      width: 100%;
      height: 100%;
      display: block;
      cursor: crosshair;
    }}

    .canvas-legend {{
      display: flex;
      gap: 12px;
      font-size: 0.72rem;
      font-family: var(--font-mono);
      background: rgba(8, 12, 20, 0.75);
      padding: 4px 10px;
      border-radius: 6px;
      border: 1px solid var(--border-subtle);
      backdrop-filter: blur(8px);
    }}

    .legend-item {{
      display: flex;
      align-items: center;
      gap: 5px;
    }}

    .legend-dot {{
      width: 8px;
      height: 8px;
      border-radius: 50%;
    }}

    .hud-tooltip {{
      position: absolute;
      bottom: 12px;
      left: 14px;
      background: rgba(10, 15, 26, 0.9);
      border: 1px solid var(--cyan);
      border-radius: 8px;
      padding: 8px 12px;
      font-family: var(--font-mono);
      font-size: 0.75rem;
      color: var(--text-main);
      box-shadow: 0 4px 20px rgba(0, 242, 254, 0.25);
      pointer-events: none;
      display: none;
      z-index: 50;
      backdrop-filter: blur(8px);
    }}

    /* Network Visualizer Action Bar */
    .network-action-bar {{
      display: flex;
      justify-content: space-between;
      align-items: center;
      margin-top: 14px;
      flex-wrap: wrap;
      gap: 10px;
    }}

    .anim-mode-toggles {{
      display: flex;
      gap: 6px;
    }}

    .mode-btn {{
      padding: 6px 12px;
      border-radius: 6px;
      font-size: 0.78rem;
      font-family: var(--font-main);
      font-weight: 600;
      background: rgba(255, 255, 255, 0.04);
      border: 1px solid var(--border-subtle);
      color: var(--text-muted);
      cursor: pointer;
      transition: all 0.2s ease;
    }}

    .mode-btn.active {{
      background: rgba(0, 242, 254, 0.12);
      border-color: var(--cyan);
      color: var(--cyan);
    }}

    /* Right Column: Training Dashboard */
    .metric-row {{
      display: grid;
      grid-template-columns: 1fr 1fr;
      gap: 10px;
      margin-bottom: 14px;
    }}

    .metric-box {{
      background: rgba(0, 0, 0, 0.4);
      border: 1px solid var(--border-subtle);
      border-radius: 10px;
      padding: 12px;
      text-align: center;
    }}

    .metric-box-label {{
      font-size: 0.72rem;
      font-family: var(--font-mono);
      color: var(--text-muted);
      text-transform: uppercase;
      letter-spacing: 0.04em;
      margin-bottom: 4px;
    }}

    .metric-box-val {{
      font-size: 1.55rem;
      font-weight: 800;
      font-family: var(--font-mono);
      color: var(--cyan);
      text-shadow: 0 0 15px var(--cyan-glow);
    }}

    .metric-box-val.loss {{
      color: var(--magenta);
      text-shadow: 0 0 15px var(--magenta-glow);
    }}

    /* Progress bar */
    .progress-bar-wrapper {{
      width: 100%;
      height: 6px;
      background: rgba(255, 255, 255, 0.06);
      border-radius: 3px;
      overflow: hidden;
      margin: 8px 0 14px;
    }}

    .progress-bar-fill {{
      height: 100%;
      width: 0%;
      background: linear-gradient(90deg, var(--cyan), var(--purple), var(--magenta));
      transition: width 0.15s ease;
      box-shadow: 0 0 8px var(--cyan);
    }}

    /* Controls Panel */
    .controls-panel {{
      display: flex;
      flex-direction: column;
      gap: 12px;
      margin-bottom: 16px;
    }}

    .control-slider-group {{
      display: flex;
      flex-direction: column;
      gap: 6px;
    }}

    .slider-header {{
      display: flex;
      justify-content: space-between;
      font-size: 0.75rem;
      font-family: var(--font-mono);
      color: var(--text-muted);
    }}

    .slider-header strong {{
      color: var(--text-main);
    }}

    input[type="range"] {{
      -webkit-appearance: none;
      width: 100%;
      height: 5px;
      border-radius: 5px;
      background: rgba(255, 255, 255, 0.1);
      outline: none;
      transition: background 0.2s;
    }}

    input[type="range"]::-webkit-slider-thumb {{
      -webkit-appearance: none;
      appearance: none;
      width: 15px;
      height: 15px;
      border-radius: 50%;
      background: var(--cyan);
      cursor: pointer;
      box-shadow: 0 0 10px var(--cyan);
      transition: transform 0.1s;
    }}

    input[type="range"]::-webkit-slider-thumb:hover {{
      transform: scale(1.25);
    }}

    /* Action Buttons Row */
    .action-btn-grid {{
      display: grid;
      grid-template-columns: 1fr 1fr;
      gap: 8px;
    }}

    /* Live Loss & Accuracy Chart Canvas */
    .chart-container {{
      width: 100%;
      height: 160px;
      background: rgba(4, 6, 12, 0.7);
      border: 1px solid var(--border-subtle);
      border-radius: 10px;
      position: relative;
      overflow: hidden;
      margin-top: 10px;
    }}

    #chart-canvas {{
      width: 100%;
      height: 100%;
      display: block;
    }}

    /* Softmax Probability Bars */
    .prob-bars-list {{
      display: flex;
      flex-direction: column;
      gap: 5px;
      width: 100%;
    }}

    .prob-row {{
      display: flex;
      align-items: center;
      gap: 8px;
      font-family: var(--font-mono);
      font-size: 0.78rem;
    }}

    .prob-digit {{
      width: 18px;
      font-weight: 700;
      color: var(--text-muted);
    }}

    .prob-digit.is-winner {{
      color: var(--cyan);
      text-shadow: 0 0 8px var(--cyan);
    }}

    .prob-track {{
      flex: 1;
      height: 12px;
      background: rgba(255, 255, 255, 0.05);
      border-radius: 3px;
      overflow: hidden;
      position: relative;
    }}

    .prob-fill {{
      height: 100%;
      width: 0%;
      background: linear-gradient(90deg, rgba(0, 242, 254, 0.6), var(--cyan));
      border-radius: 3px;
      transition: width 0.15s ease, background 0.15s ease;
    }}

    .prob-fill.winner-fill {{
      background: linear-gradient(90deg, #10b981, #00f2fe);
      box-shadow: 0 0 8px var(--cyan);
    }}

    .prob-percent {{
      width: 44px;
      text-align: right;
      color: var(--text-dim);
      font-size: 0.72rem;
    }}

    .prob-percent.is-winner {{
      color: var(--text-main);
      font-weight: 700;
    }}

    /* Test It Yourself: Interactive Drawing Canvas */
    .draw-canvas-wrapper {{
      display: flex;
      gap: 16px;
      align-items: center;
      justify-content: center;
      margin-bottom: 16px;
      flex-wrap: wrap;
    }}

    .draw-box-area {{
      display: flex;
      flex-direction: column;
      align-items: center;
      gap: 8px;
    }}

    .draw-canvas {{
      width: 200px;
      height: 200px;
      background: #000;
      border: 2px solid var(--border-subtle);
      border-radius: 12px;
      cursor: crosshair;
      box-shadow: 0 4px 20px rgba(0, 0, 0, 0.6);
      touch-action: none;
    }}

    .draw-canvas:hover {{
      border-color: var(--cyan);
    }}

    .draw-arrow-icon {{
      font-size: 1.5rem;
      color: var(--text-dim);
    }}

    .downscaled-preview {{
      display: flex;
      flex-direction: column;
      align-items: center;
      gap: 8px;
    }}

    .downscaled-grid {{
      width: 100px;
      height: 100px;
      display: grid;
      grid-template-columns: repeat(8, 1fr);
      gap: 1px;
      background: #000;
      padding: 3px;
      border: 1px solid var(--border-subtle);
      border-radius: 6px;
    }}

    .downscaled-cell {{
      background: #000;
      border-radius: 1px;
    }}

    .prediction-badge-display {{
      display: flex;
      align-items: center;
      gap: 14px;
      background: rgba(0, 0, 0, 0.4);
      padding: 12px 18px;
      border-radius: 12px;
      border: 1px solid var(--border-subtle);
      width: 100%;
      margin-top: 10px;
    }}

    .big-digit-badge {{
      width: 54px;
      height: 54px;
      border-radius: 12px;
      background: linear-gradient(135deg, rgba(0, 242, 254, 0.15), rgba(139, 92, 246, 0.15));
      border: 1px solid var(--cyan);
      display: flex;
      align-items: center;
      justify-content: center;
      font-size: 2.2rem;
      font-weight: 800;
      font-family: var(--font-mono);
      color: var(--cyan);
      box-shadow: 0 0 20px var(--cyan-glow);
    }}

    .prediction-details {{
      flex: 1;
    }}

    .prediction-title {{
      font-size: 0.75rem;
      font-family: var(--font-mono);
      color: var(--text-muted);
      text-transform: uppercase;
    }}

    .prediction-confidence {{
      font-size: 1.2rem;
      font-weight: 700;
      color: var(--text-main);
    }}

    /* Explanatory Math Section */
    .math-section {{
      padding: 60px 0 80px;
      position: relative;
    }}

    .section-header {{
      text-align: center;
      margin-bottom: 40px;
    }}

    .section-title {{
      font-size: clamp(1.8rem, 3.5vw, 2.6rem);
      font-weight: 800;
      letter-spacing: -0.03em;
      margin-bottom: 12px;
    }}

    .section-desc {{
      color: var(--text-muted);
      max-width: 650px;
      margin: 0 auto;
      font-size: 1rem;
    }}

    .math-cards-grid {{
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
      gap: 24px;
    }}

    .math-card {{
      background: var(--bg-card);
      border: 1px solid var(--border-subtle);
      border-radius: 16px;
      padding: 26px;
      backdrop-filter: blur(16px);
      transition: all 0.3s cubic-bezier(0.16, 1, 0.3, 1);
      position: relative;
      overflow: hidden;
      opacity: 0;
      transform: translateY(25px);
    }}

    .math-card.visible {{
      opacity: 1;
      transform: translateY(0);
    }}

    .math-card::before {{
      content: '';
      position: absolute;
      top: 0;
      left: 0;
      width: 100%;
      height: 3px;
      background: linear-gradient(90deg, var(--cyan), var(--purple));
      opacity: 0;
      transition: opacity 0.3s ease;
    }}

    .math-card:hover {{
      border-color: rgba(0, 242, 254, 0.4);
      transform: translateY(-4px);
      box-shadow: 0 12px 35px rgba(0, 242, 254, 0.15);
    }}

    .math-card:hover::before {{
      opacity: 1;
    }}

    .card-step-badge {{
      display: inline-flex;
      align-items: center;
      justify-content: center;
      width: 32px;
      height: 32px;
      border-radius: 8px;
      background: rgba(0, 242, 254, 0.1);
      border: 1px solid rgba(0, 242, 254, 0.3);
      color: var(--cyan);
      font-weight: 800;
      font-family: var(--font-mono);
      font-size: 0.9rem;
      margin-bottom: 16px;
    }}

    .math-formula-box {{
      background: rgba(0, 0, 0, 0.5);
      border: 1px solid var(--border-subtle);
      border-radius: 8px;
      padding: 12px 14px;
      font-family: var(--font-mono);
      font-size: 0.85rem;
      color: var(--cyan);
      margin: 14px 0;
      overflow-x: auto;
      text-shadow: 0 0 10px rgba(0, 242, 254, 0.2);
    }}

    .math-card h3 {{
      font-size: 1.2rem;
      font-weight: 700;
      margin-bottom: 8px;
      color: var(--text-main);
    }}

    .math-card p {{
      font-size: 0.9rem;
      color: var(--text-muted);
      line-height: 1.6;
    }}

    /* Footer */
    footer {{
      border-top: 1px solid var(--border-subtle);
      padding: 40px 0;
      text-align: center;
      font-size: 0.85rem;
      color: var(--text-dim);
      backdrop-filter: blur(8px);
      background: rgba(8, 9, 15, 0.9);
    }}

    .footer-links {{
      display: flex;
      justify-content: center;
      gap: 20px;
      margin-bottom: 12px;
    }}

    .footer-links a {{
      color: var(--text-muted);
      text-decoration: none;
      transition: color 0.2s;
    }}
    .footer-links a:hover {{
      color: var(--cyan);
    }}

    /* Responsive adjustments */
    @media (max-width: 640px) {{
      .hero-title {{
        font-size: 2.2rem;
      }}
      .sample-controls {{
        flex-direction: column;
      }}
      .nav-links {{
        display: none;
      }}
    }}
  </style>
</head>
<body>

  <!-- Background Particle Canvas for Hero -->
  <canvas id="hero-canvas"></canvas>

  <!-- Sticky Navigation Header -->
  <header>
    <div class="container nav-inner">
      <a href="#" class="brand">
        <div class="brand-icon">
          <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="#050b14" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round">
            <circle cx="12" cy="12" r="3"></circle>
            <path d="M19.4 15a1.65 1.65 0 0 0 .33 1.82l.06.06a2 2 0 0 1 0 2.83 2 2 0 0 1-2.83 0l-.06-.06a1.65 1.65 0 0 0-1.82-.33 1.65 1.65 0 0 0-1 1.51V21a2 2 0 0 1-2 2 2 2 0 0 1-2-2v-.09A1.65 1.65 0 0 0 9 19.4a1.65 1.65 0 0 0-1.82.33l-.06.06a2 2 0 0 1-2.83 0 2 2 0 0 1 0-2.83l.06-.06a1.65 1.65 0 0 0 .33-1.82 1.65 1.65 0 0 0-1.51-1H3a2 2 0 0 1-2-2 2 2 0 0 1 2-2h.09A1.65 1.65 0 0 0 4.6 9a1.65 1.65 0 0 0-.33-1.82l-.06-.06a2 2 0 0 1 0-2.83 2 2 0 0 1 2.83 0l.06.06a1.65 1.65 0 0 0 1.82.33H9a1.65 1.65 0 0 0 1-1.51V3a2 2 0 0 1 2-2 2 2 0 0 1 2 2v.09a1.65 1.65 0 0 0 1 1.51 1.65 1.65 0 0 0 1.82-.33l.06-.06a2 2 0 0 1 2.83 0 2 2 0 0 1 0 2.83l-.06.06a1.65 1.65 0 0 0-.33 1.82V9a1.65 1.65 0 0 0 1.51 1H21a2 2 0 0 1 2 2 2 2 0 0 1-2 2h-.09a1.65 1.65 0 0 0-1.51 1z"></path>
          </svg>
        </div>
        <span>NeuroGraph<span style="color:var(--cyan)">.js</span></span>
      </a>

      <div class="badge-pill">
        <span class="pulse-dot"></span>
        <span>100% Pure JS • No Frameworks</span>
      </div>

      <ul class="nav-links">
        <li><a href="#studio" class="nav-link">Interactive Studio</a></li>
        <li><a href="#test-digit" class="nav-link">Draw & Test</a></li>
        <li><a href="#math-explanation" class="nav-link">How It Works</a></li>
      </ul>
    </div>
  </header>

  <!-- Hero Section -->
  <section class="hero">
    <div class="container">
      <h1 class="hero-title">Neural Network from Scratch</h1>
      <p class="hero-subtitle">No PyTorch. No TensorFlow. Just math.</p>

      <div class="hero-tags">
        <div class="hero-tag"><span>Architecture:</span> <strong>64 → 32 → 10</strong></div>
        <div class="hero-tag"><span>Activation:</span> <strong>ReLU + Softmax</strong></div>
        <div class="hero-tag"><span>Optimization:</span> <strong>Backprop (LR 0.65)</strong></div>
        <div class="hero-tag"><span>Goal:</span> <strong>~9.8% → ~99% Acc</strong></div>
      </div>
    </div>
  </section>

  <!-- Main Interactive Studio Grid -->
  <main class="container" id="studio">
    <div class="dashboard-grid">
      
      <!-- Left Column: Input Visualizer & Dataset Browser -->
      <div class="col-left" style="display: flex; flex-direction: column; gap: 20px;">
        <div class="card">
          <div class="card-header">
            <h2 class="card-title">
              <svg class="card-title-icon" width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="3" y="3" width="18" height="18" rx="2"/><path d="M3 9h18M9 21V9"/></svg>
              8x8 Input Visualizer
            </h2>
            <span class="badge-pill" id="current-label-badge">Label: 0</span>
          </div>

          <div class="grid-8x8-wrapper">
            <!-- 8x8 Grid Canvas/DOM -->
            <div class="grid-8x8" id="pixel-grid-container"></div>

            <div class="sample-info-hud">
              <span>Sample: <strong id="sample-index-text" style="color:var(--cyan)">#1 / 350</strong></span>
              <span>Target: <strong id="sample-target-text" style="color:var(--emerald)">Digit 0</strong></span>
            </div>

            <div class="sample-controls">
              <button class="btn btn-sm" id="btn-prev-sample">◀ Prev</button>
              <button class="btn btn-sm" id="btn-random-sample">🎲 Random</button>
              <button class="btn btn-sm" id="btn-next-sample">Next ▶</button>
            </div>

            <!-- Quick Filter By Digit -->
            <div style="width: 100%;">
              <div style="font-size: 0.72rem; font-family: var(--font-mono); color: var(--text-dim); margin-bottom: 4px; text-align: center;">Filter by Digit Class:</div>
              <div class="digit-filter-bar" id="digit-filter-container"></div>
            </div>

            <button class="btn btn-primary" id="btn-send-to-network" style="width: 100%; margin-top: 4px;">
              ⚡ Fire Forward Pass Pulse
            </button>
          </div>
        </div>

        <!-- Softmax Probabilities Card for Current Sample -->
        <div class="card">
          <div class="card-header">
            <h2 class="card-title">
              <svg class="card-title-icon" width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M18 20V10M12 20V4M6 20v-6"/></svg>
              Softmax Probabilities
            </h2>
            <span id="current-prediction-tag" style="font-family: var(--font-mono); font-size: 0.8rem; font-weight: 700; color: var(--cyan);">Pred: ?</span>
          </div>

          <div class="prob-bars-list" id="softmax-bars-container"></div>
        </div>
      </div>

      <!-- Center Column: Network Diagram & Signal Animation -->
      <div class="col-center">
        <div class="card" style="height: 100%; display: flex; flex-direction: column;">
          <div class="card-header">
            <h2 class="card-title">
              <svg class="card-title-icon" width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="6" cy="6" r="3"/><circle cx="6" cy="18" r="3"/><circle cx="18" cy="12" r="3"/><path d="m8.5 7.5 7 3.5M8.5 16.5l7-3.5"/></svg>
              Live Network Architecture (64 → 32 → 10)
            </h2>
            <div class="canvas-legend">
              <div class="legend-item"><span class="legend-dot" style="background:var(--cyan)"></span><span>+ Weight</span></div>
              <div class="legend-item"><span class="legend-dot" style="background:var(--magenta)"></span><span>- Weight</span></div>
              <div class="legend-item"><span class="legend-dot" style="background:#10b981"></span><span>Signal</span></div>
            </div>
          </div>

          <!-- Canvas Container -->
          <div class="network-canvas-container" style="flex: 1; min-height: 480px;">
            <canvas id="network-canvas"></canvas>

            <!-- Floating HUD Tooltip for Hovered Node -->
            <div id="node-hud-tooltip" class="hud-tooltip"></div>
          </div>

          <!-- Bottom Action Bar -->
          <div class="network-action-bar">
            <div class="anim-mode-toggles">
              <button class="mode-btn active" id="btn-mode-forward">✨ Forward Pass (Photons)</button>
              <button class="mode-btn" id="btn-mode-backprop">🔥 Backprop Wave (Error)</button>
            </div>

            <div style="display: flex; gap: 8px;">
              <button class="btn btn-sm" id="btn-pulse-wave">🌊 Send Pulse Wave</button>
            </div>
          </div>
        </div>
      </div>

      <!-- Right Column: Training Dashboard & Live Charts -->
      <div class="col-right" style="display: flex; flex-direction: column; gap: 20px;">
        <div class="card">
          <div class="card-header">
            <h2 class="card-title">
              <svg class="card-title-icon" width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M12 2v4M12 18v4M4.93 4.93l2.83 2.83M16.24 16.24l2.83 2.83M2 12h4M18 12h4M4.93 19.07l2.83-2.83M16.24 7.76l2.83-2.83"/></svg>
              Training Dashboard
            </h2>
            <span class="badge-pill" id="training-status-pill">Ready</span>
          </div>

          <!-- Metrics Row -->
          <div class="metric-row">
            <div class="metric-box">
              <div class="metric-box-label">Accuracy</div>
              <div class="metric-box-val" id="metric-accuracy-val">9.8%</div>
            </div>
            <div class="metric-box">
              <div class="metric-box-label">Loss (Cross-Entropy)</div>
              <div class="metric-box-val loss" id="metric-loss-val">2.39</div>
            </div>
          </div>

          <!-- Progress -->
          <div style="display: flex; justify-content: space-between; font-size: 0.75rem; font-family: var(--font-mono); color: var(--text-muted);">
            <span>Epoch / Step: <strong id="metric-step-text" style="color:var(--text-main)">0 / 300</strong></span>
            <span>Target: <strong>300 Steps</strong></span>
          </div>
          <div class="progress-bar-wrapper">
            <div class="progress-bar-fill" id="training-progress-fill"></div>
          </div>

          <!-- Controls Panel -->
          <div class="controls-panel">
            <div class="action-btn-grid">
              <button class="btn btn-primary" id="btn-toggle-train">
                <span id="train-btn-icon">▶</span>
                <span id="train-btn-label">Start Training</span>
              </button>
              <button class="btn" id="btn-step-train">⏭ Step 1x</button>
            </div>

            <div class="action-btn-grid">
              <button class="btn btn-accent" id="btn-instant-train">⚡ Train to 300</button>
              <button class="btn" id="btn-reset-train">↺ Reset Weights</button>
            </div>

            <!-- Sliders -->
            <div class="control-slider-group" style="margin-top: 6px;">
              <div class="slider-header">
                <span>Training Speed:</span>
                <strong id="speed-label">20 steps/sec</strong>
              </div>
              <input type="range" id="slider-speed" min="1" max="60" value="20">
            </div>

            <div class="control-slider-group">
              <div class="slider-header">
                <span>Learning Rate (&eta;):</span>
                <strong id="lr-label">0.65</strong>
              </div>
              <input type="range" id="slider-lr" min="0.05" max="1.5" step="0.05" value="0.65">
            </div>
          </div>

          <!-- Loss / Accuracy Canvas Chart -->
          <div style="display: flex; justify-content: space-between; align-items: center; margin-top: 4px;">
            <div style="font-size: 0.75rem; font-family: var(--font-mono); color: var(--text-muted);">Live Learning Curve:</div>
            <div style="display: flex; gap: 8px; font-size: 0.7rem; font-family: var(--font-mono);">
              <span style="color:var(--cyan)">— Acc</span>
              <span style="color:var(--magenta)">— Loss</span>
            </div>
          </div>
          <div class="chart-container">
            <canvas id="chart-canvas"></canvas>
          </div>
        </div>
      </div>

    </div>

    <!-- Test It Yourself: Interactive Drawing Canvas Section -->
    <section class="card" id="test-digit" style="margin-bottom: 40px;">
      <div class="card-header">
        <h2 class="card-title">
          <svg class="card-title-icon" width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M12 19l7-7 3 3-7 7-3-3z"/><path d="M18 13l-1.5-7.5L2 2l3.5 14.5L13 18l5-5z"/><path d="M2 2l7.586 7.586"/><circle cx="11" cy="11" r="2"/></svg>
          Test It Yourself — Live Interactive Drawing Pad
        </h2>
        <span class="badge-pill">Real-time Inference</span>
      </div>

      <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 30px; align-items: center;">
        <div>
          <p style="font-size: 0.9rem; color: var(--text-muted); margin-bottom: 16px;">
            Draw any single digit (0-9) inside the pad with your mouse or finger. The preprocessing pipeline automatically detects stroke boundaries, centers the digit, downscales it to the 8x8 matrix format, and feeds it into the live JavaScript neural network!
          </p>

          <div class="draw-canvas-wrapper">
            <div class="draw-box-area">
              <canvas id="user-draw-canvas" class="draw-canvas" width="200" height="200"></canvas>
              <div style="display: flex; gap: 8px;">
                <button class="btn btn-sm" id="btn-clear-draw">🗑 Clear</button>
                <button class="btn btn-sm btn-primary" id="btn-send-draw-to-net">⚡ Feed to Net</button>
              </div>
            </div>

            <div class="draw-arrow-icon">➔</div>

            <div class="downscaled-preview">
              <div class="downscaled-grid" id="downscaled-preview-grid"></div>
              <div style="font-size: 0.72rem; font-family: var(--font-mono); color: var(--text-dim);">8x8 Input Vector</div>
            </div>
          </div>

          <!-- Preset Demo Digits -->
          <div style="display: flex; align-items: center; gap: 8px; justify-content: center; flex-wrap: wrap;">
            <span style="font-size: 0.75rem; font-family: var(--font-mono); color: var(--text-muted);">Quick Presets:</span>
            <div style="display: flex; gap: 4px;">
              <button class="btn btn-sm preset-draw-btn" data-digit="0">0</button>
              <button class="btn btn-sm preset-draw-btn" data-digit="1">1</button>
              <button class="btn btn-sm preset-draw-btn" data-digit="3">3</button>
              <button class="btn btn-sm preset-draw-btn" data-digit="4">4</button>
              <button class="btn btn-sm preset-draw-btn" data-digit="7">7</button>
              <button class="btn btn-sm preset-draw-btn" data-digit="8">8</button>
            </div>
          </div>
        </div>

        <!-- Live Prediction Output Panel -->
        <div style="display: flex; flex-direction: column; gap: 14px;">
          <div class="prediction-badge-display">
            <div class="big-digit-badge" id="draw-predicted-badge">?</div>
            <div class="prediction-details">
              <div class="prediction-title">Network Prediction</div>
              <div class="prediction-confidence" id="draw-confidence-text">Confidence: 0.0%</div>
            </div>
          </div>

          <div class="prob-bars-list" id="draw-softmax-bars-container"></div>
        </div>
      </div>
    </section>

    <!-- Explanatory "How It Works" Section -->
    <section class="math-section" id="math-explanation">
      <div class="section-header">
        <div class="badge-pill" style="margin-bottom: 12px;">Under the Hood</div>
        <h2 class="section-title">How the Math Actually Works</h2>
        <p class="section-desc">Every single neuron is pure linear algebra and calculus. Here is the exact mathematical step-by-step pipeline running inside your browser.</p>
      </div>

      <div class="math-cards-grid">
        <!-- Card 1: Forward Pass -->
        <div class="math-card">
          <div class="card-step-badge">1</div>
          <h3>Forward Pass (Linear Matrix Combination)</h3>
          <p>The 64-dimensional grayscale input pixel vector is multiplied by the weight matrix and added to a bias vector to compute the raw hidden logit scores.</p>
          <div class="math-formula-box">
            Z⁽¹⁾ = X · W⁽¹⁾ + b⁽¹⁾<br>
            <span style="color:var(--text-dim)">Dimensions: [1×64] · [64×32] + [1×32] = [1×32]</span>
          </div>
          <p>Each connection W_ij acts as a synapse strength that amplifies or suppresses specific visual pixel patterns.</p>
        </div>

        <!-- Card 2: Non-linear Activation (ReLU) -->
        <div class="math-card">
          <div class="card-step-badge">2</div>
          <h3>Non-Linear Activation (ReLU)</h3>
          <p>Without non-linear activation functions, stacking layers collapses into a single boring linear transformation. ReLU (Rectified Linear Unit) activates only positive signals.</p>
          <div class="math-formula-box">
            A⁽¹⁾ = max(0, Z⁽¹⁾)<br>
            <span style="color:var(--text-dim)">Derivative: dA/dZ = 1 if Z > 0 else 0</span>
          </div>
          <p>ReLU prevents vanishing gradients and allows the network to learn intricate geometric digit contours.</p>
        </div>

        <!-- Card 3: Softmax & Cross-Entropy -->
        <div class="math-card">
          <div class="card-step-badge">3</div>
          <h3>Softmax Probabilities & Loss</h3>
          <p>The output layer computes raw scores Z⁽²⁾, which Softmax converts into a normalized probability distribution summing to 100%.</p>
          <div class="math-formula-box">
            P(y = k) = exp(Z_k⁽²⁾) / ∑ exp(Z_j⁽²⁾)<br>
            L = -∑ Y_k · ln(P_k)
          </div>
          <p>Cross-Entropy exponentially penalizes confident incorrect predictions, pushing probabilities towards the ground truth label.</p>
        </div>

        <!-- Card 4: Backpropagation & Weight Updates -->
        <div class="math-card">
          <div class="card-step-badge">4</div>
          <h3>Backpropagation & Gradient Step</h3>
          <p>By the calculus chain rule, the error gradient flows backward through each weight matrix to calculate the exact direction of steepest descent.</p>
          <div class="math-formula-box">
            δ⁽²⁾ = P - Y<br>
            δ⁽¹⁾ = (δ⁽²⁾ · (W⁽²⁾)ᵀ) ⊙ (Z⁽¹⁾ > 0)<br>
            W ← W - η · (Inputᵀ · δ)
          </div>
          <p>Weights are adjusted by step size η = 0.65. After 300 iterations, the error plummets from 2.40 to 0.01!</p>
        </div>
      </div>
    </section>
  </main>

  <!-- Footer -->
  <footer>
    <div class="container">
      <div class="footer-links">
        <a href="#studio">Interactive Studio</a>
        <a href="#test-digit">Draw Digits</a>
        <a href="#math-explanation">Math Guide</a>
      </div>
      <p>Built with Pure Vanilla HTML5, CSS3, and Modern JavaScript. Zero external frameworks.</p>
    </div>
  </footer>

  <!-- Embedded Dataset & Neural Network Engine Script -->
  <script>
    // --- 1. EMBEDDED DATASET (350 balanced 8x8 digits: 35 per class 0..9) ---
    {dataset_code}

    // Parse raw string dataset into Float32Array pixel matrices
    const DATASET = RAW_DIGITS_DATA.map((str, idx) => {{
      const label = parseInt(str[0], 10);
      const hex = str.slice(2);
      const pixels = new Float32Array(64);
      for (let i = 0; i < 64; i++) {{
        pixels[i] = parseInt(hex[i], 16) / 15.0; // Normalized 0.0 to 1.0
      }}
      return {{ id: idx, label, pixels, hex }};
    }});

    // --- 2. PURE JAVASCRIPT NEURAL NETWORK CLASS ---
    class ScratchNeuralNetwork {{
      constructor(inputSize = 64, hiddenSize = 32, outputSize = 10) {{
        this.inputSize = inputSize;
        this.hiddenSize = hiddenSize;
        this.outputSize = outputSize;
        this.reset();
      }}

      reset() {{
        this.step = 0;
        this.history = []; // Array of {{ step, loss, accuracy }}
        
        // He Normal / Uniform initialization
        const scale1 = Math.sqrt(2.0 / this.inputSize);
        const scale2 = Math.sqrt(2.0 / this.hiddenSize);
        
        this.W1 = new Float32Array(this.inputSize * this.hiddenSize); // 64 x 32 = 2048
        this.b1 = new Float32Array(this.hiddenSize);                 // 32
        this.W2 = new Float32Array(this.hiddenSize * this.outputSize); // 32 x 10 = 320
        this.b2 = new Float32Array(this.outputSize);                 // 10
        
        for (let i = 0; i < this.W1.length; i++) {{
          this.W1[i] = (Math.random() * 2 - 1) * scale1;
        }}
        for (let i = 0; i < this.W2.length; i++) {{
          this.W2[i] = (Math.random() * 2 - 1) * scale2;
        }}
        // Biases start at 0
        this.b1.fill(0);
        this.b2.fill(0);
      }}

      forward(x) {{
        // x: Float32Array(64)
        // Hidden pre-activation: z1 = x @ W1 + b1
        const z1 = new Float32Array(this.hiddenSize);
        const a1 = new Float32Array(this.hiddenSize);
        for (let j = 0; j < this.hiddenSize; j++) {{
          let sum = this.b1[j];
          for (let i = 0; i < this.inputSize; i++) {{
            sum += x[i] * this.W1[i * this.hiddenSize + j];
          }}
          z1[j] = sum;
          a1[j] = sum > 0 ? sum : 0; // ReLU non-linear activation
        }}

        // Output pre-activation: z2 = a1 @ W2 + b2
        const z2 = new Float32Array(this.outputSize);
        let maxZ = -Infinity;
        for (let k = 0; k < this.outputSize; k++) {{
          let sum = this.b2[k];
          for (let j = 0; j < this.hiddenSize; j++) {{
            sum += a1[j] * this.W2[j * this.outputSize + k];
          }}
          z2[k] = sum;
          if (sum > maxZ) maxZ = sum;
        }}

        // Softmax normalization
        const probs = new Float32Array(this.outputSize);
        let sumExp = 0;
        for (let k = 0; k < this.outputSize; k++) {{
          const e = Math.exp(z2[k] - maxZ); // Numerical stability shift
          probs[k] = e;
          sumExp += e;
        }}
        for (let k = 0; k < this.outputSize; k++) {{
          probs[k] /= sumExp;
        }}

        return {{ z1, a1, z2, probs }};
      }}

      evaluate(dataset) {{
        let correct = 0;
        let totalLoss = 0;
        const perClassCorrect = new Array(10).fill(0);
        const perClassTotal = new Array(10).fill(0);

        for (let s of dataset) {{
          const {{ probs }} = this.forward(s.pixels);
          let pred = 0;
          let maxP = -1;
          for (let k = 0; k < 10; k++) {{
            if (probs[k] > maxP) {{
              maxP = probs[k];
              pred = k;
            }}
          }}
          perClassTotal[s.label]++;
          if (pred === s.label) {{
            correct++;
            perClassCorrect[s.label]++;
          }}
          totalLoss += -Math.log(Math.max(probs[s.label], 1e-15));
        }}

        const accuracy = correct / dataset.length;
        const loss = totalLoss / dataset.length;
        return {{ accuracy, loss, correct, total: dataset.length, perClassCorrect, perClassTotal }};
      }}

      trainStep(dataset, lr = 0.65) {{
        const N = dataset.length;
        const dW1 = new Float32Array(this.inputSize * this.hiddenSize);
        const db1 = new Float32Array(this.hiddenSize);
        const dW2 = new Float32Array(this.hiddenSize * this.outputSize);
        const db2 = new Float32Array(this.outputSize);

        let totalLoss = 0;
        let correct = 0;

        for (let s = 0; s < N; s++) {{
          const {{ pixels, label }} = dataset[s];
          const {{ z1, a1, probs }} = this.forward(pixels);

          let pred = 0;
          let maxP = -1;
          for (let k = 0; k < 10; k++) {{
            if (probs[k] > maxP) {{
              maxP = probs[k];
              pred = k;
            }}
          }}
          if (pred === label) correct++;
          totalLoss += -Math.log(Math.max(probs[label], 1e-15));

          // dZ2 = probs - one_hot(label)
          const dz2 = new Float32Array(10);
          for (let k = 0; k < 10; k++) {{
            dz2[k] = probs[k] - (k === label ? 1.0 : 0.0);
          }}

          // dW2 += a1^T @ dz2, db2 += dz2
          for (let j = 0; j < this.hiddenSize; j++) {{
            const aj = a1[j];
            if (aj === 0) continue; // ReLU sparsity optimization
            const rowOffset = j * this.outputSize;
            for (let k = 0; k < 10; k++) {{
              dW2[rowOffset + k] += aj * dz2[k];
            }}
          }}
          for (let k = 0; k < 10; k++) {{
            db2[k] += dz2[k];
          }}

          // da1 = dz2 @ W2^T
          // dz1 = da1 * (z1 > 0)
          const dz1 = new Float32Array(this.hiddenSize);
          for (let j = 0; j < this.hiddenSize; j++) {{
            if (z1[j] <= 0) continue;
            let sum = 0;
            const rowOffset = j * this.outputSize;
            for (let k = 0; k < 10; k++) {{
              sum += dz2[k] * this.W2[rowOffset + k];
            }}
            dz1[j] = sum;
          }}

          // dW1 += x^T @ dz1, db1 += dz1
          for (let i = 0; i < this.inputSize; i++) {{
            const xi = pixels[i];
            if (xi === 0) continue;
            const rowOffset = i * this.hiddenSize;
            for (let j = 0; j < this.hiddenSize; j++) {{
              if (dz1[j] !== 0) {{
                dW1[rowOffset + j] += xi * dz1[j];
              }}
            }}
          }}
          for (let j = 0; j < this.hiddenSize; j++) {{
            db1[j] += dz1[j];
          }}
        }}

        // Update parameters: W = W - (lr / N) * dW
        const factor = lr / N;
        for (let i = 0; i < this.W1.length; i++) this.W1[i] -= factor * dW1[i];
        for (let j = 0; j < this.b1.length; j++) this.b1[j] -= factor * db1[j];
        for (let i = 0; i < this.W2.length; i++) this.W2[i] -= factor * dW2[i];
        for (let k = 0; k < this.b2.length; k++) this.b2[k] -= factor * db2[k];

        this.step++;
        const avgLoss = totalLoss / N;
        const accuracy = correct / N;
        this.history.push({{ step: this.step, loss: avgLoss, accuracy }});

        return {{ step: this.step, loss: avgLoss, accuracy, correct, total: N }};
      }}
    }}

    // --- 3. GLOBAL APP STATE ---
    const nn = new ScratchNeuralNetwork(64, 32, 10);
    let currentSampleIndex = 0;
    let isTraining = false;
    let trainingIntervalId = null;
    let currentAnimationMode = 'forward'; // 'forward' | 'backprop'
    let hoveredNode = null; // {{ layer: 'input'|'hidden'|'output', index: number }}

    // Visual Signal Particles for dynamic Canvas pulses
    const signalParticles = [];

    // --- 4. HERO BACKGROUND PARTICLES CANVAS ---
    function setupHeroCanvas() {{
      const canvas = document.getElementById('hero-canvas');
      const ctx = canvas.getContext('2d');
      let width, height;
      const particles = [];

      function resize() {{
        width = canvas.width = window.innerWidth;
        height = canvas.height = 520;
      }}
      resize();
      window.addEventListener('resize', resize);

      for (let i = 0; i < 45; i++) {{
        particles.push({{
          x: Math.random() * width,
          y: Math.random() * height,
          vx: (Math.random() - 0.5) * 0.6,
          vy: (Math.random() - 0.5) * 0.6,
          radius: Math.random() * 2.5 + 1.2,
          color: Math.random() > 0.5 ? '#00f2fe' : '#ff007f'
        }});
      }}

      function draw() {{
        ctx.clearRect(0, 0, width, height);

        // Draw connections
        for (let i = 0; i < particles.length; i++) {{
          for (let j = i + 1; j < particles.length; j++) {{
            const dx = particles[i].x - particles[j].x;
            const dy = particles[i].y - particles[j].y;
            const dist = Math.sqrt(dx * dx + dy * dy);
            if (dist < 130) {{
              ctx.beginPath();
              ctx.moveTo(particles[i].x, particles[i].y);
              ctx.lineTo(particles[j].x, particles[j].y);
              ctx.strokeStyle = `rgba(0, 242, 254, ${{0.15 * (1 - dist / 130)}})`;
              ctx.lineWidth = 1;
              ctx.stroke();
            }}
          }}
        }}

        // Draw particles
        for (let p of particles) {{
          p.x += p.vx;
          p.y += p.vy;
          if (p.x < 0 || p.x > width) p.vx *= -1;
          if (p.y < 0 || p.y > height) p.vy *= -1;

          ctx.beginPath();
          ctx.arc(p.x, p.y, p.radius, 0, Math.PI * 2);
          ctx.fillStyle = p.color;
          ctx.shadowBlur = 8;
          ctx.shadowColor = p.color;
          ctx.fill();
          ctx.shadowBlur = 0;
        }}

        requestAnimationFrame(draw);
      }}
      draw();
    }}

    // --- 5. 8x8 PIXEL GRID RENDERER ---
    function setupPixelGrid() {{
      const container = document.getElementById('pixel-grid-container');
      container.innerHTML = '';

      for (let i = 0; i < 64; i++) {{
        const cell = document.createElement('div');
        cell.className = 'pixel-cell';
        cell.dataset.index = i;
        cell.title = `Pixel x_${{i}}`;
        cell.addEventListener('mouseenter', () => {{
          hoveredNode = {{ layer: 'input', index: i }};
          updateNodeHudTooltip(i, 'input');
        }});
        cell.addEventListener('mouseleave', () => {{
          hoveredNode = null;
          hideNodeHudTooltip();
        }});
        container.appendChild(cell);
      }}

      // Setup Digit Class Filter Buttons [0..9]
      const filterContainer = document.getElementById('digit-filter-container');
      filterContainer.innerHTML = '';
      for (let d = 0; d < 10; d++) {{
        const btn = document.createElement('button');
        btn.className = 'digit-pill-btn';
        btn.textContent = d;
        btn.addEventListener('click', () => {{
          // Find first sample of this digit
          const idx = DATASET.findIndex(s => s.label === d);
          if (idx !== -1) {{
            currentSampleIndex = idx;
            renderCurrentSample();
            triggerForwardPassAnimation();
          }}
        }});
        filterContainer.appendChild(btn);
      }}
    }}

    function renderCurrentSample() {{
      const sample = DATASET[currentSampleIndex];
      const cells = document.querySelectorAll('.pixel-cell');

      sample.pixels.forEach((val, i) => {{
        const intensity = Math.round(val * 255);
        // Stylized cyan glow heat map
        if (val > 0.05) {{
          cells[i].style.backgroundColor = `rgb(${{Math.round(val * 0)}}, ${{Math.round(val * 242)}}, ${{Math.round(val * 254)}})`;
          cells[i].style.boxShadow = `0 0 ${{val * 6}}px rgba(0, 242, 254, ${{val * 0.7}})`;
        }} else {{
          cells[i].style.backgroundColor = '#030509';
          cells[i].style.boxShadow = 'none';
        }}
      }});

      document.getElementById('current-label-badge').textContent = `Target: ${{sample.label}}`;
      document.getElementById('sample-index-text').textContent = `#${{currentSampleIndex + 1}} / ${{DATASET.length}}`;
      document.getElementById('sample-target-text').textContent = `Digit ${{sample.label}}`;

      // Update active filter button
      document.querySelectorAll('.digit-pill-btn').forEach((btn, idx) => {{
        btn.classList.toggle('active', idx === sample.label);
      }});

      // Run forward pass on this sample and update probability bars
      const forwardRes = nn.forward(sample.pixels);
      updateSoftmaxBars('softmax-bars-container', forwardRes.probs, sample.label);

      let winner = 0;
      let maxP = -1;
      for (let k = 0; k < 10; k++) {{
        if (forwardRes.probs[k] > maxP) {{
          maxP = forwardRes.probs[k];
          winner = k;
        }}
      }}
      const predTag = document.getElementById('current-prediction-tag');
      predTag.textContent = `Pred: ${{winner}} (${{(maxP * 100).toFixed(1)}}%)`;
      predTag.style.color = winner === sample.label ? '#10b981' : '#f59e0b';
    }}

    function updateSoftmaxBars(containerId, probs, targetLabel = null) {{
      const container = document.getElementById(containerId);
      container.innerHTML = '';

      let maxP = -1;
      let maxIdx = 0;
      for (let k = 0; k < 10; k++) {{
        if (probs[k] > maxP) {{
          maxP = probs[k];
          maxIdx = k;
        }}
      }}

      for (let k = 0; k < 10; k++) {{
        const isWinner = (k === maxIdx);
        const isTarget = (targetLabel !== null && k === targetLabel);
        const pVal = probs[k];
        const pct = (pVal * 100).toFixed(1);

        const row = document.createElement('div');
        row.className = 'prob-row';

        row.innerHTML = `
          <div class="prob-digit ${{isWinner ? 'is-winner' : ''}}">${{k}}</div>
          <div class="prob-track">
            <div class="prob-fill ${{isWinner ? 'winner-fill' : ''}}" style="width: ${{pct}}%;"></div>
          </div>
          <div class="prob-percent ${{isWinner ? 'is-winner' : ''}}">${{pct}}%</div>
        `;
        container.appendChild(row);
      }}
    }}

    // --- 6. INTERACTIVE NEURAL NETWORK CANVAS VISUALIZER ---
    let netCanvas, netCtx;
    const nodePositions = {{
      input: [],
      hidden: [],
      output: []
    }};

    function initNetworkCanvas() {{
      netCanvas = document.getElementById('network-canvas');
      netCtx = netCanvas.getContext('2d');

      function resize() {{
        const rect = netCanvas.parentElement.getBoundingClientRect();
        const dpr = Math.min(window.devicePixelRatio || 1, 2);
        netCanvas.width = rect.width * dpr;
        netCanvas.height = rect.height * dpr;
        netCtx.scale(dpr, dpr);
        calculateNodePositions(rect.width, rect.height);
      }}

      window.addEventListener('resize', resize);
      resize();

      // Mouse Hover Interaction on Network Canvas
      netCanvas.addEventListener('mousemove', (e) => {{
        const rect = netCanvas.getBoundingClientRect();
        const mouseX = e.clientX - rect.left;
        const mouseY = e.clientY - rect.top;
        
        let found = null;
        // Check input nodes
        for (let i = 0; i < nodePositions.input.length; i++) {{
          const p = nodePositions.input[i];
          const dist = Math.hypot(mouseX - p.x, mouseY - p.y);
          if (dist < 8) {{ found = {{ layer: 'input', index: i, x: p.x, y: p.y }}; break; }}
        }}
        if (!found) {{
          // Check hidden nodes
          for (let j = 0; j < nodePositions.hidden.length; j++) {{
            const p = nodePositions.hidden[j];
            const dist = Math.hypot(mouseX - p.x, mouseY - p.y);
            if (dist < 9) {{ found = {{ layer: 'hidden', index: j, x: p.x, y: p.y }}; break; }}
          }}
        }}
        if (!found) {{
          // Check output nodes
          for (let k = 0; k < nodePositions.output.length; k++) {{
            const p = nodePositions.output[k];
            const dist = Math.hypot(mouseX - p.x, mouseY - p.y);
            if (dist < 12) {{ found = {{ layer: 'output', index: k, x: p.x, y: p.y }}; break; }}
          }}
        }}

        hoveredNode = found;
        if (found) {{
          updateNodeHudTooltip(found.index, found.layer, e.clientX - rect.left + 15, e.clientY - rect.top + 15);
        }} else {{
          hideNodeHudTooltip();
        }}
      }});

      netCanvas.addEventListener('mouseleave', () => {{
        hoveredNode = null;
        hideNodeHudTooltip();
      }});
    }}

    function calculateNodePositions(width, height) {{
      nodePositions.input = [];
      nodePositions.hidden = [];
      nodePositions.output = [];

      // Input Layer (64 neurons arranged in 2 sleek vertical columns of 32)
      const inX = Math.max(40, width * 0.12);
      const inSpacingY = (height - 60) / 32;
      for (let i = 0; i < 64; i++) {{
        const col = Math.floor(i / 32);
        const row = i % 32;
        nodePositions.input.push({{
          x: inX + col * 20,
          y: 30 + row * inSpacingY,
          radius: 3.5
        }});
      }}

      // Hidden Layer (32 neurons arranged in 1 column)
      const hidX = width * 0.50;
      const hidSpacingY = (height - 60) / 32;
      for (let j = 0; j < 32; j++) {{
        nodePositions.hidden.push({{
          x: hidX,
          y: 30 + j * hidSpacingY,
          radius: 5
        }});
      }}

      // Output Layer (10 neurons with labels)
      const outX = Math.min(width - 60, width * 0.88);
      const outSpacingY = (height - 80) / 9;
      for (let k = 0; k < 10; k++) {{
        nodePositions.output.push({{
          x: outX,
          y: 40 + k * outSpacingY,
          radius: 8,
          label: k
        }});
      }}
    }}

    function updateNodeHudTooltip(index, layer, x = 20, y = 20) {{
      const tooltip = document.getElementById('node-hud-tooltip');
      const sample = DATASET[currentSampleIndex];
      const forwardRes = nn.forward(sample.pixels);

      let content = '';
      if (layer === 'input') {{
        const val = sample.pixels[index];
        content = `<strong>Input Neuron x_${{index}}</strong><br>Value: <code>${{val.toFixed(3)}}</code><br>Connections: 32 outgoing weights`;
      }} else if (layer === 'hidden') {{
        const z = forwardRes.z1[index];
        const a = forwardRes.a1[index];
        const b = nn.b1[index];
        content = `<strong>Hidden Neuron h_${{index}}</strong><br>Pre-activation z: <code>${{z.toFixed(3)}}</code><br>ReLU Activation a: <code>${{a.toFixed(3)}}</code><br>Bias b: <code>${{b.toFixed(3)}}</code>`;
      }} else if (layer === 'output') {{
        const z = forwardRes.z2[index];
        const p = forwardRes.probs[index];
        const b = nn.b2[index];
        const isTarget = (sample.label === index);
        content = `<strong>Output Neuron Digit [${{index}}]</strong><br>Logit z: <code>${{z.toFixed(3)}}</code><br>Softmax Prob: <code>${{(p * 100).toFixed(1)}}%</code><br>Bias b: <code>${{b.toFixed(3)}}</code>${{isTarget ? '<br><span style="color:#10b981">★ Ground Truth Target</span>' : ''}}`;
      }}

      tooltip.innerHTML = content;
      tooltip.style.display = 'block';
      tooltip.style.left = `${{Math.min(x, 260)}}px`;
      tooltip.style.top = `${{Math.min(y, 350)}}px`;
    }}

    function hideNodeHudTooltip() {{
      const tooltip = document.getElementById('node-hud-tooltip');
      tooltip.style.display = 'none';
    }}

    // Spawn signal particles that travel across synapses
    function triggerForwardPassAnimation() {{
      const sample = DATASET[currentSampleIndex];
      const forwardRes = nn.forward(sample.pixels);

      // Phase 1: Particles from active input nodes to hidden nodes
      for (let i = 0; i < 64; i++) {{
        if (sample.pixels[i] > 0.15) {{
          // Pick 4 top target hidden neurons
          for (let s = 0; s < 4; s++) {{
            const j = Math.floor(Math.random() * 32);
            signalParticles.push({{
              fromLayer: 'input',
              fromIdx: i,
              toLayer: 'hidden',
              toIdx: j,
              progress: 0,
              speed: 0.04 + Math.random() * 0.03,
              color: '#00f2fe',
              size: 2.5 + sample.pixels[i] * 2
            }});
          }}
        }}
      }}
    }}

    function triggerBackpropWaveAnimation() {{
      const sample = DATASET[currentSampleIndex];
      const forwardRes = nn.forward(sample.pixels);

      // Error wave from output backwards to hidden
      for (let k = 0; k < 10; k++) {{
        const err = Math.abs(forwardRes.probs[k] - (k === sample.label ? 1 : 0));
        if (err > 0.08) {{
          for (let s = 0; s < 5; s++) {{
            const j = Math.floor(Math.random() * 32);
            signalParticles.push({{
              fromLayer: 'output',
              fromIdx: k,
              toLayer: 'hidden',
              toIdx: j,
              progress: 0,
              speed: 0.05 + Math.random() * 0.03,
              color: '#ff007f',
              size: 3 + err * 3
            }});
          }}
        }}
      }}
    }}

    // Main 60fps Network Canvas Loop
    function renderNetworkFrame() {{
      if (!netCanvas || !netCtx) return;
      const width = netCanvas.clientWidth;
      const height = netCanvas.clientHeight;
      netCtx.clearRect(0, 0, width, height);

      const sample = DATASET[currentSampleIndex];
      const forwardRes = nn.forward(sample.pixels);

      // 1. Draw Synapses (Weights W1 and W2)
      // Hidden -> Output Synapses (W2)
      for (let j = 0; j < 32; j++) {{
        const hp = nodePositions.hidden[j];
        if (!hp) continue;
        for (let k = 0; k < 10; k++) {{
          const op = nodePositions.output[k];
          if (!op) continue;
          const w = nn.W2[j * 10 + k];
          
          let alpha = Math.min(Math.abs(w) * 0.75, 0.7);
          let isHighlighted = false;
          if (hoveredNode) {{
            if ((hoveredNode.layer === 'hidden' && hoveredNode.index === j) ||
                (hoveredNode.layer === 'output' && hoveredNode.index === k)) {{
              alpha = 0.95;
              isHighlighted = true;
            }} else {{
              alpha = 0.04;
            }}
          }}

          netCtx.beginPath();
          netCtx.moveTo(hp.x, hp.y);
          netCtx.lineTo(op.x, op.y);
          netCtx.strokeStyle = w > 0 ? `rgba(0, 242, 254, ${{alpha}})` : `rgba(255, 0, 127, ${{alpha}})`;
          netCtx.lineWidth = isHighlighted ? 2.5 : Math.min(Math.abs(w) * 1.5 + 0.5, 2);
          netCtx.stroke();
        }}
      }}

      // Input -> Hidden Synapses (W1)
      for (let i = 0; i < 64; i++) {{
        const ip = nodePositions.input[i];
        if (!ip) continue;
        const inVal = sample.pixels[i];
        
        for (let j = 0; j < 32; j++) {{
          const hp = nodePositions.hidden[j];
          if (!hp) continue;
          const w = nn.W1[i * 32 + j];

          let alpha = Math.min(Math.abs(w) * 0.45, 0.5);
          let isHighlighted = false;
          if (hoveredNode) {{
            if ((hoveredNode.layer === 'input' && hoveredNode.index === i) ||
                (hoveredNode.layer === 'hidden' && hoveredNode.index === j)) {{
              alpha = 0.95;
              isHighlighted = true;
            }} else {{
              alpha = 0.02;
            }}
          }} else if (inVal < 0.1) {{
            alpha *= 0.15; // Dim connections for inactive pixels
          }}

          netCtx.beginPath();
          netCtx.moveTo(ip.x, ip.y);
          netCtx.lineTo(hp.x, hp.y);
          netCtx.strokeStyle = w > 0 ? `rgba(0, 242, 254, ${{alpha}})` : `rgba(255, 0, 127, ${{alpha}})`;
          netCtx.lineWidth = isHighlighted ? 2 : Math.min(Math.abs(w) * 1.2 + 0.4, 1.6);
          netCtx.stroke();
        }}
      }}

      // 2. Animate and Draw Signal Particles
      for (let pIdx = signalParticles.length - 1; pIdx >= 0; pIdx--) {{
        const p = signalParticles[pIdx];
        p.progress += p.speed;

        let startPos, endPos;
        if (p.fromLayer === 'input' && p.toLayer === 'hidden') {{
          startPos = nodePositions.input[p.fromIdx];
          endPos = nodePositions.hidden[p.toIdx];
        }} else if (p.fromLayer === 'hidden' && p.toLayer === 'output') {{
          startPos = nodePositions.hidden[p.fromIdx];
          endPos = nodePositions.output[p.toIdx];
        }} else if (p.fromLayer === 'output' && p.toLayer === 'hidden') {{
          startPos = nodePositions.output[p.fromIdx];
          endPos = nodePositions.hidden[p.toIdx];
        }} else if (p.fromLayer === 'hidden' && p.toLayer === 'input') {{
          startPos = nodePositions.hidden[p.fromIdx];
          endPos = nodePositions.input[p.toIdx];
        }}

        if (startPos && endPos) {{
          const curX = startPos.x + (endPos.x - startPos.x) * p.progress;
          const curY = startPos.y + (endPos.y - startPos.y) * p.progress;

          netCtx.beginPath();
          netCtx.arc(curX, curY, p.size, 0, Math.PI * 2);
          netCtx.fillStyle = p.color;
          netCtx.shadowBlur = 10;
          netCtx.shadowColor = p.color;
          netCtx.fill();
          netCtx.shadowBlur = 0;
        }}

        if (p.progress >= 1) {{
          // If forward particle reached hidden layer, spawn particle to output!
          if (p.toLayer === 'hidden' && p.fromLayer === 'input') {{
            const outK = Math.floor(Math.random() * 10);
            signalParticles.push({{
              fromLayer: 'hidden',
              fromIdx: p.toIdx,
              toLayer: 'output',
              toIdx: outK,
              progress: 0,
              speed: 0.05 + Math.random() * 0.03,
              color: '#00f2fe',
              size: p.size
            }});
          }}
          // If backprop particle reached hidden, spawn to input!
          if (p.toLayer === 'hidden' && p.fromLayer === 'output') {{
            const inI = Math.floor(Math.random() * 64);
            signalParticles.push({{
              fromLayer: 'hidden',
              fromIdx: p.toIdx,
              toLayer: 'input',
              toIdx: inI,
              progress: 0,
              speed: 0.05 + Math.random() * 0.03,
              color: '#ff007f',
              size: p.size
            }});
          }}
          signalParticles.splice(pIdx, 1);
        }}
      }}

      // 3. Draw Nodes (Input, Hidden, Output)
      // Input Layer Nodes
      for (let i = 0; i < 64; i++) {{
        const p = nodePositions.input[i];
        if (!p) continue;
        const val = sample.pixels[i];
        const isHov = hoveredNode && hoveredNode.layer === 'input' && hoveredNode.index === i;

        netCtx.beginPath();
        netCtx.arc(p.x, p.y, isHov ? p.radius + 3 : p.radius, 0, Math.PI * 2);
        netCtx.fillStyle = `rgba(0, 242, 254, ${{Math.max(val, 0.15)}})`;
        netCtx.fill();

        if (val > 0.3 || isHov) {{
          netCtx.strokeStyle = isHov ? '#ffffff' : 'rgba(0, 242, 254, 0.8)';
          netCtx.lineWidth = isHov ? 2 : 1;
          netCtx.stroke();
        }}
      }}

      // Hidden Layer Nodes
      for (let j = 0; j < 32; j++) {{
        const p = nodePositions.hidden[j];
        if (!p) continue;
        const aVal = forwardRes.a1[j];
        const normA = Math.min(aVal, 2.5) / 2.5;
        const isHov = hoveredNode && hoveredNode.layer === 'hidden' && hoveredNode.index === j;

        netCtx.beginPath();
        netCtx.arc(p.x, p.y, isHov ? p.radius + 3 : p.radius, 0, Math.PI * 2);
        netCtx.fillStyle = aVal > 0 ? `rgba(139, 92, 246, ${{Math.max(normA, 0.25)}})` : 'rgba(30, 41, 59, 0.6)';
        netCtx.fill();

        netCtx.strokeStyle = isHov ? '#00f2fe' : (aVal > 0 ? 'rgba(139, 92, 246, 0.8)' : 'rgba(255, 255, 255, 0.15)');
        netCtx.lineWidth = isHov ? 2.5 : 1.5;
        netCtx.stroke();
      }}

      // Output Layer Nodes
      let maxProb = -1;
      let winningDigit = 0;
      for (let k = 0; k < 10; k++) {{
        if (forwardRes.probs[k] > maxProb) {{
          maxProb = forwardRes.probs[k];
          winningDigit = k;
        }}
      }}

      for (let k = 0; k < 10; k++) {{
        const p = nodePositions.output[k];
        if (!p) continue;
        const prob = forwardRes.probs[k];
        const isWinner = (k === winningDigit);
        const isTarget = (k === sample.label);
        const isHov = hoveredNode && hoveredNode.layer === 'output' && hoveredNode.index === k;

        netCtx.beginPath();
        netCtx.arc(p.x, p.y, isHov ? p.radius + 3 : p.radius, 0, Math.PI * 2);
        netCtx.fillStyle = isWinner ? (isTarget ? '#10b981' : '#f59e0b') : `rgba(0, 242, 254, ${{Math.max(prob, 0.15)}})`;
        netCtx.fill();

        if (isWinner || isTarget || isHov) {{
          netCtx.strokeStyle = isWinner ? (isTarget ? '#10b981' : '#f59e0b') : '#00f2fe';
          netCtx.lineWidth = isHov ? 3 : 2;
          netCtx.shadowBlur = 12;
          netCtx.shadowColor = isWinner ? (isTarget ? '#10b981' : '#f59e0b') : '#00f2fe';
          netCtx.stroke();
          netCtx.shadowBlur = 0;
        }}

        // Output Digit Label text
        netCtx.fillStyle = isWinner ? '#ffffff' : '#94a3b8';
        netCtx.font = `${{isWinner ? 'bold ' : ''}}11px 'JetBrains Mono', monospace`;
        netCtx.textAlign = 'left';
        netCtx.textBaseline = 'middle';
        netCtx.fillText(`[${{k}}] ${{(prob * 100).toFixed(0)}}%`, p.x + 14, p.y);
      }}

      requestAnimationFrame(renderNetworkFrame);
    }}

    // --- 7. LIVE LOSS & ACCURACY CURVE CHART CANVAS ---
    function renderTrainingChart() {{
      const canvas = document.getElementById('chart-canvas');
      if (!canvas) return;
      const ctx = canvas.getContext('2d');
      const dpr = Math.min(window.devicePixelRatio || 1, 2);
      
      const width = canvas.parentElement.clientWidth;
      const height = canvas.parentElement.clientHeight;
      canvas.width = width * dpr;
      canvas.height = height * dpr;
      ctx.scale(dpr, dpr);

      ctx.clearRect(0, 0, width, height);

      const history = nn.history;
      if (history.length === 0) {{
        ctx.fillStyle = '#64748b';
        ctx.font = '11px "JetBrains Mono", monospace';
        ctx.textAlign = 'center';
        ctx.fillText('Click "Start Training" to plot live learning curve', width / 2, height / 2);
        return;
      }}

      const maxSteps = Math.max(300, history[history.length - 1].step);
      const padL = 30, padR = 20, padT = 15, padB = 25;
      const plotW = width - padL - padR;
      const plotH = height - padT - padB;

      // Draw Grid Lines
      ctx.strokeStyle = 'rgba(255, 255, 255, 0.05)';
      ctx.lineWidth = 1;
      for (let yPct = 0; yPct <= 1; yPct += 0.25) {{
        const y = padT + plotH * (1 - yPct);
        ctx.beginPath();
        ctx.moveTo(padL, y);
        ctx.lineTo(padL + plotW, y);
        ctx.stroke();
      }}

      // Plot Accuracy Curve (Cyan)
      ctx.beginPath();
      for (let i = 0; i < history.length; i++) {{
        const h = history[i];
        const x = padL + (h.step / maxSteps) * plotW;
        const y = padT + plotH * (1 - h.accuracy);
        if (i === 0) ctx.moveTo(x, y);
        else ctx.lineTo(x, y);
      }}
      ctx.strokeStyle = '#00f2fe';
      ctx.lineWidth = 2;
      ctx.stroke();

      // Plot Loss Curve (Magenta)
      const maxLoss = 2.5;
      ctx.beginPath();
      for (let i = 0; i < history.length; i++) {{
        const h = history[i];
        const normLoss = Math.min(h.loss, maxLoss) / maxLoss;
        const x = padL + (h.step / maxSteps) * plotW;
        const y = padT + plotH * (1 - (1 - normLoss)); // loss starts high (top)
        if (i === 0) ctx.moveTo(x, y);
        else ctx.lineTo(x, y);
      }}
      ctx.strokeStyle = '#ff007f';
      ctx.lineWidth = 1.8;
      ctx.stroke();

      // Axis Labels
      ctx.fillStyle = '#64748b';
      ctx.font = '9px "JetBrains Mono", monospace';
      ctx.textAlign = 'left';
      ctx.fillText('0', padL, height - 8);
      ctx.textAlign = 'right';
      ctx.fillText(`Step ${{maxSteps}}`, padL + plotW, height - 8);
    }}

    // --- 8. TEST IT YOURSELF: INTERACTIVE DRAWING PAD ---
    let drawCanvas, drawCtx;
    let isDrawing = false;
    let drawDownscaledData = new Float32Array(64);

    function setupDrawingCanvas() {{
      drawCanvas = document.getElementById('user-draw-canvas');
      drawCtx = drawCanvas.getContext('2d');

      // Initialize black canvas
      drawCtx.fillStyle = '#000';
      drawCtx.fillRect(0, 0, drawCanvas.width, drawCanvas.height);

      function startDraw(e) {{
        isDrawing = true;
        draw(e);
      }}

      function stopDraw() {{
        if (isDrawing) {{
          isDrawing = false;
          drawCtx.beginPath();
          processUserDrawing();
        }}
      }}

      function draw(e) {{
        if (!isDrawing) return;
        const rect = drawCanvas.getBoundingClientRect();
        const clientX = e.clientX || (e.touches && e.touches[0].clientX);
        const clientY = e.clientY || (e.touches && e.touches[0].clientY);
        const x = clientX - rect.left;
        const y = clientY - rect.top;

        drawCtx.lineWidth = 16;
        drawCtx.lineCap = 'round';
        drawCtx.lineJoin = 'round';
        drawCtx.strokeStyle = '#ffffff';

        drawCtx.lineTo(x, y);
        drawCtx.stroke();
        drawCtx.beginPath();
        drawCtx.moveTo(x, y);

        processUserDrawing();
      }}

      drawCanvas.addEventListener('mousedown', startDraw);
      drawCanvas.addEventListener('mousemove', draw);
      window.addEventListener('mouseup', stopDraw);

      drawCanvas.addEventListener('touchstart', (e) => {{ e.preventDefault(); startDraw(e); }});
      drawCanvas.addEventListener('touchmove', (e) => {{ e.preventDefault(); draw(e); }});
      window.addEventListener('touchend', stopDraw);

      document.getElementById('btn-clear-draw').addEventListener('click', clearDrawingCanvas);
      document.getElementById('btn-send-draw-to-net').addEventListener('click', () => {{
        // Set drawn pixels into input visualizer
        DATASET[currentSampleIndex].pixels.set(drawDownscaledData);
        renderCurrentSample();
        triggerForwardPassAnimation();
        // Scroll smoothly to architecture
        document.getElementById('studio').scrollIntoView({{ behavior: 'smooth' }});
      }});

      // Preset button handlers
      document.querySelectorAll('.preset-draw-btn').forEach(btn => {{
        btn.addEventListener('click', () => {{
          const digit = parseInt(btn.dataset.digit, 10);
          loadPresetDrawing(digit);
        }});
      }});

      // Setup 8x8 downscaled preview grid DOM
      const previewGrid = document.getElementById('downscaled-preview-grid');
      previewGrid.innerHTML = '';
      for (let i = 0; i < 64; i++) {{
        const cell = document.createElement('div');
        cell.className = 'downscaled-cell';
        previewGrid.appendChild(cell);
      }}
    }}

    function clearDrawingCanvas() {{
      drawCtx.fillStyle = '#000';
      drawCtx.fillRect(0, 0, drawCanvas.width, drawCanvas.height);
      drawCtx.beginPath();
      drawDownscaledData.fill(0);
      updateDownscaledPreview();
      updateDrawPredictions();
    }}

    function processUserDrawing() {{
      const imgData = drawCtx.getImageData(0, 0, drawCanvas.width, drawCanvas.height);
      const data = imgData.data;
      const w = drawCanvas.width;
      const h = drawCanvas.height;

      // Find bounding box
      let minX = w, minY = h, maxX = 0, maxY = 0;
      let hasInk = false;
      for (let y = 0; y < h; y++) {{
        for (let x = 0; x < w; x++) {{
          const idx = (y * w + x) * 4;
          if (data[idx] > 30) {{ // Ink threshold
            hasInk = true;
            if (x < minX) minX = x;
            if (x > maxX) maxX = x;
            if (y < minY) minY = y;
            if (y > maxY) maxY = y;
          }}
        }}
      }}

      if (!hasInk) {{
        drawDownscaledData.fill(0);
        updateDownscaledPreview();
        updateDrawPredictions();
        return;
      }}

      // Crop and center inside an 8x8 grid with 1-cell border margin (matching sklearn optdigits)
      const boxW = Math.max(1, maxX - minX + 1);
      const boxH = Math.max(1, maxY - minY + 1);
      const maxDim = Math.max(boxW, boxH);

      // Create an intermediate offscreen canvas
      const offCanvas = document.createElement('canvas');
      offCanvas.width = 8;
      offCanvas.height = 8;
      const offCtx = offCanvas.getContext('2d');
      offCtx.fillStyle = '#000';
      offCtx.fillRect(0, 0, 8, 8);

      // Fit inside 6x6 area centered in 8x8
      const targetSize = 6;
      const scale = targetSize / maxDim;
      const drawW = boxW * scale;
      const drawH = boxH * scale;
      const targetX = 1 + (targetSize - drawW) / 2;
      const targetY = 1 + (targetSize - drawH) / 2;

      offCtx.drawImage(drawCanvas, minX, minY, boxW, boxH, targetX, targetY, drawW, drawH);

      const downData = offCtx.getImageData(0, 0, 8, 8).data;
      for (let i = 0; i < 64; i++) {{
        drawDownscaledData[i] = Math.min(1.0, downData[i * 4] / 220.0);
      }}

      updateDownscaledPreview();
      updateDrawPredictions();
    }}

    function updateDownscaledPreview() {{
      const cells = document.querySelectorAll('.downscaled-cell');
      for (let i = 0; i < 64; i++) {{
        const v = drawDownscaledData[i];
        if (v > 0.05) {{
          cells[i].style.backgroundColor = `rgba(0, 242, 254, ${{v}})`;
        }} else {{
          cells[i].style.backgroundColor = '#000';
        }}
      }}
    }}

    function updateDrawPredictions() {{
      const {{ probs }} = nn.forward(drawDownscaledData);
      let maxP = -1;
      let winner = 0;
      for (let k = 0; k < 10; k++) {{
        if (probs[k] > maxP) {{
          maxP = probs[k];
          winner = k;
        }}
      }}

      const badge = document.getElementById('draw-predicted-badge');
      const confText = document.getElementById('draw-confidence-text');

      badge.textContent = winner;
      confText.textContent = `Confidence: ${{(maxP * 100).toFixed(1)}}%`;

      updateSoftmaxBars('draw-softmax-bars-container', probs);
    }}

    function loadPresetDrawing(digit) {{
      const sample = DATASET.find(s => s.label === digit);
      if (!sample) return;

      // Draw scaled 8x8 into the draw canvas
      drawCtx.fillStyle = '#000';
      drawCtx.fillRect(0, 0, drawCanvas.width, drawCanvas.height);

      const cellSize = drawCanvas.width / 8;
      for (let r = 0; r < 8; r++) {{
        for (let c = 0; c < 8; c++) {{
          const val = sample.pixels[r * 8 + c];
          if (val > 0.1) {{
            drawCtx.beginPath();
            drawCtx.arc(c * cellSize + cellSize / 2, r * cellSize + cellSize / 2, (cellSize / 2) * val, 0, Math.PI * 2);
            drawCtx.fillStyle = '#ffffff';
            drawCtx.fill();
          }}
        }}
      }}
      processUserDrawing();
    }}

    // --- 9. TRAINING LOOP & CONTROLS ---
    function updateDashboardMetrics(stepRes = null) {{
      const evalRes = stepRes || nn.evaluate(DATASET);
      const accPct = (evalRes.accuracy * 100).toFixed(1);
      const lossVal = evalRes.loss.toFixed(3);

      document.getElementById('metric-accuracy-val').textContent = `${{accPct}}%`;
      document.getElementById('metric-loss-val').textContent = lossVal;
      document.getElementById('metric-step-text').textContent = `${{nn.step}} / 300`;

      const progressPct = Math.min(100, (nn.step / 300) * 100);
      document.getElementById('training-progress-fill').style.width = `${{progressPct}}%`;

      renderTrainingChart();
      renderCurrentSample();
    }}

    function stepTraining() {{
      const lr = parseFloat(document.getElementById('slider-lr').value) || 0.65;
      const res = nn.trainStep(DATASET, lr);
      updateDashboardMetrics(res);

      if (currentAnimationMode === 'forward') {{
        triggerForwardPassAnimation();
      }} else {{
        triggerBackpropWaveAnimation();
      }}

      if (nn.step >= 300 && isTraining) {{
        toggleTraining(false);
      }}
    }}

    function toggleTraining(forcedState = null) {{
      isTraining = (forcedState !== null) ? forcedState : !isTraining;
      const btn = document.getElementById('btn-toggle-train');
      const label = document.getElementById('train-btn-label');
      const icon = document.getElementById('train-btn-icon');
      const statusPill = document.getElementById('training-status-pill');

      if (isTraining) {{
        label.textContent = 'Pause Training';
        icon.textContent = '⏸';
        btn.classList.add('btn-accent');
        statusPill.textContent = 'Training Live...';
        statusPill.style.color = '#00f2fe';
        statusPill.style.borderColor = '#00f2fe';

        const speed = parseInt(document.getElementById('slider-speed').value, 10) || 20;
        const intervalMs = Math.max(16, Math.round(1000 / speed));

        trainingIntervalId = setInterval(() => {{
          stepTraining();
        }}, intervalMs);
      }} else {{
        label.textContent = 'Start Training';
        icon.textContent = '▶';
        btn.classList.remove('btn-accent');
        statusPill.textContent = nn.step >= 300 ? 'Completed' : 'Paused';
        statusPill.style.color = nn.step >= 300 ? '#10b981' : '#94a3b8';
        statusPill.style.borderColor = 'rgba(255, 255, 255, 0.09)';

        if (trainingIntervalId) {{
          clearInterval(trainingIntervalId);
          trainingIntervalId = null;
        }}
      }}
    }}

    // --- 10. EVENT LISTENERS & INITIALIZATION ---
    window.addEventListener('DOMContentLoaded', () => {{
      setupHeroCanvas();
      setupPixelGrid();
      initNetworkCanvas();
      setupDrawingCanvas();

      // Initial Evaluation
      const initRes = nn.evaluate(DATASET);
      nn.history.push({{ step: 0, loss: initRes.loss, accuracy: initRes.accuracy }});
      updateDashboardMetrics(initRes);
      renderCurrentSample();
      renderNetworkFrame();

      // Sample Navigation Buttons
      document.getElementById('btn-prev-sample').addEventListener('click', () => {{
        currentSampleIndex = (currentSampleIndex - 1 + DATASET.length) % DATASET.length;
        renderCurrentSample();
        triggerForwardPassAnimation();
      }});

      document.getElementById('btn-next-sample').addEventListener('click', () => {{
        currentSampleIndex = (currentSampleIndex + 1) % DATASET.length;
        renderCurrentSample();
        triggerForwardPassAnimation();
      }});

      document.getElementById('btn-random-sample').addEventListener('click', () => {{
        currentSampleIndex = Math.floor(Math.random() * DATASET.length);
        renderCurrentSample();
        triggerForwardPassAnimation();
      }});

      document.getElementById('btn-send-to-network').addEventListener('click', () => {{
        triggerForwardPassAnimation();
      }});

      document.getElementById('btn-pulse-wave').addEventListener('click', () => {{
        if (currentAnimationMode === 'forward') triggerForwardPassAnimation();
        else triggerBackpropWaveAnimation();
      }});

      // Animation Mode Toggles
      const btnModeFwd = document.getElementById('btn-mode-forward');
      const btnModeBwd = document.getElementById('btn-mode-backprop');

      btnModeFwd.addEventListener('click', () => {{
        currentAnimationMode = 'forward';
        btnModeFwd.classList.add('active');
        btnModeBwd.classList.remove('active');
        triggerForwardPassAnimation();
      }});

      btnModeBwd.addEventListener('click', () => {{
        currentAnimationMode = 'backprop';
        btnModeBwd.classList.add('active');
        btnModeFwd.classList.remove('active');
        triggerBackpropWaveAnimation();
      }});

      // Dashboard Controls
      document.getElementById('btn-toggle-train').addEventListener('click', () => toggleTraining());
      document.getElementById('btn-step-train').addEventListener('click', () => stepTraining());

      document.getElementById('btn-reset-train').addEventListener('click', () => {{
        toggleTraining(false);
        nn.reset();
        const initRes = nn.evaluate(DATASET);
        nn.history.push({{ step: 0, loss: initRes.loss, accuracy: initRes.accuracy }});
        updateDashboardMetrics(initRes);
      }});

      document.getElementById('btn-instant-train').addEventListener('click', () => {{
        toggleTraining(false);
        const lr = parseFloat(document.getElementById('slider-lr').value) || 0.65;
        while (nn.step < 300) {{
          nn.trainStep(DATASET, lr);
        }}
        updateDashboardMetrics();
        triggerForwardPassAnimation();
      }});

      // Sliders
      const speedSlider = document.getElementById('slider-speed');
      const speedLabel = document.getElementById('speed-label');
      speedSlider.addEventListener('input', (e) => {{
        const v = parseInt(e.target.value, 10);
        speedLabel.textContent = `${{v}} steps/sec`;
        if (isTraining) {{
          // Restart timer with new speed
          toggleTraining(false);
          toggleTraining(true);
        }}
      }});

      const lrSlider = document.getElementById('slider-lr');
      const lrLabel = document.getElementById('lr-label');
      lrSlider.addEventListener('input', (e) => {{
        lrLabel.textContent = parseFloat(e.target.value).toFixed(2);
      }});

      // Scroll observer for Math Cards fade-in
      const observer = new IntersectionObserver((entries) => {{
        entries.forEach(entry => {{
          if (entry.isIntersecting) {{
            entry.target.classList.add('visible');
          }}
        }});
      }}, {{ threshold: 0.15 }});

      document.querySelectorAll('.math-card').forEach(card => observer.observe(card));
    }});
  </script>
</body>
</html>"""

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html_template)

print("Generated validated index.html successfully!")
