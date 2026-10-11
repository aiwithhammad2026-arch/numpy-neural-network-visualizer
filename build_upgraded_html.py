import json

with open('dataset_js.txt', 'r') as f:
    dataset_code = f.read().strip()

html_template = f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Neural Network from Scratch | Interactive Laboratory</title>
  <meta name="description" content="An interactive, ultra-smooth 64->32->10 Neural Network learning handwritten digits with pure JavaScript and backpropagation.">
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=JetBrains+Mono:wght@400;500;700&family=Space+Grotesk:wght@400;500;600;700;800&display=swap" rel="stylesheet">

  <style>
    :root {{
      --bg-dark: #07080d;
      --bg-card: rgba(14, 18, 30, 0.78);
      --bg-card-hover: rgba(20, 26, 44, 0.9);
      --border-subtle: rgba(255, 255, 255, 0.08);
      --border-glow: rgba(0, 242, 254, 0.35);
      
      --cyan: #00f2fe;
      --cyan-glow: rgba(0, 242, 254, 0.4);
      --magenta: #ff007f;
      --magenta-glow: rgba(255, 0, 127, 0.4);
      --purple: #8b5cf6;
      --purple-glow: rgba(139, 92, 246, 0.4);
      --emerald: #10b981;
      --emerald-glow: rgba(16, 185, 129, 0.4);
      --amber: #f59e0b;
      --amber-glow: rgba(245, 158, 11, 0.4);
      
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

    html, body {{
      width: 100vw;
      height: 100vh;
      overflow: hidden;
      background-color: var(--bg-dark);
      color: var(--text-main);
      font-family: var(--font-main);
      line-height: 1.4;
      background-image: 
        radial-gradient(circle at 15% 20%, rgba(0, 242, 254, 0.06) 0%, transparent 40%),
        radial-gradient(circle at 85% 30%, rgba(139, 92, 246, 0.06) 0%, transparent 45%),
        radial-gradient(circle at 50% 85%, rgba(255, 0, 127, 0.05) 0%, transparent 50%);
    }}

    /* Scrollbar for overflow tabs if needed */
    ::-webkit-scrollbar {{
      width: 6px;
      height: 6px;
    }}
    ::-webkit-scrollbar-track {{
      background: rgba(7, 8, 13, 0.8);
    }}
    ::-webkit-scrollbar-thumb {{
      background: rgba(255, 255, 255, 0.15);
      border-radius: 3px;
    }}
    ::-webkit-scrollbar-thumb:hover {{
      background: var(--cyan);
    }}

    /* Compact Top Header (Height ~52px) */
    header {{
      height: 52px;
      padding: 0 16px;
      display: flex;
      justify-content: space-between;
      align-items: center;
      border-bottom: 1px solid var(--border-subtle);
      background: rgba(8, 10, 18, 0.85);
      backdrop-filter: blur(14px);
      z-index: 100;
      position: relative;
    }}

    .brand-group {{
      display: flex;
      align-items: center;
      gap: 10px;
    }}

    .brand-logo {{
      width: 28px;
      height: 28px;
      border-radius: 7px;
      background: linear-gradient(135deg, var(--cyan), var(--purple));
      display: flex;
      align-items: center;
      justify-content: center;
      box-shadow: 0 0 12px var(--cyan-glow);
    }}

    .brand-title {{
      font-size: 1.05rem;
      font-weight: 700;
      letter-spacing: -0.02em;
      color: var(--text-main);
      display: flex;
      align-items: center;
      gap: 6px;
    }}

    .author-badge {{
      display: inline-flex;
      align-items: center;
      gap: 5px;
      padding: 3px 9px;
      border-radius: 6px;
      background: rgba(139, 92, 246, 0.12);
      border: 1px solid rgba(139, 92, 246, 0.35);
      color: #c084fc;
      font-size: 0.72rem;
      font-family: var(--font-mono);
      font-weight: 600;
    }}

    /* Navigation Tabs */
    .tab-nav {{
      display: flex;
      gap: 6px;
      background: rgba(0, 0, 0, 0.4);
      padding: 3px;
      border-radius: 8px;
      border: 1px solid var(--border-subtle);
    }}

    .tab-btn {{
      padding: 5px 14px;
      border-radius: 6px;
      font-size: 0.8rem;
      font-weight: 600;
      font-family: var(--font-main);
      color: var(--text-muted);
      background: transparent;
      border: none;
      cursor: pointer;
      transition: all 0.2s ease;
      display: flex;
      align-items: center;
      gap: 6px;
    }}

    .tab-btn:hover {{
      color: var(--text-main);
      background: rgba(255, 255, 255, 0.05);
    }}

    .tab-btn.active {{
      background: rgba(0, 242, 254, 0.12);
      color: var(--cyan);
      box-shadow: inset 0 0 0 1px rgba(0, 242, 254, 0.4);
    }}

    /* Header Right Badges */
    .header-right {{
      display: flex;
      align-items: center;
      gap: 10px;
    }}

    .fps-badge {{
      font-family: var(--font-mono);
      font-size: 0.72rem;
      font-weight: 700;
      color: var(--emerald);
      background: rgba(16, 185, 129, 0.1);
      border: 1px solid rgba(16, 185, 129, 0.3);
      padding: 3px 8px;
      border-radius: 6px;
      display: flex;
      align-items: center;
      gap: 5px;
    }}

    .fps-dot {{
      width: 5px;
      height: 5px;
      border-radius: 50%;
      background: var(--emerald);
      box-shadow: 0 0 6px var(--emerald);
      animation: pulseDot 1.5s infinite ease-in-out;
    }}

    @keyframes pulseDot {{
      0%, 100% {{ opacity: 0.4; transform: scale(0.85); }}
      50% {{ opacity: 1; transform: scale(1.25); }}
    }}

    /* Main View Area (100vh - 52px header) */
    .app-viewport {{
      width: 100vw;
      height: calc(100vh - 52px);
      position: relative;
      overflow: hidden;
    }}

    /* Tab Content Pages */
    .tab-page {{
      position: absolute;
      top: 0;
      left: 0;
      width: 100%;
      height: 100%;
      opacity: 0;
      pointer-events: none;
      transition: opacity 0.25s ease, transform 0.25s ease;
      transform: translateY(8px);
      overflow: hidden;
    }}

    .tab-page.active {{
      opacity: 1;
      pointer-events: auto;
      transform: translateY(0);
    }}

    /* --- TAB 1: 3-COLUMN STUDIO LAYOUT (FIT TO SCREEN) --- */
    .studio-layout {{
      display: grid;
      grid-template-columns: 290px 1fr 290px;
      height: 100%;
      gap: 10px;
      padding: 10px 12px;
    }}

    @media (max-width: 1100px) {{
      .studio-layout {{
        grid-template-columns: 260px 1fr 260px;
        padding: 8px;
        gap: 8px;
      }}
    }}

    @media (max-width: 900px) {{
      html, body {{
        overflow-y: auto;
        height: auto;
      }}
      .app-viewport {{
        height: auto;
        overflow: visible;
      }}
      .tab-page {{
        position: relative;
        height: auto;
        overflow: visible;
      }}
      .studio-layout {{
        grid-template-columns: 1fr;
        height: auto;
      }}
    }}

    /* Card Panels */
    .panel-card {{
      background: var(--bg-card);
      border: 1px solid var(--border-subtle);
      border-radius: 12px;
      backdrop-filter: blur(16px);
      display: flex;
      flex-direction: column;
      overflow: hidden;
      box-shadow: 0 6px 24px rgba(0, 0, 0, 0.45);
      position: relative;
    }}

    .panel-header {{
      padding: 8px 12px;
      border-bottom: 1px solid var(--border-subtle);
      display: flex;
      justify-content: space-between;
      align-items: center;
      background: rgba(255, 255, 255, 0.02);
    }}

    .panel-title {{
      font-size: 0.82rem;
      font-weight: 700;
      letter-spacing: -0.01em;
      display: flex;
      align-items: center;
      gap: 6px;
      color: var(--text-main);
    }}

    .panel-body {{
      padding: 10px 12px;
      display: flex;
      flex-direction: column;
      gap: 10px;
      overflow-y: auto;
      flex: 1;
    }}

    /* Left Column Modules */
    .grid-8x8-wrapper {{
      display: flex;
      flex-direction: column;
      align-items: center;
      gap: 8px;
    }}

    .grid-8x8 {{
      display: grid;
      grid-template-columns: repeat(8, 1fr);
      gap: 2px;
      width: 140px;
      height: 140px;
      background: rgba(0, 0, 0, 0.7);
      padding: 4px;
      border-radius: 8px;
      border: 1px solid var(--border-subtle);
      box-shadow: inset 0 2px 6px rgba(0, 0, 0, 0.8);
    }}

    .pixel-cell {{
      width: 100%;
      height: 100%;
      border-radius: 1px;
      background: #000;
      transition: background-color 0.15s ease, box-shadow 0.15s ease;
      cursor: pointer;
    }}

    .pixel-cell:hover {{
      transform: scale(1.15);
      z-index: 10;
      outline: 1.5px solid var(--cyan);
    }}

    /* Sample Selector Controls */
    .sample-controls {{
      display: flex;
      align-items: center;
      justify-content: space-between;
      width: 100%;
      gap: 5px;
    }}

    .btn {{
      display: inline-flex;
      align-items: center;
      justify-content: center;
      gap: 6px;
      padding: 6px 10px;
      border-radius: 6px;
      font-size: 0.78rem;
      font-weight: 600;
      font-family: var(--font-main);
      cursor: pointer;
      transition: all 0.2s cubic-bezier(0.16, 1, 0.3, 1);
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
      box-shadow: 0 3px 12px rgba(0, 242, 254, 0.35);
    }}

    .btn-primary:hover {{
      background: linear-gradient(135deg, #38f9d7, #4facfe);
      box-shadow: 0 4px 16px rgba(0, 242, 254, 0.5);
    }}

    .btn-accent {{
      background: linear-gradient(135deg, #ff007f, #7928ca);
      color: #fff;
      border: none;
      box-shadow: 0 3px 12px rgba(255, 0, 127, 0.35);
    }}

    .btn-accent:hover {{
      background: linear-gradient(135deg, #ff3399, #9333ea);
      box-shadow: 0 4px 16px rgba(255, 0, 127, 0.5);
    }}

    .btn-sm {{
      padding: 4px 8px;
      font-size: 0.72rem;
    }}

    .digit-filter-bar {{
      display: flex;
      flex-wrap: wrap;
      gap: 3px;
      justify-content: center;
      width: 100%;
    }}

    .digit-pill-btn {{
      width: 22px;
      height: 22px;
      border-radius: 4px;
      background: rgba(255, 255, 255, 0.04);
      border: 1px solid var(--border-subtle);
      color: var(--text-muted);
      font-size: 0.7rem;
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
      box-shadow: 0 0 8px var(--cyan-glow);
    }}

    .sample-info-hud {{
      display: flex;
      justify-content: space-between;
      width: 100%;
      padding: 5px 8px;
      border-radius: 6px;
      background: rgba(0, 0, 0, 0.4);
      border: 1px solid var(--border-subtle);
      font-family: var(--font-mono);
      font-size: 0.72rem;
    }}

    /* Softmax Probability Bars */
    .prob-bars-list {{
      display: flex;
      flex-direction: column;
      gap: 3px;
      width: 100%;
    }}

    .prob-row {{
      display: flex;
      align-items: center;
      gap: 6px;
      font-family: var(--font-mono);
      font-size: 0.72rem;
    }}

    .prob-digit {{
      width: 14px;
      font-weight: 700;
      color: var(--text-muted);
    }}

    .prob-digit.is-winner {{
      color: var(--cyan);
      text-shadow: 0 0 6px var(--cyan);
    }}

    .prob-track {{
      flex: 1;
      height: 8px;
      background: rgba(255, 255, 255, 0.05);
      border-radius: 2px;
      overflow: hidden;
      position: relative;
    }}

    .prob-fill {{
      height: 100%;
      width: 0%;
      background: linear-gradient(90deg, rgba(0, 242, 254, 0.6), var(--cyan));
      border-radius: 2px;
      transition: width 0.12s ease;
    }}

    .prob-fill.winner-fill {{
      background: linear-gradient(90deg, #10b981, #00f2fe);
      box-shadow: 0 0 6px var(--cyan);
    }}

    .prob-percent {{
      width: 36px;
      text-align: right;
      color: var(--text-dim);
      font-size: 0.68rem;
    }}

    .prob-percent.is-winner {{
      color: var(--text-main);
      font-weight: 700;
    }}

    /* Center Network Canvas Container */
    .center-canvas-panel {{
      display: flex;
      flex-direction: column;
      height: 100%;
      border-radius: 12px;
      background: rgba(5, 7, 14, 0.9);
      border: 1px solid var(--border-subtle);
      overflow: hidden;
      position: relative;
    }}

    .canvas-hud-header {{
      padding: 6px 14px;
      display: flex;
      justify-content: space-between;
      align-items: center;
      background: rgba(255, 255, 255, 0.02);
      border-bottom: 1px solid var(--border-subtle);
      z-index: 10;
    }}

    .canvas-legend-row {{
      display: flex;
      gap: 12px;
      font-size: 0.7rem;
      font-family: var(--font-mono);
    }}

    .legend-item {{
      display: flex;
      align-items: center;
      gap: 4px;
    }}

    .legend-dot {{
      width: 7px;
      height: 7px;
      border-radius: 50%;
    }}

    .network-canvas-wrapper {{
      flex: 1;
      width: 100%;
      height: 100%;
      position: relative;
      overflow: hidden;
    }}

    #network-canvas {{
      width: 100%;
      height: 100%;
      display: block;
      cursor: crosshair;
    }}

    /* Canvas Bottom Action Bar */
    .canvas-hud-bottom {{
      padding: 6px 12px;
      display: flex;
      justify-content: space-between;
      align-items: center;
      background: rgba(8, 11, 20, 0.85);
      border-top: 1px solid var(--border-subtle);
      z-index: 10;
      flex-wrap: wrap;
      gap: 6px;
    }}

    .wave-control-group {{
      display: flex;
      align-items: center;
      gap: 8px;
    }}

    .hud-tooltip {{
      position: absolute;
      bottom: 45px;
      left: 14px;
      background: rgba(9, 14, 25, 0.94);
      border: 1px solid var(--cyan);
      border-radius: 8px;
      padding: 7px 11px;
      font-family: var(--font-mono);
      font-size: 0.72rem;
      color: var(--text-main);
      box-shadow: 0 4px 18px rgba(0, 242, 254, 0.25);
      pointer-events: none;
      display: none;
      z-index: 50;
      backdrop-filter: blur(10px);
    }}

    /* Right Column: Training Dashboard */
    .metric-grid-2 {{
      display: grid;
      grid-template-columns: 1fr 1fr;
      gap: 8px;
    }}

    .metric-card {{
      background: rgba(0, 0, 0, 0.45);
      border: 1px solid var(--border-subtle);
      border-radius: 8px;
      padding: 8px;
      text-align: center;
    }}

    .metric-card-label {{
      font-size: 0.68rem;
      font-family: var(--font-mono);
      color: var(--text-muted);
      text-transform: uppercase;
      letter-spacing: 0.04em;
      margin-bottom: 2px;
    }}

    .metric-card-num {{
      font-size: 1.35rem;
      font-weight: 800;
      font-family: var(--font-mono);
      color: var(--cyan);
      text-shadow: 0 0 12px var(--cyan-glow);
    }}

    .metric-card-num.loss {{
      color: var(--magenta);
      text-shadow: 0 0 12px var(--magenta-glow);
    }}

    .progress-bar-wrapper {{
      width: 100%;
      height: 5px;
      background: rgba(255, 255, 255, 0.06);
      border-radius: 3px;
      overflow: hidden;
      margin: 4px 0 8px;
    }}

    .progress-bar-fill {{
      height: 100%;
      width: 0%;
      background: linear-gradient(90deg, var(--cyan), var(--purple), var(--magenta));
      transition: width 0.12s ease;
      box-shadow: 0 0 6px var(--cyan);
    }}

    .control-row {{
      display: flex;
      flex-direction: column;
      gap: 4px;
    }}

    .control-label {{
      display: flex;
      justify-content: space-between;
      font-size: 0.72rem;
      font-family: var(--font-mono);
      color: var(--text-muted);
    }}

    .control-label strong {{
      color: var(--text-main);
    }}

    input[type="range"] {{
      -webkit-appearance: none;
      width: 100%;
      height: 4px;
      border-radius: 4px;
      background: rgba(255, 255, 255, 0.12);
      outline: none;
      transition: background 0.2s;
    }}

    input[type="range"]::-webkit-slider-thumb {{
      -webkit-appearance: none;
      appearance: none;
      width: 13px;
      height: 13px;
      border-radius: 50%;
      background: var(--cyan);
      cursor: pointer;
      box-shadow: 0 0 8px var(--cyan);
      transition: transform 0.1s;
    }}

    input[type="range"]::-webkit-slider-thumb:hover {{
      transform: scale(1.2);
    }}

    .chart-container {{
      width: 100%;
      height: 110px;
      background: rgba(4, 6, 12, 0.75);
      border: 1px solid var(--border-subtle);
      border-radius: 8px;
      position: relative;
      overflow: hidden;
    }}

    #chart-canvas {{
      width: 100%;
      height: 100%;
      display: block;
    }}

    /* --- TAB 2: DRAW & TEST --- */
    .draw-tab-content {{
      max-width: 960px;
      margin: 20px auto;
      padding: 0 20px;
      height: 100%;
      overflow-y: auto;
    }}

    .draw-layout-grid {{
      display: grid;
      grid-template-columns: 1fr 1fr;
      gap: 24px;
      align-items: center;
      margin-top: 14px;
    }}

    .draw-canvas {{
      width: 220px;
      height: 220px;
      background: #000;
      border: 2px solid var(--border-subtle);
      border-radius: 12px;
      cursor: crosshair;
      box-shadow: 0 4px 20px rgba(0, 0, 0, 0.6);
      touch-action: none;
    }}

    .downscaled-grid {{
      width: 90px;
      height: 90px;
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

    .big-digit-badge {{
      width: 60px;
      height: 60px;
      border-radius: 12px;
      background: linear-gradient(135deg, rgba(0, 242, 254, 0.15), rgba(139, 92, 246, 0.15));
      border: 1px solid var(--cyan);
      display: flex;
      align-items: center;
      justify-content: center;
      font-size: 2.4rem;
      font-weight: 800;
      font-family: var(--font-mono);
      color: var(--cyan);
      box-shadow: 0 0 20px var(--cyan-glow);
    }}

    /* --- TAB 3: HOW IT WORKS --- */
    .math-tab-content {{
      max-width: 1100px;
      margin: 20px auto;
      padding: 0 20px 40px;
      height: 100%;
      overflow-y: auto;
    }}

    .math-cards-grid {{
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(260px, 1fr));
      gap: 16px;
      margin-top: 16px;
    }}

    .math-card {{
      background: var(--bg-card);
      border: 1px solid var(--border-subtle);
      border-radius: 12px;
      padding: 18px;
      backdrop-filter: blur(14px);
      transition: transform 0.2s ease, border-color 0.2s ease;
    }}

    .math-card:hover {{
      border-color: var(--cyan);
      transform: translateY(-2px);
    }}

    .card-step-badge {{
      display: inline-flex;
      align-items: center;
      justify-content: center;
      width: 26px;
      height: 26px;
      border-radius: 6px;
      background: rgba(0, 242, 254, 0.1);
      border: 1px solid rgba(0, 242, 254, 0.3);
      color: var(--cyan);
      font-weight: 800;
      font-family: var(--font-mono);
      font-size: 0.8rem;
      margin-bottom: 10px;
    }}

    .math-formula-box {{
      background: rgba(0, 0, 0, 0.5);
      border: 1px solid var(--border-subtle);
      border-radius: 6px;
      padding: 8px 10px;
      font-family: var(--font-mono);
      font-size: 0.78rem;
      color: var(--cyan);
      margin: 10px 0;
      overflow-x: auto;
    }}
  </style>
</head>
<body>

  <!-- Compact Sticky Header -->
  <header>
    <div class="brand-group">
      <div class="brand-logo">
        <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="#050b14" stroke-width="2.5">
          <circle cx="12" cy="12" r="3"></circle>
          <path d="M19.4 15a1.65 1.65 0 0 0 .33 1.82l.06.06a2 2 0 0 1 0 2.83 2 2 0 0 1-2.83 0l-.06-.06a1.65 1.65 0 0 0-1.82-.33 1.65 1.65 0 0 0-1 1.51V21a2 2 0 0 1-2 2 2 2 0 0 1-2-2v-.09A1.65 1.65 0 0 0 9 19.4a1.65 1.65 0 0 0-1.82.33l-.06.06a2 2 0 0 1-2.83 0 2 2 0 0 1 0-2.83l.06-.06a1.65 1.65 0 0 0 .33-1.82 1.65 1.65 0 0 0-1.51-1H3a2 2 0 0 1-2-2 2 2 0 0 1 2-2h.09A1.65 1.65 0 0 0 4.6 9a1.65 1.65 0 0 0-.33-1.82l-.06-.06a2 2 0 0 1 0-2.83 2 2 0 0 1 2.83 0l.06.06a1.65 1.65 0 0 0 1.82.33H9a1.65 1.65 0 0 0 1-1.51V3a2 2 0 0 1 2-2 2 2 0 0 1 2 2v.09a1.65 1.65 0 0 0 1 1.51 1.65 1.65 0 0 0 1.82-.33l.06-.06a2 2 0 0 1 2.83 0 2 2 0 0 1 0 2.83l-.06.06a1.65 1.65 0 0 0-.33 1.82V9a1.65 1.65 0 0 0 1.51 1H21a2 2 0 0 1 2 2 2 2 0 0 1-2 2h-.09a1.65 1.65 0 0 0-1.51 1z"></path>
        </svg>
      </div>
      <div class="brand-title">
        <span>NeuroGraph<span style="color:var(--cyan)">.js</span></span>
      </div>
      <a href="mailto:aiwithhammad2026@gmail.com" class="author-badge" title="Contact Hammad, AI Engineer (aiwithhammad2026@gmail.com)" style="text-decoration:none; cursor:pointer;">
        <span>✦ By Hammad, AI Engineer</span>
        <span style="opacity:0.6; font-size:0.65rem;">• aiwithhammad2026@gmail.com</span>
      </a>
    </div>

    <!-- Navigation Tabs -->
    <div class="tab-nav">
      <button class="tab-btn active" data-tab="studio">
        <span>🔬 Live Studio</span>
      </button>
      <button class="tab-btn" data-tab="draw">
        <span>✍️ Draw & Test</span>
      </button>
      <button class="tab-btn" data-tab="math">
        <span>📖 How It Works</span>
      </button>
    </div>

    <!-- Right HUD Status -->
    <div class="header-right">
      <div class="fps-badge">
        <span class="fps-dot"></span>
        <span id="fps-counter-val">240 FPS</span>
      </div>
    </div>
  </header>

  <!-- Viewport Container -->
  <div class="app-viewport">
    
    <!-- ==================== TAB 1: 3-COLUMN STUDIO ==================== -->
    <div class="tab-page active" id="tab-studio">
      <div class="studio-layout">
        
        <!-- Left Column: Input Visualizer & Softmax Distribution -->
        <div style="display: flex; flex-direction: column; gap: 8px; height: 100%;">
          
          <!-- 8x8 Input Card -->
          <div class="panel-card" style="flex: 1.2;">
            <div class="panel-header">
              <span class="panel-title">
                <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="3" y="3" width="18" height="18" rx="2"/><path d="M3 9h18M9 21V9"/></svg>
                8×8 Input Matrix (64 Pixels)
              </span>
              <span id="current-label-badge" style="font-size:0.7rem; font-family:var(--font-mono); color:var(--cyan); font-weight:700;">Target: 0</span>
            </div>
            
            <div class="panel-body">
              <div class="grid-8x8-wrapper">
                <div class="grid-8x8" id="pixel-grid-container"></div>
                
                <div class="sample-info-hud">
                  <span>Sample: <strong id="sample-index-text" style="color:var(--cyan)">#1/350</strong></span>
                  <span>Digit: <strong id="sample-target-text" style="color:var(--emerald)">0</strong></span>
                </div>

                <div class="sample-controls">
                  <button class="btn btn-sm" id="btn-prev-sample">◀ Prev</button>
                  <button class="btn btn-sm" id="btn-random-sample">🎲 Rand</button>
                  <button class="btn btn-sm" id="btn-next-sample">Next ▶</button>
                </div>

                <div class="digit-filter-bar" id="digit-filter-container"></div>
              </div>
            </div>
          </div>

          <!-- Softmax Probabilities Card -->
          <div class="panel-card" style="flex: 1;">
            <div class="panel-header">
              <span class="panel-title">
                <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M18 20V10M12 20V4M6 20v-6"/></svg>
                Softmax Probabilities
              </span>
              <span id="current-prediction-tag" style="font-size:0.72rem; font-family:var(--font-mono); font-weight:700; color:var(--cyan);">Pred: ?</span>
            </div>
            <div class="panel-body" style="padding: 6px 10px;">
              <div class="prob-bars-list" id="softmax-bars-container"></div>
            </div>
          </div>

        </div>

        <!-- Center Column: Full-Height Neural Network Canvas -->
        <div class="center-canvas-panel">
          <div class="canvas-hud-header">
            <span class="panel-title">
              <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="6" cy="6" r="3"/><circle cx="6" cy="18" r="3"/><circle cx="18" cy="12" r="3"/><path d="m8.5 7.5 7 3.5M8.5 16.5l7-3.5"/></svg>
              64 → 32 → 10 Network Architecture
            </span>
            <div class="canvas-legend-row">
              <div class="legend-item"><span class="legend-dot" style="background:var(--cyan)"></span><span>+W</span></div>
              <div class="legend-item"><span class="legend-dot" style="background:var(--magenta)"></span><span>-W</span></div>
              <div class="legend-item"><span class="legend-dot" style="background:#10b981"></span><span>Pulse</span></div>
            </div>
          </div>

          <div class="network-canvas-wrapper" id="canvas-container-box">
            <canvas id="network-canvas"></canvas>
            <div id="node-hud-tooltip" class="hud-tooltip"></div>
          </div>

          <div class="canvas-hud-bottom">
            <div class="wave-control-group">
              <button class="btn btn-sm btn-primary" id="btn-trigger-wave">🌊 Send Wave (3s)</button>
              <div style="display:flex; gap:3px;">
                <button class="btn btn-sm" id="btn-mode-forward-tab" style="background:rgba(0,242,254,0.12); color:var(--cyan); border-color:var(--cyan);">✨ Forward</button>
                <button class="btn btn-sm" id="btn-mode-backprop-tab">🔥 Backprop</button>
              </div>
            </div>

            <!-- Pulse Speed Slider -->
            <div style="display:flex; align-items:center; gap:8px;">
              <span style="font-size:0.7rem; font-family:var(--font-mono); color:var(--text-muted);">Pulse Speed:</span>
              <input type="range" id="slider-wave-speed" min="0.25" max="2.0" step="0.05" value="1.0" style="width:75px;">
              <strong id="label-wave-speed" style="font-size:0.7rem; font-family:var(--font-mono); color:var(--cyan);">1.0x</strong>
            </div>
          </div>
        </div>

        <!-- Right Column: Training Dashboard & Chart -->
        <div style="display: flex; flex-direction: column; gap: 8px; height: 100%;">
          
          <div class="panel-card" style="flex: 1.2;">
            <div class="panel-header">
              <span class="panel-title">
                <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M12 2v4M12 18v4M4.93 4.93l2.83 2.83M16.24 16.24l2.83 2.83M2 12h4M18 12h4M4.93 19.07l2.83-2.83M16.24 7.76l2.83-2.83"/></svg>
                Training Dashboard
              </span>
              <span id="training-status-pill" style="font-size:0.68rem; font-family:var(--font-mono); padding:2px 6px; border-radius:4px; border:1px solid var(--border-subtle); color:var(--text-muted);">Ready</span>
            </div>

            <div class="panel-body">
              <!-- Metrics Grid -->
              <div class="metric-grid-2">
                <div class="metric-card">
                  <div class="metric-card-label">Accuracy</div>
                  <div class="metric-card-num" id="metric-accuracy-val">9.8%</div>
                </div>
                <div class="metric-card">
                  <div class="metric-card-label">Loss (CE)</div>
                  <div class="metric-card-num loss" id="metric-loss-val">2.39</div>
                </div>
              </div>

              <!-- Step Progress -->
              <div>
                <div style="display:flex; justify-content:space-between; font-size:0.7rem; font-family:var(--font-mono); color:var(--text-muted);">
                  <span>Step: <strong id="metric-step-text" style="color:var(--text-main)">0/300</strong></span>
                  <span>Target: <strong>300</strong></span>
                </div>
                <div class="progress-bar-wrapper">
                  <div class="progress-bar-fill" id="training-progress-fill"></div>
                </div>
              </div>

              <!-- Action Buttons -->
              <div style="display:grid; grid-template-columns: 1fr 1fr; gap:6px;">
                <button class="btn btn-primary" id="btn-toggle-train">
                  <span id="train-btn-icon">▶</span>
                  <span id="train-btn-label">Train</span>
                </button>
                <button class="btn" id="btn-step-train">⏭ Step 1x</button>
              </div>

              <div style="display:grid; grid-template-columns: 1fr 1fr; gap:6px;">
                <button class="btn btn-accent" id="btn-instant-train">⚡ Auto 300</button>
                <button class="btn" id="btn-reset-train">↺ Reset</button>
              </div>

              <!-- Speed & LR Sliders -->
              <div class="control-row">
                <div class="control-label">
                  <span>Training Speed:</span>
                  <strong id="speed-label">25 steps/s</strong>
                </div>
                <input type="range" id="slider-speed" min="1" max="100" value="25">
              </div>

              <div class="control-row">
                <div class="control-label">
                  <span>Learning Rate (&eta;):</span>
                  <strong id="lr-label">0.65</strong>
                </div>
                <input type="range" id="slider-lr" min="0.05" max="1.5" step="0.05" value="0.65">
              </div>
            </div>
          </div>

          <!-- Live Chart Card -->
          <div class="panel-card" style="flex: 1;">
            <div class="panel-header">
              <span class="panel-title">
                <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M3 3v18h18"/><path d="m19 9-5 5-4-4-3 3"/></svg>
                Learning Curve (Acc & Loss)
              </span>
              <div style="display:flex; gap:6px; font-size:0.65rem; font-family:var(--font-mono);">
                <span style="color:var(--cyan)">Acc</span>
                <span style="color:var(--magenta)">Loss</span>
              </div>
            </div>
            <div class="panel-body" style="padding: 6px 8px;">
              <div class="chart-container">
                <canvas id="chart-canvas"></canvas>
              </div>
            </div>
          </div>

        </div>

      </div>
    </div>

    <!-- ==================== TAB 2: DRAW & TEST ==================== -->
    <div class="tab-page" id="tab-draw">
      <div class="draw-tab-content">
        <div class="panel-card" style="padding: 20px;">
          <div class="panel-header" style="background:transparent; border:none; padding:0 0 12px;">
            <div>
              <h2 style="font-size: 1.25rem; font-weight: 700;">✍️ Interactive Handwritten Digit Drawing Pad</h2>
              <p style="font-size: 0.85rem; color: var(--text-muted);">Draw any digit (0-9) inside the pad with your mouse or finger. Runs instant client-side neural inference.</p>
            </div>
          </div>

          <div class="draw-layout-grid">
            <div style="display:flex; flex-direction:column; align-items:center; gap:12px;">
              <div style="display:flex; align-items:center; gap:14px; justify-content:center;">
                <canvas id="user-draw-canvas" class="draw-canvas" width="220" height="220"></canvas>
                <div style="font-size:1.4rem; color:var(--text-dim);">➔</div>
                <div style="display:flex; flex-direction:column; align-items:center; gap:6px;">
                  <div class="downscaled-grid" id="downscaled-preview-grid"></div>
                  <span style="font-size:0.7rem; font-family:var(--font-mono); color:var(--text-dim);">8×8 Normalized</span>
                </div>
              </div>

              <div style="display:flex; gap:8px;">
                <button class="btn btn-sm" id="btn-clear-draw">🗑 Clear</button>
                <button class="btn btn-sm btn-primary" id="btn-send-draw-to-net">⚡ Feed to Studio</button>
              </div>

              <div style="display:flex; align-items:center; gap:6px;">
                <span style="font-size:0.75rem; font-family:var(--font-mono); color:var(--text-muted);">Presets:</span>
                <button class="btn btn-sm preset-draw-btn" data-digit="0">0</button>
                <button class="btn btn-sm preset-draw-btn" data-digit="1">1</button>
                <button class="btn btn-sm preset-draw-btn" data-digit="3">3</button>
                <button class="btn btn-sm preset-draw-btn" data-digit="4">4</button>
                <button class="btn btn-sm preset-draw-btn" data-digit="7">7</button>
                <button class="btn btn-sm preset-draw-btn" data-digit="8">8</button>
              </div>
            </div>

            <!-- Prediction Results -->
            <div style="display:flex; flex-direction:column; gap:12px;">
              <div style="display:flex; align-items:center; gap:14px; background:rgba(0,0,0,0.4); padding:12px 16px; border-radius:10px; border:1px solid var(--border-subtle);">
                <div class="big-digit-badge" id="draw-predicted-badge">?</div>
                <div>
                  <div style="font-size:0.75rem; font-family:var(--font-mono); color:var(--text-muted); text-transform:uppercase;">Predicted Digit</div>
                  <div style="font-size:1.1rem; font-weight:700; color:var(--text-main);" id="draw-confidence-text">Confidence: 0.0%</div>
                </div>
              </div>

              <div class="prob-bars-list" id="draw-softmax-bars-container"></div>
            </div>
          </div>
        </div>
      </div>
    </div>

    <!-- ==================== TAB 3: HOW IT WORKS ==================== -->
    <div class="tab-page" id="tab-math">
      <div class="math-tab-content">
        <div style="text-align:center; margin-bottom:16px;">
          <h2 style="font-size:1.4rem; font-weight:800; margin-bottom:4px;">How the Mathematics Work</h2>
          <p style="font-size:0.88rem; color:var(--text-muted);">Step-by-step mathematical formulation implemented in pure JavaScript.</p>
        </div>

        <div class="math-cards-grid">
          <div class="math-card">
            <div class="card-step-badge">1</div>
            <h3 style="font-size:1rem; font-weight:700; margin-bottom:6px;">Forward Pass (Linear Dot Product)</h3>
            <p style="font-size:0.82rem; color:var(--text-muted);">64 input pixels multiply the weight matrix and add biases to form 32 hidden logits.</p>
            <div class="math-formula-box">
              Z⁽¹⁾ = X · W⁽¹⁾ + b⁽¹⁾<br>
              <span style="color:var(--text-dim)">[1×64] · [64×32] + [1×32] = [1×32]</span>
            </div>
          </div>

          <div class="math-card">
            <div class="card-step-badge">2</div>
            <h3 style="font-size:1rem; font-weight:700; margin-bottom:6px;">Non-Linear Activation (ReLU)</h3>
            <p style="font-size:0.82rem; color:var(--text-muted);">Rectified Linear Unit keeps positive values and zeroes out negative signals, introducing non-linearity.</p>
            <div class="math-formula-box">
              A⁽¹⁾ = max(0, Z⁽¹⁾)<br>
              <span style="color:var(--text-dim)">dA/dZ = 1 if Z > 0 else 0</span>
            </div>
          </div>

          <div class="math-card">
            <div class="card-step-badge">3</div>
            <h3 style="font-size:1rem; font-weight:700; margin-bottom:6px;">Softmax & Cross-Entropy Loss</h3>
            <p style="font-size:0.82rem; color:var(--text-muted);">Softmax normalizes 10 output logits into probabilities summing to 1.0.</p>
            <div class="math-formula-box">
              P(y = k) = exp(Z_k⁽²⁾) / ∑ exp(Z_j⁽²⁾)<br>
              ℒ = -∑ Y_k · ln(P_k)
            </div>
          </div>

          <div class="math-card">
            <div class="card-step-badge">4</div>
            <h3 style="font-size:1rem; font-weight:700; margin-bottom:6px;">Backpropagation & Gradient Step</h3>
            <p style="font-size:0.82rem; color:var(--text-muted);">Error gradients flow backward through the layers via chain rule to update weights.</p>
            <div class="math-formula-box">
              δ⁽²⁾ = P - Y<br>
              δ⁽¹⁾ = (δ⁽²⁾ · (W⁽²⁾)ᵀ) ⊙ (Z⁽¹⁾ > 0)<br>
              W ← W - η · (Inputᵀ · δ)
            </div>
          </div>
        </div>
      </div>
    </div>

  </div>

  <!-- Embedded Dataset & Optimized Engine -->
  <script>
    // --- 1. EMBEDDED DATASET (350 balanced 8x8 digits) ---
    {dataset_code}

    const DATASET = RAW_DIGITS_DATA.map((str, idx) => {{
      const label = parseInt(str[0], 10);
      const hex = str.slice(2);
      const pixels = new Float32Array(64);
      for (let i = 0; i < 64; i++) {{
        pixels[i] = parseInt(hex[i], 16) / 15.0;
      }}
      return {{ id: idx, label, pixels, hex }};
    }});

    // --- 2. HIGH PERFORMANCE NEURAL NETWORK CLASS ---
    class ScratchNeuralNetwork {{
      constructor(inputSize = 64, hiddenSize = 32, outputSize = 10) {{
        this.inputSize = inputSize;
        this.hiddenSize = hiddenSize;
        this.outputSize = outputSize;
        this.reset();
      }}

      reset() {{
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
        this.b1.fill(0);
        this.b2.fill(0);
      }}

      forward(x) {{
        const z1 = new Float32Array(this.hiddenSize);
        const a1 = new Float32Array(this.hiddenSize);
        for (let j = 0; j < this.hiddenSize; j++) {{
          let sum = this.b1[j];
          for (let i = 0; i < this.inputSize; i++) {{
            sum += x[i] * this.W1[i * this.hiddenSize + j];
          }}
          z1[j] = sum;
          a1[j] = sum > 0 ? sum : 0;
        }}

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

        const probs = new Float32Array(this.outputSize);
        let sumExp = 0;
        for (let k = 0; k < this.outputSize; k++) {{
          const e = Math.exp(z2[k] - maxZ);
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
          if (pred === s.label) correct++;
          totalLoss += -Math.log(Math.max(probs[s.label], 1e-15));
        }}
        return {{ accuracy: correct / dataset.length, loss: totalLoss / dataset.length, step: this.step }};
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

          let pred = 0, maxP = -1;
          for (let k = 0; k < 10; k++) {{
            if (probs[k] > maxP) {{ maxP = probs[k]; pred = k; }}
          }}
          if (pred === label) correct++;
          totalLoss += -Math.log(Math.max(probs[label], 1e-15));

          const dz2 = new Float32Array(10);
          for (let k = 0; k < 10; k++) {{
            dz2[k] = probs[k] - (k === label ? 1.0 : 0.0);
          }}

          for (let j = 0; j < this.hiddenSize; j++) {{
            const aj = a1[j];
            if (aj === 0) continue;
            const rowOffset = j * this.outputSize;
            for (let k = 0; k < 10; k++) dW2[rowOffset + k] += aj * dz2[k];
          }}
          for (let k = 0; k < 10; k++) db2[k] += dz2[k];

          const dz1 = new Float32Array(this.hiddenSize);
          for (let j = 0; j < this.hiddenSize; j++) {{
            if (z1[j] <= 0) continue;
            let sum = 0;
            const rowOffset = j * this.outputSize;
            for (let k = 0; k < 10; k++) sum += dz2[k] * this.W2[rowOffset + k];
            dz1[j] = sum;
          }}

          for (let i = 0; i < this.inputSize; i++) {{
            const xi = pixels[i];
            if (xi === 0) continue;
            const rowOffset = i * this.hiddenSize;
            for (let j = 0; j < this.hiddenSize; j++) {{
              if (dz1[j] !== 0) dW1[rowOffset + j] += xi * dz1[j];
            }}
          }}
          for (let j = 0; j < this.hiddenSize; j++) db1[j] += dz1[j];
        }}

        const factor = lr / N;
        for (let i = 0; i < this.W1.length; i++) this.W1[i] -= factor * dW1[i];
        for (let j = 0; j < this.b1.length; j++) this.b1[j] -= factor * db1[j];
        for (let i = 0; i < this.W2.length; i++) this.W2[i] -= factor * dW2[i];
        for (let k = 0; k < this.b2.length; k++) this.b2[k] -= factor * db2[k];

        this.step++;
        const avgLoss = totalLoss / N;
        const accuracy = correct / N;
        this.history.push({{ step: this.step, loss: avgLoss, accuracy }});
        return {{ step: this.step, loss: avgLoss, accuracy }};
      }}
    }}

    // --- 3. APP STATE & GLOBAL CONSTANTS ---
    const nn = new ScratchNeuralNetwork(64, 32, 10);
    let currentSampleIndex = 0;
    let isTraining = false;
    let trainingAccumulator = 0;
    let targetAccDisplay = 0.098;
    let currentAccDisplay = 0.098;
    let targetLossDisplay = 2.39;
    let currentLossDisplay = 2.39;

    // Smooth Wave Animation State (Duration ~3s, Easing interpolation)
    let waveMode = 'forward'; // 'forward' | 'backprop'
    let waveProgress = 1.0; // 0.0 to 1.0
    let waveDuration = 3.0; // seconds
    let waveActive = false;
    let nodeGlowLevels = {{
      input: new Float32Array(64),
      hidden: new Float32Array(32),
      output: new Float32Array(10)
    }};

    // Offscreen Canvas Cache for 240Hz Rendering
    let offscreenSynapsesCanvas = document.createElement('canvas');
    let offscreenSynapsesCtx = offscreenSynapsesCanvas.getContext('2d');
    let needsSynapsesCacheUpdate = true;

    // Glow Sprites
    const glowSprites = {{}};
    function createGlowSprite(colorHex) {{
      const c = document.createElement('canvas');
      c.width = 32;
      c.height = 32;
      const ctx = c.getContext('2d');
      const grad = ctx.createRadialGradient(16, 16, 0, 16, 16, 16);
      grad.addColorStop(0, colorHex);
      grad.addColorStop(0.4, colorHex + '88');
      grad.addColorStop(1, 'transparent');
      ctx.fillStyle = grad;
      ctx.fillRect(0, 0, 32, 32);
      return c;
    }}
    glowSprites.cyan = createGlowSprite('#00f2fe');
    glowSprites.magenta = createGlowSprite('#ff007f');
    glowSprites.emerald = createGlowSprite('#10b981');
    glowSprites.purple = createGlowSprite('#8b5cf6');

    // Smooth Easing: Cubic In-Out
    function easeInOutCubic(x) {{
      return x < 0.5 ? 4 * x * x * x : 1 - Math.pow(-2 * x + 2, 3) / 2;
    }}

    // --- 4. 8x8 PIXEL GRID DOM SETUP ---
    function setupPixelGrid() {{
      const container = document.getElementById('pixel-grid-container');
      container.innerHTML = '';
      for (let i = 0; i < 64; i++) {{
        const cell = document.createElement('div');
        cell.className = 'pixel-cell';
        cell.dataset.index = i;
        cell.addEventListener('mouseenter', () => updateNodeTooltip(i, 'input'));
        cell.addEventListener('mouseleave', hideNodeTooltip);
        container.appendChild(cell);
      }}

      const filterContainer = document.getElementById('digit-filter-container');
      filterContainer.innerHTML = '';
      for (let d = 0; d < 10; d++) {{
        const btn = document.createElement('button');
        btn.className = 'digit-pill-btn';
        btn.textContent = d;
        btn.addEventListener('click', () => {{
          const idx = DATASET.findIndex(s => s.label === d);
          if (idx !== -1) {{
            currentSampleIndex = idx;
            renderCurrentSample();
            startWaveAnimation('forward');
          }}
        }});
        filterContainer.appendChild(btn);
      }}
    }}

    function renderCurrentSample() {{
      const sample = DATASET[currentSampleIndex];
      const cells = document.querySelectorAll('.pixel-cell');

      sample.pixels.forEach((val, i) => {{
        if (val > 0.05) {{
          cells[i].style.backgroundColor = `rgb(${{Math.round(val * 0)}}, ${{Math.round(val * 242)}}, ${{Math.round(val * 254)}})`;
          cells[i].style.boxShadow = `0 0 ${{val * 4}}px rgba(0, 242, 254, ${{val * 0.6}})`;
        }} else {{
          cells[i].style.backgroundColor = '#030509';
          cells[i].style.boxShadow = 'none';
        }}
      }});

      document.getElementById('current-label-badge').textContent = `Target: ${{sample.label}}`;
      document.getElementById('sample-index-text').textContent = `#${{currentSampleIndex + 1}}/350`;
      document.getElementById('sample-target-text').textContent = `${{sample.label}}`;

      document.querySelectorAll('.digit-pill-btn').forEach((btn, idx) => {{
        btn.classList.toggle('active', idx === sample.label);
      }});

      const forwardRes = nn.forward(sample.pixels);
      updateSoftmaxBars('softmax-bars-container', forwardRes.probs, sample.label);

      let winner = 0, maxP = -1;
      for (let k = 0; k < 10; k++) {{
        if (forwardRes.probs[k] > maxP) {{ maxP = forwardRes.probs[k]; winner = k; }}
      }}
      const predTag = document.getElementById('current-prediction-tag');
      predTag.textContent = `Pred: ${{winner}} (${{(maxP * 100).toFixed(0)}}%)`;
      predTag.style.color = winner === sample.label ? '#10b981' : '#f59e0b';
    }}

    function updateSoftmaxBars(containerId, probs, targetLabel = null) {{
      const container = document.getElementById(containerId);
      container.innerHTML = '';
      let maxP = -1, maxIdx = 0;
      for (let k = 0; k < 10; k++) {{
        if (probs[k] > maxP) {{ maxP = probs[k]; maxIdx = k; }}
      }}

      for (let k = 0; k < 10; k++) {{
        const isWinner = (k === maxIdx);
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

    // --- 5. NETWORK CANVAS WITH RESIZEOBSERVER & DPR ---
    let netCanvas, netCtx;
    let hoveredNode = null;
    const nodePositions = {{ input: [], hidden: [], output: [] }};

    function initNetworkCanvas() {{
      netCanvas = document.getElementById('network-canvas');
      netCtx = netCanvas.getContext('2d');
      const wrapper = document.getElementById('canvas-container-box');

      const ro = new ResizeObserver(entries => {{
        for (let entry of entries) {{
          const w = entry.contentRect.width;
          const h = entry.contentRect.height;
          if (w <= 0 || h <= 0) continue;
          const dpr = Math.min(window.devicePixelRatio || 1, 2);
          netCanvas.width = w * dpr;
          netCanvas.height = h * dpr;
          netCtx.resetTransform();
          netCtx.scale(dpr, dpr);

          offscreenSynapsesCanvas.width = w * dpr;
          offscreenSynapsesCanvas.height = h * dpr;
          offscreenSynapsesCtx.resetTransform();
          offscreenSynapsesCtx.scale(dpr, dpr);

          calculateNodePositions(w, h);
          needsSynapsesCacheUpdate = true;
          renderTrainingChart();
        }}
      }});
      ro.observe(wrapper);

      netCanvas.addEventListener('mousemove', (e) => {{
        const rect = netCanvas.getBoundingClientRect();
        const mouseX = e.clientX - rect.left;
        const mouseY = e.clientY - rect.top;

        let found = null;
        for (let i = 0; i < nodePositions.input.length; i++) {{
          const p = nodePositions.input[i];
          if (Math.hypot(mouseX - p.x, mouseY - p.y) < 7) {{ found = {{ layer: 'input', index: i }}; break; }}
        }}
        if (!found) {{
          for (let j = 0; j < nodePositions.hidden.length; j++) {{
            const p = nodePositions.hidden[j];
            if (Math.hypot(mouseX - p.x, mouseY - p.y) < 8) {{ found = {{ layer: 'hidden', index: j }}; break; }}
          }}
        }}
        if (!found) {{
          for (let k = 0; k < nodePositions.output.length; k++) {{
            const p = nodePositions.output[k];
            if (Math.hypot(mouseX - p.x, mouseY - p.y) < 11) {{ found = {{ layer: 'output', index: k }}; break; }}
          }}
        }}

        hoveredNode = found;
        if (found) updateNodeTooltip(found.index, found.layer, mouseX + 15, mouseY + 15);
        else hideNodeTooltip();
      }});

      netCanvas.addEventListener('mouseleave', () => {{
        hoveredNode = null;
        hideNodeTooltip();
      }});
    }}

    function calculateNodePositions(width, height) {{
      nodePositions.input = [];
      nodePositions.hidden = [];
      nodePositions.output = [];

      // 64 inputs in 2 columns of 32
      const inX = Math.max(30, width * 0.10);
      const inSpacingY = (height - 36) / 32;
      for (let i = 0; i < 64; i++) {{
        const col = Math.floor(i / 32);
        const row = i % 32;
        nodePositions.input.push({{
          x: inX + col * 16,
          y: 18 + row * inSpacingY,
          radius: 3.2
        }});
      }}

      // 32 hidden neurons in 1 column
      const hidX = width * 0.50;
      const hidSpacingY = (height - 36) / 32;
      for (let j = 0; j < 32; j++) {{
        nodePositions.hidden.push({{
          x: hidX,
          y: 18 + j * hidSpacingY,
          radius: 4.5
        }});
      }}

      // 10 outputs in 1 column
      const outX = Math.min(width - 50, width * 0.88);
      const outSpacingY = (height - 60) / 9;
      for (let k = 0; k < 10; k++) {{
        nodePositions.output.push({{
          x: outX,
          y: 30 + k * outSpacingY,
          radius: 7.5,
          label: k
        }});
      }}
    }}

    function updateNodeTooltip(index, layer, x = 20, y = 20) {{
      const tooltip = document.getElementById('node-hud-tooltip');
      const sample = DATASET[currentSampleIndex];
      const forwardRes = nn.forward(sample.pixels);
      let content = '';

      if (layer === 'input') {{
        content = `<strong>x_${{index}}</strong> | Pix: <code>${{sample.pixels[index].toFixed(2)}}</code>`;
      }} else if (layer === 'hidden') {{
        content = `<strong>h_${{index}}</strong> | z: <code>${{forwardRes.z1[index].toFixed(2)}}</code> | ReLU a: <code>${{forwardRes.a1[index].toFixed(2)}}</code>`;
      }} else if (layer === 'output') {{
        const isTarget = (sample.label === index);
        content = `<strong>Output [${{index}}]</strong> | Prob: <code>${{(forwardRes.probs[index] * 100).toFixed(1)}}%</code>${{isTarget ? ' ★' : ''}}`;
      }}

      tooltip.innerHTML = content;
      tooltip.style.display = 'block';
      tooltip.style.left = `${{Math.min(x, 220)}}px`;
      tooltip.style.top = `${{Math.min(y, 240)}}px`;
    }}

    function hideNodeTooltip() {{
      document.getElementById('node-hud-tooltip').style.display = 'none';
    }}

    // Update Offscreen Synapse Cache (Fast Baseline Rendering)
    function updateOffscreenSynapses() {{
      if (!offscreenSynapsesCtx) return;
      const w = offscreenSynapsesCanvas.width;
      const h = offscreenSynapsesCanvas.height;
      const dpr = Math.min(window.devicePixelRatio || 1, 2);
      offscreenSynapsesCtx.clearRect(0, 0, w / dpr, h / dpr);

      // Draw W2
      for (let j = 0; j < 32; j++) {{
        const hp = nodePositions.hidden[j];
        if (!hp) continue;
        for (let k = 0; k < 10; k++) {{
          const op = nodePositions.output[k];
          if (!op) continue;
          const weight = nn.W2[j * 10 + k];
          const alpha = Math.min(Math.abs(weight) * 0.45, 0.45);
          offscreenSynapsesCtx.beginPath();
          offscreenSynapsesCtx.moveTo(hp.x, hp.y);
          offscreenSynapsesCtx.lineTo(op.x, op.y);
          offscreenSynapsesCtx.strokeStyle = weight > 0 ? `rgba(0, 242, 254, ${{alpha}})` : `rgba(255, 0, 127, ${{alpha}})`;
          offscreenSynapsesCtx.lineWidth = 0.8;
          offscreenSynapsesCtx.stroke();
        }}
      }}

      // Draw W1 (dim non-active)
      for (let i = 0; i < 64; i++) {{
        const ip = nodePositions.input[i];
        if (!ip) continue;
        for (let j = 0; j < 32; j++) {{
          const hp = nodePositions.hidden[j];
          if (!hp) continue;
          const weight = nn.W1[i * 32 + j];
          const alpha = Math.min(Math.abs(weight) * 0.25, 0.25);
          offscreenSynapsesCtx.beginPath();
          offscreenSynapsesCtx.moveTo(ip.x, ip.y);
          offscreenSynapsesCtx.lineTo(hp.x, hp.y);
          offscreenSynapsesCtx.strokeStyle = weight > 0 ? `rgba(0, 242, 254, ${{alpha}})` : `rgba(255, 0, 127, ${{alpha}})`;
          offscreenSynapsesCtx.lineWidth = 0.6;
          offscreenSynapsesCtx.stroke();
        }}
      }}
      needsSynapsesCacheUpdate = false;
    }}

    // Trigger Slow Smooth Wave (3 seconds, customizable)
    function startWaveAnimation(mode = 'forward') {{
      waveMode = mode;
      waveProgress = 0.0;
      waveActive = true;
    }}

    // --- 6. 240Hz MAIN RENDER LOOP WITH DELTA TIME ---
    let lastTimestamp = performance.now();
    let frameCount = 0;
    let fpsTimer = 0;

    function renderAppFrame(now) {{
      const dt = Math.min((now - lastTimestamp) / 1000, 0.1); // clamp delta
      lastTimestamp = now;

      // Calculate Real FPS
      frameCount++;
      fpsTimer += dt;
      if (fpsTimer >= 0.5) {{
        const currentFps = Math.round(frameCount / fpsTimer);
        document.getElementById('fps-counter-val').textContent = `${{currentFps}} FPS`;
        frameCount = 0;
        fpsTimer = 0;
      }}

      // Smooth Number Interpolation (Count-up tweening)
      currentAccDisplay += (targetAccDisplay - currentAccDisplay) * Math.min(dt * 12, 1);
      currentLossDisplay += (targetLossDisplay - currentLossDisplay) * Math.min(dt * 12, 1);
      document.getElementById('metric-accuracy-val').textContent = `${{(currentAccDisplay * 100).toFixed(1)}}%`;
      document.getElementById('metric-loss-val').textContent = currentLossDisplay.toFixed(2);

      // Advance Wave Animation
      if (waveActive) {{
        const speedMultiplier = parseFloat(document.getElementById('slider-wave-speed').value) || 1.0;
        const speed = (1.0 / waveDuration) * speedMultiplier;
        waveProgress += dt * speed;
        if (waveProgress >= 1.0) {{
          waveProgress = 1.0;
          waveActive = false;
        }}
      }}

      // Render Network Canvas
      if (netCanvas && netCtx && nodePositions.output.length > 0) {{
        const width = netCanvas.clientWidth;
        const height = netCanvas.clientHeight;
        netCtx.clearRect(0, 0, width, height);

        if (needsSynapsesCacheUpdate) {{
          updateOffscreenSynapses();
        }}

        // Draw offscreen static cache
        const dpr = Math.min(window.devicePixelRatio || 1, 2);
        netCtx.drawImage(offscreenSynapsesCanvas, 0, 0, width, height);

        const sample = DATASET[currentSampleIndex];
        const forwardRes = nn.forward(sample.pixels);

        const easedP = easeInOutCubic(waveProgress);

        // Calculate Wave Phase Activation
        // Forward: 0.0-0.3 (Input -> Hidden), 0.3-0.7 (Hidden), 0.7-1.0 (Output)
        // Backprop: 0.0-0.3 (Output -> Hidden), 0.3-0.7 (Hidden), 0.7-1.0 (Input)
        let waveX = 0;
        if (waveMode === 'forward') {{
          const inX = nodePositions.input[0].x;
          const outX = nodePositions.output[0].x;
          waveX = inX + (outX - inX) * easedP;
        }} else {{
          const inX = nodePositions.input[0].x;
          const outX = nodePositions.output[0].x;
          waveX = outX - (outX - inX) * easedP;
        }}

        // Dynamic Glow Connections (Top Active Synapses with Additive Blending)
        netCtx.save();
        netCtx.globalCompositeOperation = 'lighter';

        // Draw Glowing Synapse Pulses
        if (waveActive) {{
          if (waveMode === 'forward') {{
            // Input to Hidden Synapse Wave
            if (easedP > 0.05 && easedP < 0.65) {{
              const pRatio = Math.min(1, Math.max(0, (easedP - 0.05) / 0.55));
              for (let i = 0; i < 64; i += 2) {{
                if (sample.pixels[i] < 0.15) continue;
                const ip = nodePositions.input[i];
                for (let j = 0; j < 32; j += 3) {{
                  const hp = nodePositions.hidden[j];
                  const pulseX = ip.x + (hp.x - ip.x) * pRatio;
                  const pulseY = ip.y + (hp.y - ip.y) * pRatio;

                  netCtx.beginPath();
                  netCtx.arc(pulseX, pulseY, 2.2, 0, Math.PI * 2);
                  netCtx.fillStyle = '#00f2fe';
                  netCtx.fill();
                }}
              }}
            }}
            // Hidden to Output Synapse Wave
            if (easedP > 0.45 && easedP < 1.0) {{
              const pRatio = Math.min(1, Math.max(0, (easedP - 0.45) / 0.5));
              for (let j = 0; j < 32; j += 2) {{
                const hp = nodePositions.hidden[j];
                if (forwardRes.a1[j] <= 0) continue;
                for (let k = 0; k < 10; k++) {{
                  const op = nodePositions.output[k];
                  const pulseX = hp.x + (op.x - hp.x) * pRatio;
                  const pulseY = hp.y + (op.y - hp.y) * pRatio;

                  netCtx.beginPath();
                  netCtx.arc(pulseX, pulseY, 2.5, 0, Math.PI * 2);
                  netCtx.fillStyle = '#10b981';
                  netCtx.fill();
                }}
              }}
            }}
          }} else {{
            // Backprop Wave (Red / Magenta)
            if (easedP > 0.05 && easedP < 0.65) {{
              const pRatio = Math.min(1, Math.max(0, (easedP - 0.05) / 0.55));
              for (let k = 0; k < 10; k++) {{
                const op = nodePositions.output[k];
                for (let j = 0; j < 32; j += 3) {{
                  const hp = nodePositions.hidden[j];
                  const pulseX = op.x - (op.x - hp.x) * pRatio;
                  const pulseY = op.y - (op.y - hp.y) * pRatio;

                  netCtx.beginPath();
                  netCtx.arc(pulseX, pulseY, 2.5, 0, Math.PI * 2);
                  netCtx.fillStyle = '#ff007f';
                  netCtx.fill();
                }}
              }}
            }}
          }}
        }}

        // Highlight Hovered Node Connections
        if (hoveredNode) {{
          if (hoveredNode.layer === 'hidden') {{
            const j = hoveredNode.index;
            const hp = nodePositions.hidden[j];
            for (let i = 0; i < 64; i++) {{
              const ip = nodePositions.input[i];
              const w = nn.W1[i * 32 + j];
              netCtx.beginPath();
              netCtx.moveTo(ip.x, ip.y);
              netCtx.lineTo(hp.x, hp.y);
              netCtx.strokeStyle = w > 0 ? 'rgba(0, 242, 254, 0.9)' : 'rgba(255, 0, 127, 0.9)';
              netCtx.lineWidth = 1.8;
              netCtx.stroke();
            }}
          }}
        }}

        netCtx.restore();

        // Draw Nodes
        // Input Nodes
        for (let i = 0; i < 64; i++) {{
          const p = nodePositions.input[i];
          const val = sample.pixels[i];
          const isHov = hoveredNode && hoveredNode.layer === 'input' && hoveredNode.index === i;
          const distWave = Math.abs(p.x - waveX);
          const waveGlow = waveActive && distWave < 45 ? (1 - distWave / 45) : 0;

          netCtx.beginPath();
          netCtx.arc(p.x, p.y, isHov ? p.radius + 2 : p.radius, 0, Math.PI * 2);
          netCtx.fillStyle = `rgba(0, 242, 254, ${{Math.max(val, 0.15) + waveGlow * 0.6}})`;
          netCtx.fill();

          if (val > 0.25 || isHov || waveGlow > 0.3) {{
            netCtx.strokeStyle = isHov ? '#ffffff' : 'rgba(0, 242, 254, 0.9)';
            netCtx.lineWidth = 1;
            netCtx.stroke();
          }}
        }}

        // Hidden Nodes
        for (let j = 0; j < 32; j++) {{
          const p = nodePositions.hidden[j];
          const aVal = forwardRes.a1[j];
          const normA = Math.min(aVal, 2.5) / 2.5;
          const isHov = hoveredNode && hoveredNode.layer === 'hidden' && hoveredNode.index === j;
          const distWave = Math.abs(p.x - waveX);
          const waveGlow = waveActive && distWave < 55 ? (1 - distWave / 55) : 0;

          netCtx.beginPath();
          netCtx.arc(p.x, p.y, isHov ? p.radius + 2.5 : p.radius, 0, Math.PI * 2);
          netCtx.fillStyle = aVal > 0 ? `rgba(139, 92, 246, ${{Math.max(normA, 0.2) + waveGlow * 0.7}})` : 'rgba(30, 41, 59, 0.5)';
          netCtx.fill();

          netCtx.strokeStyle = isHov ? '#00f2fe' : (aVal > 0 ? 'rgba(139, 92, 246, 0.8)' : 'rgba(255, 255, 255, 0.15)');
          netCtx.lineWidth = isHov ? 2 : 1;
          netCtx.stroke();
        }}

        // Output Nodes
        let maxProb = -1, winningDigit = 0;
        for (let k = 0; k < 10; k++) {{
          if (forwardRes.probs[k] > maxProb) {{ maxProb = forwardRes.probs[k]; winningDigit = k; }}
        }}

        for (let k = 0; k < 10; k++) {{
          const p = nodePositions.output[k];
          const prob = forwardRes.probs[k];
          const isWinner = (k === winningDigit);
          const isTarget = (k === sample.label);
          const isHov = hoveredNode && hoveredNode.layer === 'output' && hoveredNode.index === k;
          const distWave = Math.abs(p.x - waveX);
          const waveGlow = waveActive && distWave < 60 ? (1 - distWave / 60) : 0;

          netCtx.beginPath();
          netCtx.arc(p.x, p.y, isHov ? p.radius + 3 : p.radius, 0, Math.PI * 2);
          netCtx.fillStyle = isWinner ? (isTarget ? '#10b981' : '#f59e0b') : `rgba(0, 242, 254, ${{Math.max(prob, 0.15) + waveGlow * 0.5}})`;
          netCtx.fill();

          if (isWinner || isTarget || isHov) {{
            netCtx.strokeStyle = isWinner ? (isTarget ? '#10b981' : '#f59e0b') : '#00f2fe';
            netCtx.lineWidth = isHov ? 2.5 : 1.8;
            netCtx.stroke();
          }}

          // Output Digit Label text
          netCtx.fillStyle = isWinner ? '#ffffff' : '#94a3b8';
          netCtx.font = `${{isWinner ? 'bold ' : ''}}10px 'JetBrains Mono', monospace`;
          netCtx.textAlign = 'left';
          netCtx.textBaseline = 'middle';
          netCtx.fillText(`[${{k}}] ${{(prob * 100).toFixed(0)}}%`, p.x + 12, p.y);
        }}
      }}

      requestAnimationFrame(renderAppFrame);
    }}

    // --- 7. TRAINING ENGINE (DECOUPLED FROM RENDER LOOP) ---
    let trainTimer = null;
    function startTrainingLoop() {{
      if (trainTimer) clearInterval(trainTimer);
      const speed = parseInt(document.getElementById('slider-speed').value, 10) || 25;
      const intervalMs = Math.max(10, Math.round(1000 / speed));

      trainTimer = setInterval(() => {{
        if (!isTraining) return;
        const lr = parseFloat(document.getElementById('slider-lr').value) || 0.65;
        const res = nn.trainStep(DATASET, lr);
        targetAccDisplay = res.accuracy;
        targetLossDisplay = res.loss;
        needsSynapsesCacheUpdate = true;

        document.getElementById('metric-step-text').textContent = `${{nn.step}}/300`;
        document.getElementById('training-progress-fill').style.width = `${{Math.min(100, (nn.step / 300) * 100)}}%`;

        if (nn.step % 5 === 0 || nn.step === 300) {{
          renderTrainingChart();
          renderCurrentSample();
        }}

        if (nn.step >= 300) {{
          toggleTraining(false);
          startWaveAnimation('forward');
        }}
      }}, intervalMs);
    }}

    function toggleTraining(forcedState = null) {{
      isTraining = (forcedState !== null) ? forcedState : !isTraining;
      const label = document.getElementById('train-btn-label');
      const icon = document.getElementById('train-btn-icon');
      const btn = document.getElementById('btn-toggle-train');
      const statusPill = document.getElementById('training-status-pill');

      if (isTraining) {{
        label.textContent = 'Pause';
        icon.textContent = '⏸';
        btn.classList.add('btn-accent');
        statusPill.textContent = 'Training...';
        statusPill.style.color = '#00f2fe';
        statusPill.style.borderColor = '#00f2fe';
        startTrainingLoop();
      }} else {{
        label.textContent = 'Train';
        icon.textContent = '▶';
        btn.classList.remove('btn-accent');
        statusPill.textContent = nn.step >= 300 ? 'Done' : 'Paused';
        statusPill.style.color = nn.step >= 300 ? '#10b981' : '#94a3b8';
        statusPill.style.borderColor = 'rgba(255, 255, 255, 0.08)';
        if (trainTimer) {{
          clearInterval(trainTimer);
          trainTimer = null;
        }}
      }}
    }}

    // --- 8. LIVE CHART RENDERING ---
    function renderTrainingChart() {{
      const canvas = document.getElementById('chart-canvas');
      if (!canvas) return;
      const ctx = canvas.getContext('2d');
      const dpr = Math.min(window.devicePixelRatio || 1, 2);
      const width = canvas.parentElement.clientWidth;
      const height = canvas.parentElement.clientHeight;
      if (width <= 0 || height <= 0) return;

      canvas.width = width * dpr;
      canvas.height = height * dpr;
      ctx.resetTransform();
      ctx.scale(dpr, dpr);
      ctx.clearRect(0, 0, width, height);

      const history = nn.history;
      if (history.length === 0) {{
        ctx.fillStyle = '#64748b';
        ctx.font = '10px "JetBrains Mono", monospace';
        ctx.textAlign = 'center';
        ctx.fillText('Click "Train" to record curve', width / 2, height / 2);
        return;
      }}

      const maxSteps = Math.max(300, history[history.length - 1].step);
      const padL = 24, padR = 14, padT = 10, padB = 18;
      const plotW = width - padL - padR;
      const plotH = height - padT - padB;

      // Grid
      ctx.strokeStyle = 'rgba(255, 255, 255, 0.05)';
      ctx.lineWidth = 1;
      for (let yPct = 0; yPct <= 1; yPct += 0.5) {{
        const y = padT + plotH * (1 - yPct);
        ctx.beginPath();
        ctx.moveTo(padL, y);
        ctx.lineTo(padL + plotW, y);
        ctx.stroke();
      }}

      // Acc Curve (Cyan)
      ctx.beginPath();
      for (let i = 0; i < history.length; i++) {{
        const h = history[i];
        const x = padL + (h.step / maxSteps) * plotW;
        const y = padT + plotH * (1 - h.accuracy);
        if (i === 0) ctx.moveTo(x, y);
        else ctx.lineTo(x, y);
      }}
      ctx.strokeStyle = '#00f2fe';
      ctx.lineWidth = 1.8;
      ctx.stroke();

      // Loss Curve (Magenta)
      const maxLoss = 2.5;
      ctx.beginPath();
      for (let i = 0; i < history.length; i++) {{
        const h = history[i];
        const normLoss = Math.min(h.loss, maxLoss) / maxLoss;
        const x = padL + (h.step / maxSteps) * plotW;
        const y = padT + plotH * normLoss;
        if (i === 0) ctx.moveTo(x, y);
        else ctx.lineTo(x, y);
      }}
      ctx.strokeStyle = '#ff007f';
      ctx.lineWidth = 1.6;
      ctx.stroke();

      ctx.fillStyle = '#64748b';
      ctx.font = '8px "JetBrains Mono", monospace';
      ctx.textAlign = 'left';
      ctx.fillText('0', padL, height - 4);
      ctx.textAlign = 'right';
      ctx.fillText(`${{maxSteps}}`, padL + plotW, height - 4);
    }}

    // --- 9. DRAW & TEST INTERACTIVE PAD ---
    let drawCanvas, drawCtx;
    let isDrawing = false;
    let drawDownscaledData = new Float32Array(64);

    function setupDrawingCanvas() {{
      drawCanvas = document.getElementById('user-draw-canvas');
      drawCtx = drawCanvas.getContext('2d');
      drawCtx.fillStyle = '#000';
      drawCtx.fillRect(0, 0, drawCanvas.width, drawCanvas.height);

      function start(e) {{ isDrawing = true; draw(e); }}
      function stop() {{
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

      drawCanvas.addEventListener('mousedown', start);
      drawCanvas.addEventListener('mousemove', draw);
      window.addEventListener('mouseup', stop);
      drawCanvas.addEventListener('touchstart', (e) => {{ e.preventDefault(); start(e); }});
      drawCanvas.addEventListener('touchmove', (e) => {{ e.preventDefault(); draw(e); }});
      window.addEventListener('touchend', stop);

      document.getElementById('btn-clear-draw').addEventListener('click', () => {{
        drawCtx.fillStyle = '#000';
        drawCtx.fillRect(0, 0, drawCanvas.width, drawCanvas.height);
        drawCtx.beginPath();
        drawDownscaledData.fill(0);
        updateDownscaledPreview();
        updateDrawPredictions();
      }});

      document.getElementById('btn-send-draw-to-net').addEventListener('click', () => {{
        DATASET[currentSampleIndex].pixels.set(drawDownscaledData);
        renderCurrentSample();
        switchTab('studio');
        startWaveAnimation('forward');
      }});

      document.querySelectorAll('.preset-draw-btn').forEach(btn => {{
        btn.addEventListener('click', () => {{
          const digit = parseInt(btn.dataset.digit, 10);
          loadPresetDrawing(digit);
        }});
      }});

      const previewGrid = document.getElementById('downscaled-preview-grid');
      previewGrid.innerHTML = '';
      for (let i = 0; i < 64; i++) {{
        const cell = document.createElement('div');
        cell.className = 'downscaled-cell';
        previewGrid.appendChild(cell);
      }}
    }}

    function processUserDrawing() {{
      const imgData = drawCtx.getImageData(0, 0, drawCanvas.width, drawCanvas.height);
      const data = imgData.data;
      const w = drawCanvas.width, h = drawCanvas.height;

      let minX = w, minY = h, maxX = 0, maxY = 0, hasInk = false;
      for (let y = 0; y < h; y++) {{
        for (let x = 0; x < w; x++) {{
          if (data[(y * w + x) * 4] > 30) {{
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

      const boxW = Math.max(1, maxX - minX + 1);
      const boxH = Math.max(1, maxY - minY + 1);
      const maxDim = Math.max(boxW, boxH);

      const off = document.createElement('canvas');
      off.width = 8;
      off.height = 8;
      const offCtx = off.getContext('2d');
      offCtx.fillStyle = '#000';
      offCtx.fillRect(0, 0, 8, 8);

      const scale = 6 / maxDim;
      const drawW = boxW * scale;
      const drawH = boxH * scale;
      offCtx.drawImage(drawCanvas, minX, minY, boxW, boxH, 1 + (6 - drawW)/2, 1 + (6 - drawH)/2, drawW, drawH);

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
        cells[i].style.backgroundColor = v > 0.05 ? `rgba(0, 242, 254, ${{v}})` : '#000';
      }}
    }}

    function updateDrawPredictions() {{
      const {{ probs }} = nn.forward(drawDownscaledData);
      let maxP = -1, winner = 0;
      for (let k = 0; k < 10; k++) {{
        if (probs[k] > maxP) {{ maxP = probs[k]; winner = k; }}
      }}
      document.getElementById('draw-predicted-badge').textContent = winner;
      document.getElementById('draw-confidence-text').textContent = `Confidence: ${{(maxP * 100).toFixed(1)}}%`;
      updateSoftmaxBars('draw-softmax-bars-container', probs);
    }}

    function loadPresetDrawing(digit) {{
      const sample = DATASET.find(s => s.label === digit);
      if (!sample) return;
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

    // --- 10. TAB NAVIGATION SYSTEM ---
    function switchTab(tabId) {{
      document.querySelectorAll('.tab-btn').forEach(b => {{
        b.classList.toggle('active', b.dataset.tab === tabId);
      }});
      document.querySelectorAll('.tab-page').forEach(p => {{
        p.classList.toggle('active', p.id === `tab-${{tabId}}`);
      }});
      if (tabId === 'studio') {{
        needsSynapsesCacheUpdate = true;
        renderTrainingChart();
      }}
    }}

    // --- 11. INITIALIZATION ---
    window.addEventListener('DOMContentLoaded', () => {{
      setupPixelGrid();
      initNetworkCanvas();
      setupDrawingCanvas();

      // Navigation tabs
      document.querySelectorAll('.tab-btn').forEach(btn => {{
        btn.addEventListener('click', () => switchTab(btn.dataset.tab));
      }});

      // Evaluate initial untrained state
      const initRes = nn.evaluate(DATASET);
      targetAccDisplay = initRes.accuracy;
      currentAccDisplay = initRes.accuracy;
      targetLossDisplay = initRes.loss;
      currentLossDisplay = initRes.loss;
      nn.history.push(initRes);
      renderCurrentSample();
      renderTrainingChart();

      // Sample Controls
      document.getElementById('btn-prev-sample').addEventListener('click', () => {{
        currentSampleIndex = (currentSampleIndex - 1 + DATASET.length) % DATASET.length;
        renderCurrentSample();
        startWaveAnimation('forward');
      }});

      document.getElementById('btn-next-sample').addEventListener('click', () => {{
        currentSampleIndex = (currentSampleIndex + 1) % DATASET.length;
        renderCurrentSample();
        startWaveAnimation('forward');
      }});

      document.getElementById('btn-random-sample').addEventListener('click', () => {{
        currentSampleIndex = Math.floor(Math.random() * DATASET.length);
        renderCurrentSample();
        startWaveAnimation('forward');
      }});

      // Wave Controls
      document.getElementById('btn-trigger-wave').addEventListener('click', () => {{
        startWaveAnimation(waveMode);
      }});

      const btnFwd = document.getElementById('btn-mode-forward-tab');
      const btnBwd = document.getElementById('btn-mode-backprop-tab');

      btnFwd.addEventListener('click', () => {{
        waveMode = 'forward';
        btnFwd.style.background = 'rgba(0,242,254,0.12)';
        btnFwd.style.color = 'var(--cyan)';
        btnFwd.style.borderColor = 'var(--cyan)';
        btnBwd.style.background = 'transparent';
        btnBwd.style.color = 'var(--text-muted)';
        btnBwd.style.borderColor = 'var(--border-subtle)';
        startWaveAnimation('forward');
      }});

      btnBwd.addEventListener('click', () => {{
        waveMode = 'backprop';
        btnBwd.style.background = 'rgba(255,0,127,0.15)';
        btnBwd.style.color = 'var(--magenta)';
        btnBwd.style.borderColor = 'var(--magenta)';
        btnFwd.style.background = 'transparent';
        btnFwd.style.color = 'var(--text-muted)';
        btnFwd.style.borderColor = 'var(--border-subtle)';
        startWaveAnimation('backprop');
      }});

      // Speed Slider
      const waveSpeedSlider = document.getElementById('slider-wave-speed');
      const waveSpeedLabel = document.getElementById('label-wave-speed');
      waveSpeedSlider.addEventListener('input', (e) => {{
        waveSpeedLabel.textContent = `${{parseFloat(e.target.value).toFixed(2)}}x`;
      }});

      // Dashboard Controls
      document.getElementById('btn-toggle-train').addEventListener('click', () => toggleTraining());
      document.getElementById('btn-step-train').addEventListener('click', () => {{
        const lr = parseFloat(document.getElementById('slider-lr').value) || 0.65;
        const res = nn.trainStep(DATASET, lr);
        targetAccDisplay = res.accuracy;
        targetLossDisplay = res.loss;
        needsSynapsesCacheUpdate = true;
        document.getElementById('metric-step-text').textContent = `${{nn.step}}/300`;
        document.getElementById('training-progress-fill').style.width = `${{Math.min(100, (nn.step / 300) * 100)}}%`;
        renderTrainingChart();
        renderCurrentSample();
        startWaveAnimation('forward');
      }});

      document.getElementById('btn-instant-train').addEventListener('click', () => {{
        toggleTraining(false);
        const lr = parseFloat(document.getElementById('slider-lr').value) || 0.65;
        while (nn.step < 300) {{
          nn.trainStep(DATASET, lr);
        }}
        const res = nn.evaluate(DATASET);
        targetAccDisplay = res.accuracy;
        targetLossDisplay = res.loss;
        needsSynapsesCacheUpdate = true;
        document.getElementById('metric-step-text').textContent = `300/300`;
        document.getElementById('training-progress-fill').style.width = '100%';
        renderTrainingChart();
        renderCurrentSample();
        startWaveAnimation('forward');
      }});

      document.getElementById('btn-reset-train').addEventListener('click', () => {{
        toggleTraining(false);
        nn.reset();
        const res = nn.evaluate(DATASET);
        targetAccDisplay = res.accuracy;
        targetLossDisplay = res.loss;
        nn.history.push(res);
        needsSynapsesCacheUpdate = true;
        document.getElementById('metric-step-text').textContent = `0/300`;
        document.getElementById('training-progress-fill').style.width = '0%';
        renderTrainingChart();
        renderCurrentSample();
      }});

      const speedSlider = document.getElementById('slider-speed');
      const speedLabel = document.getElementById('speed-label');
      speedSlider.addEventListener('input', (e) => {{
        speedLabel.textContent = `${{e.target.value}} steps/s`;
        if (isTraining) startTrainingLoop();
      }});

      const lrSlider = document.getElementById('slider-lr');
      const lrLabel = document.getElementById('lr-label');
      lrSlider.addEventListener('input', (e) => {{
        lrLabel.textContent = parseFloat(e.target.value).toFixed(2);
      }});

      // Launch 240Hz Render Loop
      requestAnimationFrame(renderAppFrame);
    }});
  </script>
</body>
</html>"""

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html_template)

print("Successfully generated upgraded 100vh 240Hz index.html!")
