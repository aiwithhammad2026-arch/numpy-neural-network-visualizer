import template_parts

def generate_html():
    css_content = """
    :root {
      --bg-dark: #07080d;
      --bg-card: rgba(13, 17, 28, 0.82);
      --bg-card-hover: rgba(18, 24, 40, 0.92);
      --border-subtle: rgba(255, 255, 255, 0.08);
      --border-glow: rgba(0, 242, 254, 0.35);
      
      --cyan: #00f2fe;
      --cyan-glow: rgba(0, 242, 254, 0.4);
      --pink: #ff007f;
      --pink-glow: rgba(255, 0, 127, 0.4);
      --purple: #8b5cf6;
      --purple-glow: rgba(139, 92, 246, 0.4);
      --emerald: #10b981;
      --emerald-glow: rgba(16, 185, 129, 0.4);
      --amber: #f59e0b;
      --red: #ef4444;
      
      --text-main: #f8fafc;
      --text-muted: #94a3b8;
      --text-dim: #64748b;
      
      --font-sans: 'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
      --font-mono: 'JetBrains Mono', 'Fira Code', monospace;
    }

    * {
      box-sizing: border-box;
      margin: 0;
      padding: 0;
    }

    html {
      scroll-behavior: smooth;
      background-color: var(--bg-dark);
      color: var(--text-main);
      font-family: var(--font-sans);
    }

    body {
      background-color: var(--bg-dark);
      color: var(--text-main);
      font-family: var(--font-sans);
      line-height: 1.4;
      overflow-x: hidden;
      min-height: 100vh;
      background-image: 
        radial-gradient(circle at 15% 15%, rgba(0, 242, 254, 0.05) 0%, transparent 40%),
        radial-gradient(circle at 85% 20%, rgba(139, 92, 246, 0.05) 0%, transparent 45%),
        radial-gradient(circle at 50% 85%, rgba(255, 0, 127, 0.04) 0%, transparent 50%);
    }

    /* Scrollbars */
    ::-webkit-scrollbar {
      width: 6px;
      height: 6px;
    }
    ::-webkit-scrollbar-track {
      background: rgba(7, 8, 13, 0.8);
    }
    ::-webkit-scrollbar-thumb {
      background: rgba(255, 255, 255, 0.15);
      border-radius: 3px;
    }
    ::-webkit-scrollbar-thumb:hover {
      background: var(--cyan);
    }

    /* TOP BAR (Compact, 46px) */
    .top-bar {
      height: 46px;
      padding: 0 clamp(10px, 2vw, 24px);
      display: flex;
      justify-content: space-between;
      align-items: center;
      border-bottom: 1px solid var(--border-subtle);
      background: rgba(8, 10, 18, 0.92);
      position: sticky;
      top: 0;
      z-index: 200;
    }

    .brand-group {
      display: flex;
      align-items: center;
      gap: 12px;
    }

    .brand-title {
      font-weight: 700;
      font-size: clamp(0.85rem, 1.2vw, 1.05rem);
      letter-spacing: -0.02em;
      display: flex;
      align-items: center;
      gap: 6px;
      white-space: nowrap;
    }

    .brand-title .logo-dot {
      width: 8px;
      height: 8px;
      border-radius: 50%;
      background: var(--cyan);
      box-shadow: 0 0 10px var(--cyan);
    }

    .brand-subtitle {
      font-size: clamp(0.68rem, 0.85vw, 0.78rem);
      color: var(--text-muted);
      font-family: var(--font-mono);
      white-space: nowrap;
      border-left: 1px solid var(--border-subtle);
      padding-left: 10px;
    }

    @media (max-width: 1024px) {
      .brand-subtitle { display: none; }
    }

    /* Nav Links */
    .nav-links {
      display: flex;
      align-items: center;
      gap: 6px;
    }

    .nav-btn {
      background: transparent;
      border: 1px solid transparent;
      color: var(--text-muted);
      font-size: clamp(0.72rem, 0.85vw, 0.82rem);
      font-family: var(--font-sans);
      font-weight: 500;
      padding: 4px 10px;
      border-radius: 6px;
      cursor: pointer;
      text-decoration: none;
      transition: color 0.15s, border-color 0.15s, background-color 0.15s;
    }

    .nav-btn:hover {
      color: var(--text-main);
      background: rgba(255, 255, 255, 0.05);
      border-color: var(--border-subtle);
    }

    .nav-btn.active {
      color: var(--cyan);
      background: rgba(0, 242, 254, 0.08);
      border-color: rgba(0, 242, 254, 0.25);
    }

    /* Header Right (Credit & FPS) */
    .header-right {
      display: flex;
      align-items: center;
      gap: 12px;
    }

    .credit-badge {
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
    }

    .credit-gradient-text {
      background: linear-gradient(135deg, #00f2fe 0%, #a855f7 50%, #ff007f 100%);
      -webkit-background-clip: text;
      -webkit-text-fill-color: transparent;
      font-weight: 700;
    }

    .pulsing-dot {
      width: 6px;
      height: 6px;
      border-radius: 50%;
      background: #10b981;
      box-shadow: 0 0 8px #10b981;
      animation: pulse-glow 2s infinite ease-in-out;
    }

    @keyframes pulse-glow {
      0%, 100% { opacity: 0.4; transform: scale(0.9); }
      50% { opacity: 1; transform: scale(1.2); }
    }

    .fps-badge {
      font-family: var(--font-mono);
      font-size: 0.72rem;
      color: var(--emerald);
      background: rgba(16, 185, 129, 0.08);
      border: 1px solid rgba(16, 185, 129, 0.25);
      padding: 3px 8px;
      border-radius: 4px;
      white-space: nowrap;
    }

    /* ==================== STUDIO SECTION (100dvh x 100vw, NO SCROLL) ==================== */
    #studio-section {
      width: 100vw;
      height: calc(100dvh - 46px);
      max-height: calc(100dvh - 46px);
      overflow: hidden;
      display: grid;
      grid-template-columns: minmax(280px, 320px) 1fr minmax(290px, 330px);
      gap: clamp(8px, 1vw, 14px);
      padding: clamp(6px, 1vw, 12px) clamp(8px, 1.5vw, 18px);
      position: relative;
    }

    /* Common Card Styles */
    .card {
      background: var(--bg-card);
      border: 1px solid var(--border-subtle);
      border-radius: 10px;
      overflow: hidden;
      display: flex;
      flex-direction: column;
      box-shadow: 0 4px 20px rgba(0, 0, 0, 0.35);
      min-height: 0;
    }

    .card-header {
      padding: clamp(6px, 0.8vh, 10px) clamp(10px, 1vw, 14px);
      border-bottom: 1px solid var(--border-subtle);
      display: flex;
      justify-content: space-between;
      align-items: center;
      background: rgba(255, 255, 255, 0.015);
      flex-shrink: 0;
    }

    .card-title {
      font-size: clamp(0.74rem, 0.9vw, 0.85rem);
      font-weight: 600;
      color: var(--text-main);
      display: flex;
      align-items: center;
      gap: 6px;
    }

    .card-body {
      padding: clamp(6px, 0.8vh, 10px) clamp(8px, 1vw, 12px);
      display: flex;
      flex-direction: column;
      gap: clamp(6px, 0.8vh, 10px);
      flex: 1;
      min-height: 0;
      overflow-y: auto;
    }

    /* Column Layouts */
    .studio-col-left, .studio-col-right {
      display: flex;
      flex-direction: column;
      gap: clamp(8px, 1vh, 12px);
      height: 100%;
      min-height: 0;
    }

    .studio-col-center {
      display: flex;
      flex-direction: column;
      height: 100%;
      min-height: 0;
      position: relative;
    }

    /* LEFT COLUMN: 8x8 Grid & Controls */
    .grid-container {
      display: flex;
      flex-direction: column;
      align-items: center;
      gap: clamp(6px, 0.8vh, 10px);
      width: 100%;
    }

    .pixel-grid {
      display: grid;
      grid-template-columns: repeat(8, 1fr);
      grid-template-rows: repeat(8, 1fr);
      gap: 2px;
      width: clamp(140px, 18vh, 175px);
      height: clamp(140px, 18vh, 175px);
      background: rgba(0, 0, 0, 0.6);
      padding: 4px;
      border-radius: 8px;
      border: 1px solid var(--border-subtle);
      box-shadow: inset 0 0 12px rgba(0, 0, 0, 0.7);
    }

    .pixel-cell {
      border-radius: 2px;
      transition: background-color 0.1s;
    }

    .sample-nav-row {
      display: flex;
      align-items: center;
      justify-content: space-between;
      width: 100%;
      gap: 6px;
    }

    .sample-meta {
      font-size: 0.72rem;
      font-family: var(--font-mono);
      color: var(--text-muted);
    }

    .btn-group {
      display: flex;
      gap: 4px;
    }

    /* Buttons */
    .btn {
      background: rgba(255, 255, 255, 0.05);
      border: 1px solid var(--border-subtle);
      color: var(--text-main);
      font-family: var(--font-sans);
      font-size: clamp(0.68rem, 0.8vw, 0.75rem);
      font-weight: 500;
      padding: clamp(4px, 0.6vh, 6px) clamp(8px, 0.8vw, 12px);
      border-radius: 6px;
      cursor: pointer;
      display: inline-flex;
      align-items: center;
      justify-content: center;
      gap: 5px;
      transition: background-color 0.15s, border-color 0.15s, transform 0.1s;
      white-space: nowrap;
      user-select: none;
    }

    .btn:hover {
      background: rgba(255, 255, 255, 0.1);
      border-color: rgba(255, 255, 255, 0.2);
    }

    .btn:active {
      transform: scale(0.97);
    }

    .btn-primary {
      background: rgba(0, 242, 254, 0.15);
      border-color: rgba(0, 242, 254, 0.4);
      color: var(--cyan);
    }
    .btn-primary:hover {
      background: rgba(0, 242, 254, 0.25);
      border-color: var(--cyan);
    }

    .btn-accent {
      background: rgba(139, 92, 246, 0.15);
      border-color: rgba(139, 92, 246, 0.4);
      color: #c084fc;
    }
    .btn-accent:hover {
      background: rgba(139, 92, 246, 0.25);
      border-color: var(--purple);
    }

    .btn-sm {
      padding: 3px 8px;
      font-size: 0.7rem;
    }

    /* Digit Chips (0-9) */
    .digit-chips-row {
      display: flex;
      justify-content: space-between;
      width: 100%;
      gap: 2px;
    }

    .digit-chip {
      flex: 1;
      height: 24px;
      display: flex;
      align-items: center;
      justify-content: center;
      background: rgba(255, 255, 255, 0.03);
      border: 1px solid var(--border-subtle);
      border-radius: 4px;
      font-family: var(--font-mono);
      font-size: 0.72rem;
      font-weight: 600;
      color: var(--text-muted);
      cursor: pointer;
      transition: all 0.15s;
    }

    .digit-chip:hover {
      color: var(--text-main);
      border-color: rgba(255, 255, 255, 0.2);
      background: rgba(255, 255, 255, 0.08);
    }

    .digit-chip.active {
      color: var(--cyan);
      border-color: var(--cyan);
      background: rgba(0, 242, 254, 0.12);
    }

    /* Softmax Probability Bars */
    .prob-list {
      display: flex;
      flex-direction: column;
      gap: clamp(2px, 0.35vh, 4px);
      width: 100%;
      flex: 1;
      justify-content: space-between;
    }

    .prob-item {
      display: flex;
      align-items: center;
      gap: 8px;
      font-size: clamp(0.68rem, 0.78vw, 0.74rem);
      font-family: var(--font-mono);
    }

    .prob-label {
      width: 16px;
      font-weight: 700;
      color: var(--text-muted);
      text-align: right;
    }

    .prob-track {
      flex: 1;
      height: clamp(8px, 1.1vh, 12px);
      background: rgba(255, 255, 255, 0.04);
      border-radius: 3px;
      overflow: hidden;
      border: 1px solid rgba(255, 255, 255, 0.04);
      position: relative;
    }

    .prob-fill {
      height: 100%;
      width: 0%;
      background: linear-gradient(90deg, rgba(0, 242, 254, 0.7), rgba(0, 242, 254, 1));
      border-radius: 2px;
      transition: width 0.12s ease-out;
    }

    .prob-val {
      width: 44px;
      text-align: right;
      color: var(--text-dim);
      font-size: 0.68rem;
    }

    .prob-item.target .prob-label {
      color: var(--emerald);
      text-shadow: 0 0 8px rgba(16, 185, 129, 0.5);
    }

    .prob-item.predicted .prob-fill {
      background: linear-gradient(90deg, #8b5cf6, #00f2fe);
      box-shadow: 0 0 10px rgba(0, 242, 254, 0.5);
    }
    .prob-item.predicted .prob-val {
      color: var(--cyan);
      font-weight: 700;
    }

    /* CENTER COLUMN: Canvas & HUD */
    .canvas-card {
      height: 100%;
      display: flex;
      flex-direction: column;
      position: relative;
    }

    .canvas-hud-top {
      padding: clamp(6px, 0.8vh, 10px) 14px;
      border-bottom: 1px solid var(--border-subtle);
      display: flex;
      justify-content: space-between;
      align-items: center;
      background: rgba(255, 255, 255, 0.015);
      flex-shrink: 0;
    }

    .legend-row {
      display: flex;
      align-items: center;
      gap: 12px;
      font-size: 0.7rem;
      font-family: var(--font-mono);
      color: var(--text-muted);
    }

    .legend-item {
      display: flex;
      align-items: center;
      gap: 4px;
    }

    .legend-dot {
      width: 7px;
      height: 7px;
      border-radius: 50%;
    }

    .canvas-viewport {
      flex: 1;
      width: 100%;
      position: relative;
      min-height: 0;
      background: radial-gradient(circle at 50% 50%, rgba(13, 17, 28, 0.6) 0%, rgba(6, 8, 14, 0.95) 100%);
    }

    #network-canvas {
      position: absolute;
      top: 0;
      left: 0;
      width: 100%;
      height: 100%;
      display: block;
    }

    .canvas-hud-bottom {
      padding: clamp(6px, 0.8vh, 10px) 14px;
      border-top: 1px solid var(--border-subtle);
      display: flex;
      justify-content: space-between;
      align-items: center;
      background: rgba(8, 10, 18, 0.85);
      flex-shrink: 0;
      gap: 10px;
    }

    .pulse-control-group {
      display: flex;
      align-items: center;
      gap: 8px;
    }

    /* RIGHT COLUMN: Training Dashboard & Chart */
    .metric-grid {
      display: grid;
      grid-template-columns: 1fr 1fr;
      gap: 8px;
      width: 100%;
    }

    .metric-box {
      background: rgba(0, 0, 0, 0.35);
      border: 1px solid var(--border-subtle);
      border-radius: 8px;
      padding: clamp(6px, 0.8vh, 10px) 10px;
      display: flex;
      flex-direction: column;
      gap: 2px;
    }

    .metric-title {
      font-size: 0.68rem;
      font-family: var(--font-mono);
      color: var(--text-dim);
      text-transform: uppercase;
      letter-spacing: 0.05em;
    }

    .metric-number {
      font-family: var(--font-mono);
      font-size: clamp(1.15rem, 1.6vw, 1.45rem);
      font-weight: 800;
      color: var(--cyan);
      line-height: 1.1;
    }

    .metric-number.loss {
      color: var(--pink);
    }

    .progress-wrapper {
      display: flex;
      flex-direction: column;
      gap: 4px;
      width: 100%;
    }

    .progress-meta {
      display: flex;
      justify-content: space-between;
      font-family: var(--font-mono);
      font-size: 0.7rem;
      color: var(--text-muted);
    }

    .progress-track {
      height: 6px;
      background: rgba(255, 255, 255, 0.05);
      border-radius: 3px;
      overflow: hidden;
      border: 1px solid rgba(255, 255, 255, 0.04);
    }

    .progress-fill {
      height: 100%;
      width: 0%;
      background: linear-gradient(90deg, var(--cyan), var(--purple));
      border-radius: 3px;
      transition: width 0.1s linear;
    }

    .controls-grid {
      display: grid;
      grid-template-columns: 1fr 1fr;
      gap: 6px;
      width: 100%;
    }

    /* Sliders */
    .slider-row {
      display: flex;
      flex-direction: column;
      gap: 3px;
      width: 100%;
    }

    .slider-header {
      display: flex;
      justify-content: space-between;
      font-size: 0.7rem;
      font-family: var(--font-mono);
      color: var(--text-muted);
    }

    .slider-val {
      color: var(--cyan);
      font-weight: 600;
    }

    input[type="range"] {
      -webkit-appearance: none;
      width: 100%;
      height: 4px;
      border-radius: 2px;
      background: rgba(255, 255, 255, 0.1);
      outline: none;
      margin: 4px 0;
    }

    input[type="range"]::-webkit-slider-thumb {
      -webkit-appearance: none;
      width: 13px;
      height: 13px;
      border-radius: 50%;
      background: var(--cyan);
      cursor: pointer;
      box-shadow: 0 0 6px var(--cyan);
      transition: transform 0.1s;
    }

    input[type="range"]::-webkit-slider-thumb:hover {
      transform: scale(1.2);
    }

    /* Live Chart Canvas */
    .chart-box {
      width: 100%;
      flex: 1;
      min-height: clamp(100px, 14vh, 160px);
      position: relative;
      background: rgba(0, 0, 0, 0.3);
      border-radius: 6px;
      border: 1px solid var(--border-subtle);
      overflow: hidden;
    }

    #loss-chart-canvas {
      position: absolute;
      top: 0;
      left: 0;
      width: 100%;
      height: 100%;
      display: block;
    }

    /* ==================== LOWER SECTIONS (Draw & Test, How It Works, Footer) ==================== */
    .lower-content-container {
      max-width: 1280px;
      margin: 0 auto;
      padding: clamp(30px, 5vh, 60px) clamp(16px, 3vw, 32px);
      display: flex;
      flex-direction: column;
      gap: clamp(40px, 6vh, 70px);
    }

    .section-title-wrap {
      text-align: center;
      margin-bottom: clamp(16px, 3vh, 28px);
    }

    .section-heading {
      font-size: clamp(1.3rem, 2vw, 1.8rem);
      font-weight: 800;
      letter-spacing: -0.02em;
      margin-bottom: 6px;
      display: flex;
      align-items: center;
      justify-content: center;
      gap: 10px;
    }

    .section-subtext {
      font-size: clamp(0.82rem, 1vw, 0.92rem);
      color: var(--text-muted);
      max-width: 640px;
      margin: 0 auto;
    }

    /* Draw & Test Section */
    .draw-container-grid {
      display: grid;
      grid-template-columns: auto 1fr;
      gap: clamp(20px, 3vw, 40px);
      background: var(--bg-card);
      border: 1px solid var(--border-subtle);
      border-radius: 12px;
      padding: clamp(16px, 2.5vw, 30px);
      align-items: center;
    }

    .draw-left-pad {
      display: flex;
      flex-direction: column;
      align-items: center;
      gap: 14px;
    }

    .draw-canvases-row {
      display: flex;
      align-items: center;
      gap: 16px;
    }

    #user-draw-canvas {
      width: 220px;
      height: 220px;
      background: #000;
      border: 2px solid var(--border-glow);
      border-radius: 10px;
      cursor: crosshair;
      touch-action: none;
      box-shadow: 0 0 20px rgba(0, 242, 254, 0.15);
    }

    .arrow-icon {
      color: var(--text-dim);
      font-size: 1.5rem;
    }

    .downscaled-wrap {
      display: flex;
      flex-direction: column;
      align-items: center;
      gap: 6px;
    }

    #downscaled-preview {
      width: 96px;
      height: 96px;
      display: grid;
      grid-template-columns: repeat(8, 1fr);
      grid-template-rows: repeat(8, 1fr);
      gap: 1px;
      background: #000;
      padding: 3px;
      border-radius: 6px;
      border: 1px solid var(--border-subtle);
    }

    .downscaled-cell {
      border-radius: 1px;
    }

    .draw-right-predictions {
      display: flex;
      flex-direction: column;
      gap: 16px;
    }

    .prediction-highlight-card {
      background: rgba(0, 0, 0, 0.4);
      border: 1px solid var(--border-subtle);
      border-radius: 10px;
      padding: 14px 20px;
      display: flex;
      align-items: center;
      gap: 20px;
    }

    .big-digit {
      font-size: 3rem;
      font-family: var(--font-mono);
      font-weight: 800;
      color: var(--cyan);
      text-shadow: 0 0 20px var(--cyan-glow);
      line-height: 1;
      width: 60px;
      text-align: center;
    }

    .prediction-meta {
      display: flex;
      flex-direction: column;
      gap: 2px;
    }

    .prediction-meta-title {
      font-size: 0.72rem;
      font-family: var(--font-mono);
      color: var(--text-muted);
      text-transform: uppercase;
      letter-spacing: 0.05em;
    }

    .prediction-meta-confidence {
      font-size: 1.25rem;
      font-weight: 700;
      color: var(--text-main);
    }

    /* How It Works (4 Cards) */
    .how-cards-grid {
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(260px, 1fr));
      gap: 16px;
      margin-bottom: 30px;
    }

    .how-card {
      background: var(--bg-card);
      border: 1px solid var(--border-subtle);
      border-radius: 10px;
      padding: 18px;
      display: flex;
      flex-direction: column;
      gap: 10px;
      transition: transform 0.2s, border-color 0.2s;
    }

    .how-card:hover {
      transform: translateY(-2px);
      border-color: rgba(255, 255, 255, 0.2);
    }

    .how-card-num {
      width: 26px;
      height: 26px;
      border-radius: 6px;
      background: rgba(0, 242, 254, 0.15);
      color: var(--cyan);
      display: flex;
      align-items: center;
      justify-content: center;
      font-family: var(--font-mono);
      font-weight: 700;
      font-size: 0.8rem;
    }

    .how-card-title {
      font-size: 1rem;
      font-weight: 700;
      color: var(--text-main);
    }

    .how-card-desc {
      font-size: 0.82rem;
      color: var(--text-muted);
      line-height: 1.5;
    }

    .math-snippet {
      background: rgba(0, 0, 0, 0.5);
      border: 1px solid var(--border-subtle);
      border-radius: 6px;
      padding: 8px 10px;
      font-family: var(--font-mono);
      font-size: 0.75rem;
      color: var(--cyan);
      overflow-x: auto;
    }

    /* Code Block Box */
    .code-container {
      background: #06080e;
      border: 1px solid var(--border-subtle);
      border-radius: 10px;
      overflow: hidden;
      margin-top: 10px;
    }

    .code-header {
      padding: 10px 16px;
      background: rgba(255, 255, 255, 0.02);
      border-bottom: 1px solid var(--border-subtle);
      display: flex;
      justify-content: space-between;
      align-items: center;
    }

    .code-title {
      font-family: var(--font-mono);
      font-size: 0.78rem;
      color: var(--text-muted);
      display: flex;
      align-items: center;
      gap: 8px;
    }

    pre.code-block {
      padding: 16px;
      font-family: var(--font-mono);
      font-size: clamp(0.72rem, 0.85vw, 0.82rem);
      line-height: 1.55;
      overflow-x: auto;
      color: #e2e8f0;
      background: transparent;
    }

    /* Syntax Tokens */
    .tok-kw { color: #c084fc; font-weight: 600; }
    .tok-fn { color: #38bdf8; }
    .tok-num { color: #f472b6; }
    .tok-comment { color: #64748b; font-style: italic; }

    /* Footer */
    footer {
      border-top: 1px solid var(--border-subtle);
      padding: 24px clamp(16px, 3vw, 32px);
      display: flex;
      justify-content: space-between;
      align-items: center;
      background: rgba(6, 8, 14, 0.95);
      font-size: 0.82rem;
      color: var(--text-muted);
    }

    /* Toast Notification */
    #milestone-toast {
      position: fixed;
      bottom: 24px;
      right: 24px;
      background: rgba(14, 20, 36, 0.95);
      border: 1px solid var(--cyan);
      box-shadow: 0 8px 30px rgba(0, 242, 254, 0.25);
      border-radius: 10px;
      padding: 14px 20px;
      display: flex;
      align-items: center;
      gap: 12px;
      z-index: 1000;
      transform: translateY(120px);
      opacity: 0;
      transition: transform 0.4s cubic-bezier(0.175, 0.885, 0.32, 1.275), opacity 0.4s ease;
      pointer-events: none;
    }

    #milestone-toast.show {
      transform: translateY(0);
      opacity: 1;
      pointer-events: auto;
    }

    #confetti-canvas {
      position: fixed;
      top: 0;
      left: 0;
      width: 100vw;
      height: 100vh;
      pointer-events: none;
      z-index: 999;
    }

    /* Responsive under 900px */
    @media (max-width: 900px) {
      #studio-section {
        height: auto;
        max-height: none;
        overflow: visible;
        grid-template-columns: 1fr;
      }
      .studio-col-left, .studio-col-center, .studio-col-right {
        height: auto;
      }
      .canvas-viewport {
        height: 480px;
      }
      .draw-container-grid {
        grid-template-columns: 1fr;
      }
    }

    @media (prefers-reduced-motion: reduce) {
      * {
        animation-duration: 0.01ms !important;
        animation-iteration-count: 1 !important;
        transition-duration: 0.01ms !important;
        scroll-behavior: auto !important;
      }
    }
    """

    # We assemble the full HTML
    html_code = f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Neural Network from Scratch | Hammad, AI Engineer</title>
  <meta name="description" content="A complete 64->32->10 Neural Network learning handwritten digits with pure JavaScript and full-batch backpropagation. Built by Hammad, AI Engineer.">
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&family=JetBrains+Mono:wght@400;500;600;700&display=swap" rel="stylesheet">
  <style>
{css_content}
  </style>
</head>
<body>

  <!-- Confetti Canvas -->
  <canvas id="confetti-canvas"></canvas>

  <!-- Compact Top Bar -->
  <header class="top-bar">
    <div class="brand-group">
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
    </div>
  </header>

  <!-- STUDIO SECTION (100dvh x 100vw, NO SCROLL ON DESKTOP) -->
  <section id="studio-section">

    <!-- LEFT COLUMN -->
    <div class="studio-col-left">
      <!-- 8x8 Input Card -->
      <div class="card" style="flex: 1.15;">
        <div class="card-header">
          <span class="card-title">
            <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="3" y="3" width="18" height="18" rx="2"/><path d="M3 9h18M9 21V9"/></svg>
            8×8 Input Matrix (64 Pixels)
          </span>
          <span id="target-digit-badge" style="font-size:0.72rem; font-family:var(--font-mono); color:var(--cyan); font-weight:700;">Target: 0</span>
        </div>
        <div class="card-body">
          <div class="grid-container">
            <div class="pixel-grid" id="studio-pixel-grid"></div>

            <div class="sample-nav-row">
              <span class="sample-meta" id="sample-meta-text">Sample #1 / 1797</span>
              <div class="btn-group">
                <button class="btn btn-sm" id="btn-prev-sample">◀ Prev</button>
                <button class="btn btn-sm" id="btn-rand-sample">🎲 Rand</button>
                <button class="btn btn-sm" id="btn-next-sample">Next ▶</button>
              </div>
            </div>

            <!-- Digit Chips 0-9 -->
            <div class="digit-chips-row" id="digit-chips-container"></div>
          </div>
        </div>
      </div>

      <!-- Prediction Card (10 Probabilities) -->
      <div class="card" style="flex: 1;">
        <div class="card-header">
          <span class="card-title">
            <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M18 20V10M12 20V4M6 20v-6"/></svg>
            Softmax Probabilities
          </span>
          <span id="studio-predicted-badge" style="font-size:0.72rem; font-family:var(--font-mono); color:var(--cyan); font-weight:700;">Pred: ?</span>
        </div>
        <div class="card-body" style="padding: 6px 10px;">
          <div class="prob-list" id="studio-prob-list"></div>
        </div>
      </div>
    </div>

    <!-- CENTER COLUMN: Network Canvas -->
    <div class="studio-col-center">
      <div class="card canvas-card">
        <div class="canvas-hud-top">
          <span class="card-title">
            <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="6" cy="6" r="3"/><circle cx="6" cy="18" r="3"/><circle cx="18" cy="12" r="3"/><path d="m8.5 7.5 7 3.5M8.5 16.5l7-3.5"/></svg>
            64 → 32 → 10 Network Architecture
          </span>
          <div class="legend-row">
            <div class="legend-item"><span class="legend-dot" style="background:var(--cyan)"></span><span>+W</span></div>
            <div class="legend-item"><span class="legend-dot" style="background:var(--pink)"></span><span>-W</span></div>
            <div class="legend-item"><span class="legend-dot" style="background:rgba(255,255,255,0.3)"></span><span>Top 15%</span></div>
          </div>
        </div>

        <div class="canvas-viewport" id="canvas-container">
          <canvas id="network-canvas"></canvas>
        </div>

        <div class="canvas-hud-bottom">
          <div class="pulse-control-group">
            <button class="btn btn-sm btn-primary" id="btn-forward-pulse">✨ Forward Pulse</button>
            <button class="btn btn-sm" id="btn-backprop-pulse" style="color:#ef4444; border-color:rgba(239,68,68,0.4);">🔥 Backprop Pulse</button>
            <label style="display:flex; align-items:center; gap:5px; font-size:0.7rem; font-family:var(--font-mono); color:var(--text-muted); cursor:pointer;">
              <input type="checkbox" id="check-auto-loop" checked style="accent-color:var(--cyan);">
              Auto-loop pulses
            </label>
          </div>

          <div style="display:flex; align-items:center; gap:8px;">
            <span style="font-size:0.7rem; font-family:var(--font-mono); color:var(--text-muted);">Pulse Speed:</span>
            <input type="range" id="slider-pulse-speed" min="0.25" max="2.0" step="0.05" value="1.0" style="width:70px;">
            <span id="val-pulse-speed" style="font-size:0.7rem; font-family:var(--font-mono); color:var(--cyan); width:28px;">1.0x</span>
          </div>
        </div>
      </div>
    </div>

    <!-- RIGHT COLUMN: Dashboard & Live Chart -->
    <div class="studio-col-right">
      <!-- Dashboard Card -->
      <div class="card" style="flex: 1.15;">
        <div class="card-header">
          <span class="card-title">
            <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M12 2v4M12 18v4M4.93 4.93l2.83 2.83M16.24 16.24l2.83 2.83M2 12h4M18 12h4M4.93 19.07l2.83-2.83M16.24 7.76l2.83-2.83"/></svg>
            Training Dashboard
          </span>
          <span id="train-status-pill" style="font-size:0.68rem; font-family:var(--font-mono); color:var(--text-muted); border:1px solid var(--border-subtle); padding:2px 6px; border-radius:4px;">Ready</span>
        </div>
        <div class="card-body">
          <!-- Metric Tiles -->
          <div class="metric-grid">
            <div class="metric-box">
              <span class="metric-title">Accuracy</span>
              <span class="metric-number" id="metric-accuracy">10.0%</span>
            </div>
            <div class="metric-box">
              <span class="metric-title">Loss (CE)</span>
              <span class="metric-number loss" id="metric-loss">2.33</span>
            </div>
          </div>

          <!-- Step Progress -->
          <div class="progress-wrapper">
            <div class="progress-meta">
              <span>Step: <strong id="metric-step" style="color:var(--text-main);">0 / 300</strong></span>
              <span>Target: 300</span>
            </div>
            <div class="progress-track">
              <div class="progress-fill" id="step-progress-fill"></div>
            </div>
          </div>

          <!-- Buttons -->
          <div class="controls-grid">
            <button class="btn btn-primary" id="btn-toggle-train">
              <span id="train-icon">▶</span>
              <span id="train-label">Start</span>
            </button>
            <button class="btn" id="btn-single-step">⏭ Step</button>
          </div>
          <div class="controls-grid">
            <button class="btn btn-accent" id="btn-train-300">⚡ Train to 300</button>
            <button class="btn" id="btn-reset-net">↺ Reset</button>
          </div>

          <!-- Sliders -->
          <div class="slider-row">
            <div class="slider-header">
              <span>Training Speed:</span>
              <span class="slider-val" id="val-speed">30 steps/s</span>
            </div>
            <input type="range" id="slider-speed" min="1" max="100" value="30">
          </div>

          <div class="slider-row">
            <div class="slider-header">
              <span>Learning Rate (η):</span>
              <span class="slider-val" id="val-lr">0.50</span>
            </div>
            <input type="range" id="slider-lr" min="0.05" max="1.50" step="0.05" value="0.50">
          </div>

          <div class="slider-row">
            <div class="slider-header">
              <span>Pulse Speed:</span>
              <span class="slider-val" id="val-pulse-speed-right">1.0x</span>
            </div>
            <input type="range" id="slider-pulse-speed-right" min="0.25" max="2.0" step="0.05" value="1.0">
          </div>
        </div>
      </div>

      <!-- Live Chart Card -->
      <div class="card" style="flex: 1;">
        <div class="card-header">
          <span class="card-title">
            <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M3 3v18h18"/><path d="m19 9-5 5-4-4-3 3"/></svg>
            Live Learning Curve
          </span>
          <div style="display:flex; gap:8px; font-size:0.68rem; font-family:var(--font-mono);">
            <span style="color:var(--cyan)">● Acc</span>
            <span style="color:var(--pink)">● Loss</span>
          </div>
        </div>
        <div class="card-body" style="padding: 6px 8px;">
          <div class="chart-box">
            <canvas id="loss-chart-canvas"></canvas>
          </div>
        </div>
      </div>
    </div>

  </section>

  <!-- LOWER SECTIONS -->
  <div class="lower-content-container">

    <!-- DRAW & TEST SECTION -->
    <section id="draw-section">
      <div class="section-title-wrap">
        <h2 class="section-heading">✍️ Draw & Test</h2>
        <p class="section-subtext">Draw any handwritten digit (0–9) below. The canvas crops, centers, downsamples to 8×8, and passes it through the live neural network.</p>
      </div>

      <div class="draw-container-grid">
        <div class="draw-left-pad">
          <div class="draw-canvases-row">
            <canvas id="user-draw-canvas" width="220" height="220"></canvas>
            <span class="arrow-icon">➔</span>
            <div class="downscaled-wrap">
              <div id="downscaled-preview"></div>
              <span style="font-size:0.7rem; font-family:var(--font-mono); color:var(--text-dim);">8×8 Downscaled</span>
            </div>
          </div>

          <div style="display:flex; gap:8px; width:100%; justify-content:center;">
            <button class="btn btn-sm" id="btn-clear-draw">🗑 Clear</button>
            <button class="btn btn-sm btn-primary" id="btn-feed-to-studio">⚡ Feed to Studio</button>
          </div>

          <div style="display:flex; align-items:center; gap:6px;">
            <span style="font-size:0.72rem; font-family:var(--font-mono); color:var(--text-muted);">Presets:</span>
            <button class="btn btn-sm draw-preset" data-d="0">0</button>
            <button class="btn btn-sm draw-preset" data-d="1">1</button>
            <button class="btn btn-sm draw-preset" data-d="3">3</button>
            <button class="btn btn-sm draw-preset" data-d="4">4</button>
            <button class="btn btn-sm draw-preset" data-d="7">7</button>
            <button class="btn btn-sm draw-preset" data-d="8">8</button>
          </div>
        </div>

        <div class="draw-right-predictions">
          <div class="prediction-highlight-card">
            <div class="big-digit" id="draw-big-digit">?</div>
            <div class="prediction-meta">
              <span class="prediction-meta-title">Live Model Prediction</span>
              <span class="prediction-meta-confidence" id="draw-confidence">Confidence: 0.0%</span>
            </div>
          </div>

          <div class="prob-list" id="draw-prob-list" style="height:auto; gap:4px;"></div>
        </div>
      </div>
    </section>

    <!-- HOW IT WORKS SECTION -->
    <section id="how-it-works-section">
      <div class="section-title-wrap">
        <h2 class="section-heading">📖 How It Works</h2>
        <p class="section-subtext">The mathematical foundation of deep learning implemented from scratch without PyTorch or TensorFlow.</p>
      </div>

      <div class="how-cards-grid">
        <div class="how-card">
          <div class="how-card-num">1</div>
          <h3 class="how-card-title">Forward Pass (Linear Dot Product)</h3>
          <p class="how-card-desc">Each layer calculates the weighted sum of its inputs and adds a learnable bias term.</p>
          <div class="math-snippet">
            Z⁽¹⁾ = X · W⁽¹⁾ + b⁽¹⁾<br>
            [1×64] · [64×32] + [1×32] = [1×32]
          </div>
        </div>

        <div class="how-card">
          <div class="how-card-num">2</div>
          <h3 class="how-card-title">Softmax & Cross-Entropy Loss</h3>
          <p class="how-card-desc">Softmax converts raw logits into a valid probability distribution summing to 1.0, evaluated against true labels.</p>
          <div class="math-snippet">
            P_k = exp(Z_k⁽²⁾) / ∑ exp(Z_j⁽²⁾)<br>
            ℒ = -∑ Y_k · ln(P_k)
          </div>
        </div>

        <div class="how-card">
          <div class="how-card-num">3</div>
          <h3 class="how-card-title">Backpropagation (Chain Rule)</h3>
          <p class="how-card-desc">Error signals flow backward through layers to compute exact partial derivatives with respect to each weight and bias.</p>
          <div class="math-snippet">
            δ⁽²⁾ = P - Y<br>
            δ⁽¹⁾ = (δ⁽²⁾ · (W⁽²⁾)ᵀ) ⊙ (Z⁽¹⁾ > 0)
          </div>
        </div>

        <div class="how-card">
          <div class="how-card-num">4</div>
          <h3 class="how-card-title">Gradient Step (Optimization)</h3>
          <p class="how-card-desc">Weights step in the opposite direction of the gradient scaled by the learning rate (η) to minimize loss.</p>
          <div class="math-snippet">
            W ← W - η · (Inputᵀ · δ)<br>
            b ← b - η · ∑ δ
          </div>
        </div>
      </div>

      <!-- Python NumPy Code Block -->
      <div class="code-container">
        <div class="code-header">
          <div class="code-title">
            <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="16 18 22 12 16 6"/><polyline points="8 6 2 12 8 18"/></svg>
            <span>NumPy Reference Implementation (300 Steps Full-Batch)</span>
          </div>
          <button class="btn btn-sm btn-primary" id="btn-copy-code">📋 Copy Code</button>
        </div>
        <pre class="code-block"><code>{template_parts.highlighted_py}</code></pre>
      </div>
    </section>

  </div>

  <!-- Footer -->
  <footer>
    <div>
      Designed &amp; built by <strong style="color:var(--cyan)">Hammad, AI Engineer</strong>
      <span style="opacity:0.4; margin:0 8px;">•</span>
      <a href="mailto:aiwithhammad2026@gmail.com" style="color:var(--purple); text-decoration:none;">aiwithhammad2026@gmail.com</a>
    </div>
    <button class="btn btn-sm" id="btn-back-to-top">↑ Back to top</button>
  </footer>

  <!-- Milestone Toast -->
  <div id="milestone-toast">
    <span style="font-size:1.6rem;">🎉</span>
    <div>
      <div style="font-weight:700; color:var(--cyan); font-size:0.9rem;">95% Accuracy Milestone Reached!</div>
      <div style="font-size:0.78rem; color:var(--text-muted);">The neural network has successfully learned handwritten digit representations.</div>
    </div>
  </div>

  <!-- Raw Python Code for Copying -->
  <textarea id="raw-python-code" style="display:none;">{template_parts.python_code_raw}</textarea>

  <!-- JAVASCRIPT APPLICATION LOGIC -->
  <script>
  (function() {{
    'use strict';

    // 1. EMBEDDED DATASET (1,797 samples from sklearn load_digits)
    const DIGITS_B64 = "{template_parts.b64_str}";
    const rawBin = atob(DIGITS_B64);
    const N = 1797;
    const X_DATA = new Float32Array(N * 64);
    const Y_DATA = new Int32Array(N);

    let bPtr = 0;
    for (let s = 0; s < N; s++) {{
      Y_DATA[s] = rawBin.charCodeAt(bPtr++);
      for (let i = 0; i < 64; i++) {{
        X_DATA[s * 64 + i] = rawBin.charCodeAt(bPtr++) / 16.0;
      }}
    }}

    // Gaussian normal generator
    function randn() {{
      let u = 0, v = 0;
      while (u === 0) u = Math.random();
      while (v === 0) v = Math.random();
      return Math.sqrt(-2.0 * Math.log(u)) * Math.cos(2.0 * Math.PI * v);
    }}

    // Cubic easing
    function easeInOutCubic(t) {{
      return t < 0.5 ? 4 * t * t * t : 1 - Math.pow(-2 * t + 2, 3) / 2;
    }}

    // 2. NEURAL NETWORK CLASS
    class NeuralNetwork {{
      constructor(inputSize = 64, hiddenSize = 32, outputSize = 10) {{
        this.inputSize = inputSize;
        this.hiddenSize = hiddenSize;
        this.outputSize = outputSize;
        this.step = 0;
        this.history = [];
        this.weightsDirty = true;
        this.lastWeightsDirtyTime = 0;
        this.reset();
      }}

      reset() {{
        this.step = 0;
        this.history = [];
        this.milestoneReached = false;
        
        this.W1 = new Float32Array(this.inputSize * this.hiddenSize);
        this.b1 = new Float32Array(this.hiddenSize);
        this.W2 = new Float32Array(this.hiddenSize * this.outputSize);
        this.b2 = new Float32Array(this.outputSize);

        // Standard deviation 0.1
        for (let i = 0; i < this.W1.length; i++) this.W1[i] = randn() * 0.1;
        for (let i = 0; i < this.W2.length; i++) this.W2[i] = randn() * 0.1;
        this.b1.fill(0);
        this.b2.fill(0);

        // Pre-allocated buffers for full-batch to avoid garbage collection
        this.Z1 = new Float32Array(N * this.hiddenSize);
        this.A1 = new Float32Array(N * this.hiddenSize);
        this.Z2 = new Float32Array(N * this.outputSize);
        this.Probs = new Float32Array(N * this.outputSize);
        this.dZ2 = new Float32Array(N * this.outputSize);

        this.dW1 = new Float32Array(this.inputSize * this.hiddenSize);
        this.db1 = new Float32Array(this.hiddenSize);
        this.dW2 = new Float32Array(this.hiddenSize * this.outputSize);
        this.db2 = new Float32Array(this.outputSize);

        // Delta tracking for backprop flash
        this.deltaW1 = new Float32Array(this.W1.length);
        this.deltaW2 = new Float32Array(this.W2.length);

        this.weightsDirty = true;
        this.lastWeightsDirtyTime = performance.now();

        // Initial evaluation
        const initial = this.evaluateFull();
        this.history.push({{ step: 0, loss: initial.loss, accuracy: initial.accuracy }});
        return initial;
      }}

      // Single forward pass for UI & testing
      forwardSingle(x) {{
        const z1 = new Float32Array(this.hiddenSize);
        const a1 = new Float32Array(this.hiddenSize);
        for (let j = 0; j < this.hiddenSize; j++) {{
          let sum = this.b1[j];
          for (let i = 0; i < this.inputSize; i++) {{
            sum += x[i] * this.W1[i * this.hiddenSize + j];
          }}
          z1[j] = sum;
          a1[j] = sum > 0 ? sum : 0; // ReLU
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

      // Fast evaluation over full dataset
      evaluateFull() {{
        let totalLoss = 0;
        let correct = 0;
        for (let s = 0; s < N; s++) {{
          const xOff = s * 64;
          const target = Y_DATA[s];
          let maxZ = -Infinity;
          
          // Hidden
          const a1 = new Float32Array(32);
          for (let j = 0; j < 32; j++) {{
            let sum = this.b1[j];
            for (let i = 0; i < 64; i++) sum += X_DATA[xOff + i] * this.W1[i * 32 + j];
            a1[j] = sum > 0 ? sum : 0;
          }}

          // Output
          const z2 = new Float32Array(10);
          for (let k = 0; k < 10; k++) {{
            let sum = this.b2[k];
            for (let j = 0; j < 32; j++) sum += a1[j] * this.W2[j * 10 + k];
            z2[k] = sum;
            if (sum > maxZ) maxZ = sum;
          }}

          let sumExp = 0;
          for (let k = 0; k < 10; k++) sumExp += Math.exp(z2[k] - maxZ);
          
          let maxP = -1, pred = 0;
          for (let k = 0; k < 10; k++) {{
            const p = Math.exp(z2[k] - maxZ) / sumExp;
            if (p > maxP) {{ maxP = p; pred = k; }}
            if (k === target) totalLoss += -Math.log(Math.max(p, 1e-15));
          }}
          if (pred === target) correct++;
        }}
        return {{ loss: totalLoss / N, accuracy: correct / N }};
      }}

      // One full-batch backprop step
      trainStep(lr = 0.5) {{
        if (this.step >= 300) return null;

        // 1. Z1 and A1 = ReLU(Z1)
        for (let s = 0; s < N; s++) {{
          const xOff = s * 64;
          const zOff = s * 32;
          for (let j = 0; j < 32; j++) {{
            let sum = this.b1[j];
            for (let i = 0; i < 64; i++) {{
              sum += X_DATA[xOff + i] * this.W1[i * 32 + j];
            }}
            this.Z1[zOff + j] = sum;
            this.A1[zOff + j] = sum > 0 ? sum : 0;
          }}
        }}

        // 2. Z2 and Softmax
        let totalLoss = 0;
        let correct = 0;

        for (let s = 0; s < N; s++) {{
          const aOff = s * 32;
          const z2Off = s * 10;
          let maxZ = -Infinity;
          for (let k = 0; k < 10; k++) {{
            let sum = this.b2[k];
            for (let j = 0; j < 32; j++) {{
              sum += this.A1[aOff + j] * this.W2[j * 10 + k];
            }}
            this.Z2[z2Off + k] = sum;
            if (sum > maxZ) maxZ = sum;
          }}

          let sumExp = 0;
          for (let k = 0; k < 10; k++) {{
            const e = Math.exp(this.Z2[z2Off + k] - maxZ);
            this.Probs[z2Off + k] = e;
            sumExp += e;
          }}

          const invSum = 1.0 / sumExp;
          let maxP = -1, pred = 0;
          const target = Y_DATA[s];
          for (let k = 0; k < 10; k++) {{
            const p = this.Probs[z2Off + k] * invSum;
            this.Probs[z2Off + k] = p;
            if (p > maxP) {{ maxP = p; pred = k; }}
            this.dZ2[z2Off + k] = (p - (k === target ? 1.0 : 0.0)) / N;
          }}

          if (pred === target) correct++;
          totalLoss += -Math.log(Math.max(this.Probs[z2Off + target], 1e-15));
        }}

        // 3. dW2 and db2
        this.dW2.fill(0);
        this.db2.fill(0);
        for (let s = 0; s < N; s++) {{
          const aOff = s * 32;
          const dzOff = s * 10;
          for (let k = 0; k < 10; k++) {{
            const dzk = this.dZ2[dzOff + k];
            this.db2[k] += dzk;
            for (let j = 0; j < 32; j++) {{
              this.dW2[j * 10 + k] += this.A1[aOff + j] * dzk;
            }}
          }}
        }}

        // 4. Backprop to hidden: dW1 and db1
        this.dW1.fill(0);
        this.db1.fill(0);
        for (let s = 0; s < N; s++) {{
          const dzOff = s * 10;
          const xOff = s * 64;
          const zOff = s * 32;
          for (let j = 0; j < 32; j++) {{
            if (this.Z1[zOff + j] <= 0) continue;
            let dz1 = 0;
            for (let k = 0; k < 10; k++) {{
              dz1 += this.dZ2[dzOff + k] * this.W2[j * 10 + k];
            }}
            this.db1[j] += dz1;
            for (let i = 0; i < 64; i++) {{
              const xi = X_DATA[xOff + i];
              if (xi !== 0) {{
                this.dW1[i * 32 + j] += xi * dz1;
              }}
            }}
          }}
        }}

        // 5. Update weights & track deltas
        for (let i = 0; i < this.W1.length; i++) {{
          const stepW = lr * this.dW1[i];
          this.W1[i] -= stepW;
          this.deltaW1[i] = Math.abs(stepW);
        }}
        for (let j = 0; j < this.b1.length; j++) {{
          this.b1[j] -= lr * this.db1[j];
        }}
        for (let i = 0; i < this.W2.length; i++) {{
          const stepW = lr * this.dW2[i];
          this.W2[i] -= stepW;
          this.deltaW2[i] = Math.abs(stepW);
        }}
        for (let k = 0; k < this.b2.length; k++) {{
          this.b2[k] -= lr * this.db2[k];
        }}

        this.step++;
        this.weightsDirty = true;
        this.lastWeightsDirtyTime = performance.now();

        const stepLoss = totalLoss / N;
        const stepAcc = correct / N;
        this.history.push({{ step: this.step, loss: stepLoss, accuracy: stepAcc }});
        return {{ step: this.step, loss: stepLoss, accuracy: stepAcc }};
      }}
    }}

    // Instantiate Neural Network
    const nn = new NeuralNetwork();

    // 3. PRE-RENDERED RADIAL GLOW SPRITES (Zero shadowBlur!)
    function createGlowSprite(color, size = 64) {{
      const c = document.createElement('canvas');
      c.width = size;
      c.height = size;
      const ctx = c.getContext('2d');
      const grad = ctx.createRadialGradient(size / 2, size / 2, 0, size / 2, size / 2, size / 2);
      grad.addColorStop(0, color);
      grad.addColorStop(0.4, color.replace('1)', '0.35)'));
      grad.addColorStop(1, 'rgba(0,0,0,0)');
      ctx.fillStyle = grad;
      ctx.fillRect(0, 0, size, size);
      return c;
    }}

    const spriteCyan = createGlowSprite('rgba(0, 242, 254, 1)');
    const spritePink = createGlowSprite('rgba(255, 0, 127, 1)');
    const spritePurple = createGlowSprite('rgba(139, 92, 246, 1)');
    const spriteRed = createGlowSprite('rgba(239, 68, 68, 1)');
    const spriteGreen = createGlowSprite('rgba(16, 185, 129, 1)');
    const spriteGold = createGlowSprite('rgba(245, 158, 11, 1)');

    // 4. CANVAS RENDERING & OFFSCREEN CONNECTIONS
    const canvas = document.getElementById('network-canvas');
    const ctx = canvas.getContext('2d', {{ alpha: false }});
    const canvasContainer = document.getElementById('canvas-container');

    // Offscreen canvas for static connections
    const offscreenConn = document.createElement('canvas');
    const offscreenCtx = offscreenConn.getContext('2d');

    let canvasWidth = 800;
    let canvasHeight = 600;
    let dpr = window.devicePixelRatio || 1;

    // Node coordinate arrays
    const inputPos = [];
    const hiddenPos = [];
    const outputPos = [];

    // Top 250 connections for wave light travel
    let topLightConnections = [];

    function updateNodePositions() {{
      inputPos.length = 0;
      hiddenPos.length = 0;
      outputPos.length = 0;

      const w = canvasWidth;
      const h = canvasHeight;

      // Layer X positions
      const xInput = w * 0.12;
      const xHidden = w * 0.50;
      const xOutput = w * 0.82;

      // Input nodes: 64 nodes arranged vertically
      const inMargin = h * 0.04;
      const inStep = (h - inMargin * 2) / 63;
      for (let i = 0; i < 64; i++) {{
        inputPos.push({{ x: xInput, y: inMargin + i * inStep, r: clamp(h * 0.005, 2.5, 4.5) }});
      }}

      // Hidden nodes: 32 nodes
      const hidMargin = h * 0.06;
      const hidStep = (h - hidMargin * 2) / 31;
      for (let j = 0; j < 32; j++) {{
        hiddenPos.push({{ x: xHidden, y: hidMargin + j * hidStep, r: clamp(h * 0.009, 4.5, 7.5) }});
      }}

      // Output nodes: 10 nodes
      const outMargin = h * 0.08;
      const outStep = (h - outMargin * 2) / 9;
      for (let k = 0; k < 10; k++) {
        outputPos.push({ x: xOutput, y: outMargin + k * outStep, r: clamp(h * 0.018, 9.0, 14.0) });
      }
    }

    function resizeCanvas() {
      const rect = canvasContainer.getBoundingClientRect();
      canvasWidth = rect.width > 20 ? rect.width : (canvasContainer.clientWidth || 800);
      canvasHeight = rect.height > 20 ? rect.height : (canvasContainer.clientHeight || 600);
      dpr = Math.min(window.devicePixelRatio || 1, 2);

      canvas.width = Math.round(canvasWidth * dpr);
      canvas.height = Math.round(canvasHeight * dpr);
      ctx.setTransform(dpr, 0, 0, dpr, 0, 0);

      offscreenConn.width = Math.round(canvasWidth * dpr);
      offscreenConn.height = Math.round(canvasHeight * dpr);
      offscreenCtx.setTransform(dpr, 0, 0, dpr, 0, 0);

      updateNodePositions();
      rebuildOffscreenConnections();
      drawChart();
    }

    const resizeObserver = new ResizeObserver(() => {
      resizeCanvas();
    });
    resizeObserver.observe(canvasContainer);

    function clamp(val, min, max) {
      return Math.max(min, Math.min(max, val));
    }

    // REBUILD STATIC CONNECTIONS (Max 10 times/sec during training)
    let lastOffscreenBuildTime = 0;

    function rebuildOffscreenConnections() {
      if (inputPos.length === 0 || hiddenPos.length === 0 || outputPos.length === 0) {
        updateNodePositions();
      }
      offscreenCtx.clearRect(0, 0, canvasWidth, canvasHeight);
      topLightConnections = [];

      // Collect all connections with weights
      const conns1 = [];
      for (let i = 0; i < 64; i++) {
        for (let j = 0; j < 32; j++) {
          const w = nn.W1[i * 32 + j];
          conns1.push({ layer: 1, from: i, to: j, w, absW: Math.abs(w), p1: inputPos[i], p2: hiddenPos[j] });
        }
      }

      const conns2 = [];
      for (let j = 0; j < 32; j++) {
        for (let k = 0; k < 10; k++) {
          const w = nn.W2[j * 10 + k];
          conns2.push({ layer: 2, from: j, to: k, w, absW: Math.abs(w), p1: hiddenPos[j], p2: outputPos[k] });
        }
      }

      const allConns = conns1.concat(conns2);
      allConns.sort((a, b) => b.absW - a.absW);

      // Top 15% strong connections
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
      offscreenCtx.stroke(negPath);

      lastOffscreenBuildTime = performance.now();
      nn.weightsDirty = false;
    }

    // 5. SLOW, SMOOTH PULSE ENGINE
    let pulseState = {{
      active: true,
      mode: 'forward', // 'forward' or 'backprop'
      startTime: 0,
      duration: 4000,
      progress: 0,
      speed: 1.0,
      autoLoop: true,
      cooldown: 0
    }};

    function triggerPulse(mode = 'forward') {{
      pulseState.active = true;
      pulseState.mode = mode;
      pulseState.startTime = performance.now();
      pulseState.progress = 0;
      pulseState.duration = 4000 / pulseState.speed;
    }}

    // 6. ACTIVE STUDIO SAMPLE & DRAW PAD STATE
    let currentSampleIndex = 0;
    let customStudioInput = null; // null or Float32Array(64) from drawing pad

    function getCurrentInputPixels() {{
      if (customStudioInput) return customStudioInput;
      const off = currentSampleIndex * 64;
      return X_DATA.subarray(off, off + 64);
    }}

    function getCurrentTargetDigit() {{
      if (customStudioInput) return -1;
      return Y_DATA[currentSampleIndex];
    }}

    // 7. MAIN RENDER LOOP (requestAnimationFrame only, up to 240 Hz)
    let lastFrameTime = performance.now();
    let frameCount = 0;
    let fpsTimer = 0;
    let currentFPS = 60;

    // Node activation trails
    const inputTrails = new Float32Array(64);
    const hiddenTrails = new Float32Array(32);
    const outputTrails = new Float32Array(10);

    function renderLoop(now) {{
      const dt = Math.min((now - lastFrameTime) / 1000, 0.1);
      lastFrameTime = now;

      // FPS Tracking
      frameCount++;
      fpsTimer += dt;
      if (fpsTimer >= 0.5) {{
        currentFPS = Math.round(frameCount / fpsTimer);
        document.getElementById('fps-counter').textContent = `${{currentFPS}} FPS`;
        frameCount = 0;
        fpsTimer = 0;
      }}

      // Check if offscreen connection canvas needs rebuild (max 10 times/sec)
      if (nn.weightsDirty && (now - lastOffscreenBuildTime >= 100)) {{
        rebuildOffscreenConnections();
      }}

      // Forward pass on active studio sample for live visualizations
      const inputPixels = getCurrentInputPixels();
      const targetDigit = getCurrentTargetDigit();
      const {{ a1, probs }} = nn.forwardSingle(inputPixels);

      // Identify predicted digit
      let predictedDigit = 0;
      let maxProb = -1;
      for (let k = 0; k < 10; k++) {{
        if (probs[k] > maxProb) {{
          maxProb = probs[k];
          predictedDigit = k;
        }}
      }}

      // PULSE PROGRESS UPDATE
      if (pulseState.active) {{
        const elapsed = now - pulseState.startTime;
        pulseState.progress = clamp(elapsed / pulseState.duration, 0, 1);
        
        if (pulseState.progress >= 1) {{
          pulseState.active = false;
          if (pulseState.autoLoop) {{
            pulseState.cooldown = now + 400; // brief pause before next loop
          }}
        }}
      }} else if (pulseState.autoLoop && now >= pulseState.cooldown && pulseState.cooldown > 0) {{
        pulseState.cooldown = 0;
        triggerPulse('forward');
      }}

      const waveProgress = easeInOutCubic(pulseState.progress);
      const isForward = pulseState.mode === 'forward';
      const isBackprop = pulseState.mode === 'backprop';

      // Trail decay
      const decay = Math.exp(-2.5 * dt);
      for (let i = 0; i < 64; i++) inputTrails[i] *= decay;
      for (let j = 0; j < 32; j++) hiddenTrails[j] *= decay;
      for (let k = 0; k < 10; k++) outputTrails[k] *= decay;

      // Wave hit triggers
      if (pulseState.active) {{
        if (isForward) {{
          // Input layer wave hit around t=0.0 to 0.15
          if (pulseState.progress < 0.25) {{
            for (let i = 0; i < 64; i++) {{
              if (inputPixels[i] > 0.1) inputTrails[i] = Math.max(inputTrails[i], inputPixels[i]);
            }}
          }}
          // Hidden layer wave hit around t=0.45 to 0.65
          if (pulseState.progress >= 0.4 && pulseState.progress <= 0.65) {{
            for (let j = 0; j < 32; j++) {{
              hiddenTrails[j] = Math.max(hiddenTrails[j], Math.min(1.0, a1[j] * 0.8 + 0.3));
            }}
          }}
          // Output layer hit around t=0.85 to 1.0
          if (pulseState.progress >= 0.8) {{
            for (let k = 0; k < 10; k++) {{
              outputTrails[k] = Math.max(outputTrails[k], probs[k]);
            }}
          }}
        }} else if (isBackprop) {{
          // Wave travels from Output (x=1) -> Hidden (x=0.5) -> Input (x=0)
          if (pulseState.progress < 0.25) {{
            for (let k = 0; k < 10; k++) outputTrails[k] = 1.0;
          }}
          if (pulseState.progress >= 0.4 && pulseState.progress <= 0.65) {{
            for (let j = 0; j < 32; j++) hiddenTrails[j] = 1.0;
          }}
          if (pulseState.progress >= 0.8) {{
            for (let i = 0; i < 64; i++) inputTrails[i] = 1.0;
          }}
        }}
      }}

      // --- CLEAR MAIN CANVAS ---
      ctx.fillStyle = '#07080d';
      ctx.fillRect(0, 0, canvasWidth, canvasHeight);

      // --- DRAW STATIC CONNECTIONS FROM OFFSCREEN CANVAS ---
      ctx.drawImage(offscreenConn, 0, 0, canvasWidth, canvasHeight);

      // --- DRAW LAYER HEADER BADGES ---
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
      }

      // --- DRAW WAVE PULSE PACKETS & GLOW ALONG TOP CONNECTIONS ---
      if (pulseState.active) {
        ctx.save();
        ctx.globalCompositeOperation = 'lighter';

        if (isForward) {{
          // Forward wave packets traveling along topLightConnections
          for (let c of topLightConnections) {{
            let packetT = 0;
            if (c.layer === 1) {{
              // t from 0.05 to 0.55
              packetT = (waveProgress - 0.05) / 0.50;
            }} else {{
              // t from 0.50 to 0.95
              packetT = (waveProgress - 0.50) / 0.45;
            }}

            if (packetT >= 0 && packetT <= 1) {{
              const px = c.p1.x + (c.p2.x - c.p1.x) * packetT;
              const py = c.p1.y + (c.p2.y - c.p1.y) * packetT;
              const r = 12;
              const sprite = c.w > 0 ? spriteCyan : spritePink;
              ctx.drawImage(sprite, px - r, py - r, r * 2, r * 2);
            }}
          }}
        }} else if (isBackprop) {{
          // Backprop red wave traveling right to left
          const backT = 1 - waveProgress; // travels from 1 to 0
          for (let c of topLightConnections) {{
            let packetT = 0;
            if (c.layer === 2) {{
              packetT = (waveProgress - 0.05) / 0.48;
            }} else {{
              packetT = (waveProgress - 0.50) / 0.48;
            }}

            if (packetT >= 0 && packetT <= 1) {{
              // Backwards: from p2 to p1
              const px = c.p2.x - (c.p2.x - c.p1.x) * packetT;
              const py = c.p2.y - (c.p2.y - c.p1.y) * packetT;
              const r = 14;
              ctx.drawImage(spriteRed, px - r, py - r, r * 2, r * 2);
            }}
          }}

          // Flash weights that changed most when wave nears completion
          if (waveProgress > 0.75) {{
            const flashAlpha = Math.sin((waveProgress - 0.75) * 4 * Math.PI);
            if (flashAlpha > 0) {{
              for (let i = 0; i < 15; i++) {{
                const c = topLightConnections[i];
                if (c) {{
                  const mx = (c.p1.x + c.p2.x) / 2;
                  const my = (c.p1.y + c.p2.y) / 2;
                  ctx.drawImage(spriteGold, mx - 16, my - 16, 32, 32);
                }}
              }}
            }}
          }}
        }}

        ctx.restore();
      }}

      // --- DRAW INPUT NODES (64) ---
      for (let i = 0; i < 64; i++) {
        const node = inputPos[i];
        if (!node) continue;
        const act = inputPixels[i];
        const trail = inputTrails[i];
        const intensity = Math.max(act, trail);

        // Node circle
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
      ctx.font = '600 12px "JetBrains Mono", monospace';
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
      }

      // SMOOTH ACCURACY & LOSS COUNT-UP INTERPOLATION
      updateCountUpAnimation(dt);

      requestAnimationFrame(renderLoop);
    }}

    // 8. ACCURACY & LOSS COUNT-UP SYSTEM
    let currentDispAcc = 10.0;
    let targetAcc = 10.0;
    let currentDispLoss = 2.33;
    let targetLoss = 2.33;

    function updateCountUpAnimation(dt) {{
      const accElem = document.getElementById('metric-accuracy');
      const lossElem = document.getElementById('metric-loss');

      const lerpFactor = Math.min(1.0, 10.0 * dt);
      currentDispAcc += (targetAcc - currentDispAcc) * lerpFactor;
      currentDispLoss += (targetLoss - currentDispLoss) * lerpFactor;

      accElem.textContent = currentDispAcc.toFixed(1) + '%';
      lossElem.textContent = currentDispLoss.toFixed(2);
    }}

    // 9. LIVE CHART RENDERING (Redraws ONLY when new step arrives)
    const chartCanvas = document.getElementById('loss-chart-canvas');
    const chartCtx = chartCanvas.getContext('2d');

    function drawChart() {{
      const rect = chartCanvas.parentElement.getBoundingClientRect();
      const w = Math.max(rect.width, 200);
      const h = Math.max(rect.height, 90);
      const cDpr = Math.min(window.devicePixelRatio || 1, 2);

      chartCanvas.width = Math.round(w * cDpr);
      chartCanvas.height = Math.round(h * cDpr);
      chartCtx.setTransform(cDpr, 0, 0, cDpr, 0, 0);

      chartCtx.fillStyle = 'rgba(8, 11, 20, 0.9)';
      chartCtx.fillRect(0, 0, w, h);

      // Grid lines
      chartCtx.strokeStyle = 'rgba(255, 255, 255, 0.05)';
      chartCtx.lineWidth = 1;
      for (let y = 0.25; y <= 0.75; y += 0.25) {{
        chartCtx.beginPath();
        chartCtx.moveTo(0, h * y);
        chartCtx.lineTo(w, h * y);
        chartCtx.stroke();
      }}

      const hist = nn.history;
      if (!hist || hist.length < 2) return;

      const paddingLeft = 32;
      const paddingBottom = 16;
      const plotW = w - paddingLeft - 8;
      const plotH = h - paddingBottom - 8;

      // Accuracy path (0.0 to 1.0)
      chartCtx.beginPath();
      for (let i = 0; i < hist.length; i++) {{
        const pt = hist[i];
        const px = paddingLeft + (pt.step / 300) * plotW;
        const py = (h - paddingBottom) - pt.accuracy * plotH;
        if (i === 0) chartCtx.moveTo(px, py);
        else chartCtx.lineTo(px, py);
      }}
      chartCtx.strokeStyle = '#00f2fe';
      chartCtx.lineWidth = 1.8;
      chartCtx.stroke();

      // Loss path (scale 0.0 to 2.5)
      chartCtx.beginPath();
      for (let i = 0; i < hist.length; i++) {{
        const pt = hist[i];
        const px = paddingLeft + (pt.step / 300) * plotW;
        const normalizedLoss = Math.min(pt.loss / 2.5, 1.0);
        const py = (h - paddingBottom) - normalizedLoss * plotH;
        if (i === 0) chartCtx.moveTo(px, py);
        else chartCtx.lineTo(px, py);
      }}
      chartCtx.strokeStyle = '#ff007f';
      chartCtx.lineWidth = 1.8;
      chartCtx.stroke();

      // Y-axis labels
      chartCtx.font = '9px "JetBrains Mono", monospace';
      chartCtx.fillStyle = 'rgba(148, 163, 184, 0.6)';
      chartCtx.textAlign = 'right';
      chartCtx.fillText('100%', paddingLeft - 4, 12);
      chartCtx.fillText('0%', paddingLeft - 4, h - paddingBottom);
    }}

    // 10. TRAINING CONTROLLER (Independent timer with steps/sec slider)
    let isTraining = false;
    let trainingTimer = null;
    let trainingSpeed = 30; // steps/sec
    let learningRate = 0.50;

    function applyTrainingStep() {{
      const res = nn.trainStep(learningRate);
      if (!res) {{
        pauseTraining();
        return;
      }}

      targetAcc = res.accuracy * 100;
      targetLoss = res.loss;

      // Update step progress
      document.getElementById('metric-step').textContent = `${{res.step}} / 300`;
      document.getElementById('step-progress-fill').style.width = `${{(res.step / 300) * 100}}%`;

      // Redraw live chart only on new step
      drawChart();

      // Check 95% accuracy milestone
      if (res.accuracy >= 0.95 && !nn.milestoneReached) {{
        nn.milestoneReached = true;
        fireConfetti();
        showMilestoneToast();
      }}

      // Live update drawing pad prediction if open
      if (isDrawingPadActive) {{
        updateDrawPredictions();
      }}

      // Live update studio probability bars
      updateStudioUI();

      if (res.step >= 300) {{
        pauseTraining();
        document.getElementById('train-status-pill').textContent = 'Completed (300)';
        document.getElementById('train-status-pill').style.color = '#10b981';
      }}
    }}

    function scheduleNextTrainingStep() {{
      if (!isTraining) return;
      applyTrainingStep();
      if (isTraining && nn.step < 300) {{
        const delay = Math.max(1, Math.round(1000 / trainingSpeed));
        trainingTimer = setTimeout(scheduleNextTrainingStep, delay);
      }}
    }}

    function startTraining() {{
      if (nn.step >= 300) return;
      isTraining = true;
      document.getElementById('train-icon').textContent = '⏸';
      document.getElementById('train-label').textContent = 'Pause';
      document.getElementById('train-status-pill').textContent = 'Training...';
      document.getElementById('train-status-pill').style.color = '#00f2fe';
      scheduleNextTrainingStep();
    }}

    function pauseTraining() {{
      isTraining = false;
      if (trainingTimer) clearTimeout(trainingTimer);
      document.getElementById('train-icon').textContent = '▶';
      document.getElementById('train-label').textContent = 'Start';
      document.getElementById('train-status-pill').textContent = nn.step >= 300 ? 'Completed (300)' : 'Paused';
    }}

    function resetTraining() {{
      pauseTraining();
      const initial = nn.reset();
      targetAcc = initial.accuracy * 100;
      targetLoss = initial.loss;
      currentDispAcc = targetAcc;
      currentDispLoss = targetLoss;
      document.getElementById('metric-accuracy').textContent = targetAcc.toFixed(1) + '%';
      document.getElementById('metric-loss').textContent = targetLoss.toFixed(2);
      document.getElementById('metric-step').textContent = '0 / 300';
      document.getElementById('step-progress-fill').style.width = '0%';
      document.getElementById('train-status-pill').textContent = 'Ready';
      document.getElementById('train-status-pill').style.color = '#94a3b8';
      rebuildOffscreenConnections();
      drawChart();
      updateStudioUI();
      if (isDrawingPadActive) updateDrawPredictions();
    }}

    // 11. STUDIO UI: 8x8 GRID & SOFTMAX BARS
    const pixelGridContainer = document.getElementById('studio-pixel-grid');
    const probListContainer = document.getElementById('studio-prob-list');

    // Build 64 pixel cells in 8x8 grid
    const pixelCells = [];
    for (let i = 0; i < 64; i++) {{
      const cell = document.createElement('div');
      cell.className = 'pixel-cell';
      pixelGridContainer.appendChild(cell);
      pixelCells.push(cell);
    }}

    // Build 10 Softmax Probability Bars
    const probRows = [];
    for (let k = 0; k < 10; k++) {{
      const item = document.createElement('div');
      item.className = 'prob-item';
      item.innerHTML = `
        <span class="prob-label">[${{k}}]</span>
        <div class="prob-track"><div class="prob-fill"></div></div>
        <span class="prob-val">0.0%</span>
      `;
      probListContainer.appendChild(item);
      probRows.push({{
        item,
        fill: item.querySelector('.prob-fill'),
        val: item.querySelector('.prob-val')
      }});
    }}

    // Digit chips 0-9
    const chipsContainer = document.getElementById('digit-chips-container');
    const chipBtns = [];
    for (let d = 0; d < 10; d++) {{
      const chip = document.createElement('button');
      chip.className = 'digit-chip';
      chip.textContent = d;
      chip.addEventListener('click', () => {{
        customStudioInput = null;
        // Jump to first sample with this target digit
        for (let s = 0; s < N; s++) {{
          if (Y_DATA[s] === d) {{
            currentSampleIndex = s;
            break;
          }}
        }}
        updateStudioUI();
        triggerPulse('forward');
      }});
      chipsContainer.appendChild(chip);
      chipBtns.push(chip);
    }}

    function updateStudioUI() {{
      const inputPixels = getCurrentInputPixels();
      const targetDigit = getCurrentTargetDigit();
      const {{ probs }} = nn.forwardSingle(inputPixels);

      // 1. Update 8x8 grid cells
      for (let i = 0; i < 64; i++) {{
        const v = inputPixels[i];
        if (v > 0.05) {{
          const b = Math.round(v * 255);
          pixelCells[i].style.backgroundColor = `rgb(${{Math.round(b * 0.1)}}, ${{Math.round(b * 0.95)}}, ${{Math.round(b * 1.0)}})`;
        }} else {{
          pixelCells[i].style.backgroundColor = 'rgba(255, 255, 255, 0.02)';
        }}
      }}

      // 2. Sample info & chips
      if (customStudioInput) {{
        document.getElementById('sample-meta-text').textContent = 'Custom Drawn Digit';
        document.getElementById('target-digit-badge').textContent = 'Target: Drawing';
        chipBtns.forEach(c => c.classList.remove('active'));
      }} else {{
        document.getElementById('sample-meta-text').textContent = `Sample #${{currentSampleIndex + 1}} / 1797`;
        document.getElementById('target-digit-badge').textContent = `Target: ${{targetDigit}}`;
        chipBtns.forEach((c, idx) => {{
          c.classList.toggle('active', idx === targetDigit);
        }});
      }}

      // 3. Find predicted digit
      let maxP = -1, pred = 0;
      for (let k = 0; k < 10; k++) {{
        if (probs[k] > maxP) {{ maxP = probs[k]; pred = k; }}
      }}

      document.getElementById('studio-predicted-badge').textContent = `Pred: ${{pred}} (${{(maxP * 100).toFixed(1)}}%)`;

      // 4. Update 10 probability bars
      for (let k = 0; k < 10; k++) {{
        const row = probRows[k];
        const p = probs[k];
        const pct = (p * 100).toFixed(1) + '%';
        row.fill.style.width = pct;
        row.val.textContent = pct;

        row.item.classList.toggle('target', k === targetDigit);
        row.item.classList.toggle('predicted', k === pred);
      }}
    }}

    // Sample Navigation Buttons
    document.getElementById('btn-prev-sample').addEventListener('click', () => {{
      customStudioInput = null;
      currentSampleIndex = (currentSampleIndex - 1 + N) % N;
      updateStudioUI();
      triggerPulse('forward');
    }});

    document.getElementById('btn-next-sample').addEventListener('click', () => {{
      customStudioInput = null;
      currentSampleIndex = (currentSampleIndex + 1) % N;
      updateStudioUI();
      triggerPulse('forward');
    }});

    document.getElementById('btn-rand-sample').addEventListener('click', () => {{
      customStudioInput = null;
      currentSampleIndex = Math.floor(Math.random() * N);
      updateStudioUI();
      triggerPulse('forward');
    }});

    // Training Buttons
    document.getElementById('btn-toggle-train').addEventListener('click', () => {{
      if (isTraining) pauseTraining();
      else startTraining();
    }});

    document.getElementById('btn-single-step').addEventListener('click', () => {{
      pauseTraining();
      applyTrainingStep();
    }});

    document.getElementById('btn-train-300').addEventListener('click', () => {{
      pauseTraining();
      // Fast burst: train all remaining steps immediately
      while (nn.step < 300) {{
        nn.trainStep(learningRate);
      }}
      const last = nn.history[nn.history.length - 1];
      targetAcc = last.accuracy * 100;
      targetLoss = last.loss;
      document.getElementById('metric-step').textContent = '300 / 300';
      document.getElementById('step-progress-fill').style.width = '100%';
      document.getElementById('train-status-pill').textContent = 'Completed (300)';
      document.getElementById('train-status-pill').style.color = '#10b981';
      rebuildOffscreenConnections();
      drawChart();
      updateStudioUI();
      if (isDrawingPadActive) updateDrawPredictions();

      if (last.accuracy >= 0.95 && !nn.milestoneReached) {{
        nn.milestoneReached = true;
        fireConfetti();
        showMilestoneToast();
      }}
    }});

    document.getElementById('btn-reset-net').addEventListener('click', () => {{
      resetTraining();
    }});

    // Sliders
    const sliderSpeed = document.getElementById('slider-speed');
    const valSpeed = document.getElementById('val-speed');
    sliderSpeed.addEventListener('input', (e) => {{
      trainingSpeed = parseInt(e.target.value, 10);
      valSpeed.textContent = `${{trainingSpeed}} steps/s`;
    }});

    const sliderLr = document.getElementById('slider-lr');
    const valLr = document.getElementById('val-lr');
    sliderLr.addEventListener('input', (e) => {{
      learningRate = parseFloat(e.target.value);
      valLr.textContent = learningRate.toFixed(2);
    }});

    const sliderPulseSpeed = document.getElementById('slider-pulse-speed');
    const valPulseSpeed = document.getElementById('val-pulse-speed');
    const sliderPulseSpeedRight = document.getElementById('slider-pulse-speed-right');
    const valPulseSpeedRight = document.getElementById('val-pulse-speed-right');

    function onPulseSpeedChange(speed) {{
      pulseState.speed = speed;
      const speedStr = speed.toFixed(1) + 'x';
      if (valPulseSpeed) valPulseSpeed.textContent = speedStr;
      if (valPulseSpeedRight) valPulseSpeedRight.textContent = speedStr;
      if (sliderPulseSpeed) sliderPulseSpeed.value = speed;
      if (sliderPulseSpeedRight) sliderPulseSpeedRight.value = speed;
      pulseState.duration = 4000 / pulseState.speed;
    }}

    if (sliderPulseSpeed) {{
      sliderPulseSpeed.addEventListener('input', (e) => {{
        onPulseSpeedChange(parseFloat(e.target.value));
      }});
    }}
    if (sliderPulseSpeedRight) {{
      sliderPulseSpeedRight.addEventListener('input', (e) => {{
        onPulseSpeedChange(parseFloat(e.target.value));
      }});
    }}

    const checkAutoLoop = document.getElementById('check-auto-loop');
    checkAutoLoop.addEventListener('change', (e) => {{
      pulseState.autoLoop = e.target.checked;
    }});

    document.getElementById('btn-forward-pulse').addEventListener('click', () => {{
      triggerPulse('forward');
    }});

    document.getElementById('btn-backprop-pulse').addEventListener('click', () => {{
      triggerPulse('backprop');
    }});

    // 12. DRAW & TEST INTERACTIVE PAD
    const drawCanvas = document.getElementById('user-draw-canvas');
    const drawCtx = drawCanvas.getContext('2d');
    const downscaledContainer = document.getElementById('downscaled-preview');
    const drawProbContainer = document.getElementById('draw-prob-list');

    let isDrawing = false;
    let isDrawingPadActive = true;
    let drawnNormalizedPixels = new Float32Array(64);

    // Build 64 downscaled preview cells
    const downscaledCells = [];
    for (let i = 0; i < 64; i++) {{
      const cell = document.createElement('div');
      cell.className = 'downscaled-cell';
      downscaledContainer.appendChild(cell);
      downscaledCells.push(cell);
    }}

    // Build 10 probability bars for Draw & Test
    const drawProbRows = [];
    for (let k = 0; k < 10; k++) {{
      const item = document.createElement('div');
      item.className = 'prob-item';
      item.innerHTML = `
        <span class="prob-label">[${{k}}]</span>
        <div class="prob-track"><div class="prob-fill"></div></div>
        <span class="prob-val">0.0%</span>
      `;
      drawProbContainer.appendChild(item);
      drawProbRows.push({{
        item,
        fill: item.querySelector('.prob-fill'),
        val: item.querySelector('.prob-val')
      }});
    }}

    // Initialize Draw Canvas
    function clearDrawPad() {{
      drawCtx.fillStyle = '#000000';
      drawCtx.fillRect(0, 0, drawCanvas.width, drawCanvas.height);
      drawnNormalizedPixels.fill(0);
      for (let i = 0; i < 64; i++) downscaledCells[i].style.backgroundColor = '#000';
      document.getElementById('draw-big-digit').textContent = '?';
      document.getElementById('draw-confidence').textContent = 'Confidence: 0.0%';
      drawProbRows.forEach(r => {{
        r.fill.style.width = '0%';
        r.val.textContent = '0.0%';
        r.item.classList.remove('predicted');
      }});
    }}
    clearDrawPad();

    // Drawing stroke logic
    drawCtx.strokeStyle = '#ffffff';
    drawCtx.lineWidth = 15;
    drawCtx.lineCap = 'round';
    drawCtx.lineJoin = 'round';

    function getCanvasCoords(e) {{
      const rect = drawCanvas.getBoundingClientRect();
      const scaleX = drawCanvas.width / rect.width;
      const scaleY = drawCanvas.height / rect.height;
      if (e.touches && e.touches[0]) {{
        return {{
          x: (e.touches[0].clientX - rect.left) * scaleX,
          y: (e.touches[0].clientY - rect.top) * scaleY
        }};
      }}
      return {{
        x: (e.clientX - rect.left) * scaleX,
        y: (e.clientY - rect.top) * scaleY
      }};
    }}

    function startStroke(e) {{
      e.preventDefault();
      isDrawing = true;
      const {{ x, y }} = getCanvasCoords(e);
      drawCtx.beginPath();
      drawCtx.moveTo(x, y);
      drawCtx.lineTo(x, y);
      drawCtx.stroke();
      processDrawing();
    }}

    function moveStroke(e) {{
      if (!isDrawing) return;
      e.preventDefault();
      const {{ x, y }} = getCanvasCoords(e);
      drawCtx.lineTo(x, y);
      drawCtx.stroke();
      processDrawing();
    }}

    function endStroke() {{
      if (!isDrawing) return;
      isDrawing = false;
      processDrawing();
    }}

    drawCanvas.addEventListener('mousedown', startStroke);
    window.addEventListener('mousemove', moveStroke);
    window.addEventListener('mouseup', endStroke);

    drawCanvas.addEventListener('touchstart', startStroke, {{ passive: false }});
    window.addEventListener('touchmove', moveStroke, {{ passive: false }});
    window.addEventListener('touchend', endStroke);

    document.getElementById('btn-clear-draw').addEventListener('click', clearDrawPad);

    // Process drawn image: Bounding Box -> Crop & Center -> 8x8 Downsampling
    function processDrawing() {{
      const imgData = drawCtx.getImageData(0, 0, drawCanvas.width, drawCanvas.height);
      const data = imgData.data;
      const w = drawCanvas.width;
      const h = drawCanvas.height;

      let minX = w, maxX = 0, minY = h, maxY = 0;
      let hasPixels = false;

      for (let y = 0; y < h; y++) {{
        for (let x = 0; x < w; x++) {{
          const idx = (y * w + x) * 4;
          if (data[idx] > 30) {{ // red channel
            hasPixels = true;
            if (x < minX) minX = x;
            if (x > maxX) maxX = x;
            if (y < minY) minY = y;
            if (y > maxY) maxY = y;
          }}
        }}
      }}

      if (!hasPixels) {{
        clearDrawPad();
        return;
      }}

      // Create offscreen 8x8 canvas with centering
      const padW = maxX - minX + 1;
      const padH = maxY - minY + 1;
      const maxDim = Math.max(padW, padH);

      const off8 = document.createElement('canvas');
      off8.width = 8;
      off8.height = 8;
      const offCtx = off8.getContext('2d');
      offCtx.fillStyle = '#000';
      offCtx.fillRect(0, 0, 8, 8);

      // Fit into 6x6 area centered within 8x8 (1px margin)
      const scale = 6.0 / maxDim;
      const targetW = padW * scale;
      const targetH = padH * scale;
      const offsetX = 1.0 + (6.0 - targetW) / 2.0;
      const offsetY = 1.0 + (6.0 - targetH) / 2.0;

      // Draw cropped region onto 8x8 canvas
      offCtx.imageSmoothingEnabled = true;
      offCtx.drawImage(drawCanvas, minX, minY, padW, padH, offsetX, offsetY, targetW, targetH);

      const scaledData = offCtx.getImageData(0, 0, 8, 8).data;
      for (let i = 0; i < 64; i++) {{
        const lum = scaledData[i * 4] / 255.0;
        drawnNormalizedPixels[i] = lum;
        // Update downscaled preview
        const b = Math.round(lum * 255);
        downscaledCells[i].style.backgroundColor = `rgb(${{b}}, ${{b}}, ${{b}})`;
      }}

      updateDrawPredictions();
    }}

    function updateDrawPredictions() {{
      const {{ probs }} = nn.forwardSingle(drawnNormalizedPixels);
      let maxP = -1, pred = 0;
      for (let k = 0; k < 10; k++) {{
        if (probs[k] > maxP) {{ maxP = probs[k]; pred = k; }}
      }}

      document.getElementById('draw-big-digit').textContent = pred.toString();
      document.getElementById('draw-confidence').textContent = `Confidence: ${{(maxP * 100).toFixed(1)}}%`;

      for (let k = 0; k < 10; k++) {{
        const row = drawProbRows[k];
        const p = probs[k];
        const pct = (p * 100).toFixed(1) + '%';
        row.fill.style.width = pct;
        row.val.textContent = pct;
        row.item.classList.toggle('predicted', k === pred);
      }}
    }}

    // Feed to Studio button
    document.getElementById('btn-feed-to-studio').addEventListener('click', () => {{
      customStudioInput = new Float32Array(drawnNormalizedPixels);
      updateStudioUI();
      triggerPulse('forward');
      // Scroll to studio smoothly
      document.getElementById('studio-section').scrollIntoView({{ behavior: 'smooth' }});
    }});

    // Preset digit drawings
    document.querySelectorAll('.draw-preset').forEach(btn => {{
      btn.addEventListener('click', () => {{
        const digit = parseInt(btn.dataset.d, 10);
        // Find a representative sample from dataset
        let sampleIdx = 0;
        for (let s = 0; s < N; s++) {{
          if (Y_DATA[s] === digit) {{ sampleIdx = s; break; }}
        }}
        const pix = X_DATA.subarray(sampleIdx * 64, (sampleIdx + 1) * 64);
        
        // Draw onto 220x220 canvas
        drawCtx.fillStyle = '#000';
        drawCtx.fillRect(0, 0, 220, 220);
        for (let y = 0; y < 8; y++) {{
          for (let x = 0; x < 8; x++) {{
            const v = pix[y * 8 + x];
            if (v > 0.1) {{
              drawCtx.fillStyle = `rgba(255, 255, 255, ${{v}})`;
              drawCtx.beginPath();
              drawCtx.arc(x * 25 + 22, y * 25 + 22, 10, 0, Math.PI * 2);
              drawCtx.fill();
            }}
          }}
        }}
        processDrawing();
      }});
    }});

    // 13. CONFETTI & TOAST
    const confettiCanvas = document.getElementById('confetti-canvas');
    const confettiCtx = confettiCanvas.getContext('2d');
    let confettiParticles = [];
    let confettiActive = false;

    function resizeConfetti() {{
      confettiCanvas.width = window.innerWidth;
      confettiCanvas.height = window.innerHeight;
    }}
    window.addEventListener('resize', resizeConfetti);
    resizeConfetti();

    function fireConfetti() {{
      confettiParticles = [];
      const colors = ['#00f2fe', '#8b5cf6', '#ff007f', '#10b981', '#f59e0b', '#ffffff'];
      for (let i = 0; i < 120; i++) {{
        confettiParticles.push({{
          x: window.innerWidth * (0.2 + Math.random() * 0.6),
          y: window.innerHeight * 0.3,
          vx: (Math.random() - 0.5) * 12,
          vy: -Math.random() * 10 - 4,
          size: Math.random() * 7 + 4,
          color: colors[Math.floor(Math.random() * colors.length)],
          rotation: Math.random() * 360,
          vRot: (Math.random() - 0.5) * 12,
          alpha: 1.0
        }});
      }}
      confettiActive = true;
      runConfettiLoop();
    }}

    function runConfettiLoop() {{
      if (!confettiActive) return;
      confettiCtx.clearRect(0, 0, confettiCanvas.width, confettiCanvas.height);

      let alive = false;
      for (let p of confettiParticles) {{
        p.x += p.vx;
        p.y += p.vy;
        p.vy += 0.28; // gravity
        p.rotation += p.vRot;
        p.alpha -= 0.007;

        if (p.alpha > 0) {{
          alive = true;
          confettiCtx.save();
          confettiCtx.translate(p.x, p.y);
          confettiCtx.rotate((p.rotation * Math.PI) / 180);
          confettiCtx.globalAlpha = p.alpha;
          confettiCtx.fillStyle = p.color;
          confettiCtx.fillRect(-p.size / 2, -p.size / 2, p.size, p.size);
          confettiCtx.restore();
        }}
      }}

      if (alive) {{
        requestAnimationFrame(runConfettiLoop);
      }} else {{
        confettiActive = false;
        confettiCtx.clearRect(0, 0, confettiCanvas.width, confettiCanvas.height);
      }}
    }}

    function showMilestoneToast() {{
      const toast = document.getElementById('milestone-toast');
      toast.classList.add('show');
      setTimeout(() => {{
        toast.classList.remove('show');
      }}, 5000);
    }}

    // Copy Python Code Button
    document.getElementById('btn-copy-code').addEventListener('click', () => {{
      const rawCode = document.getElementById('raw-python-code').value;
      navigator.clipboard.writeText(rawCode).then(() => {{
        const btn = document.getElementById('btn-copy-code');
        const originalText = btn.textContent;
        btn.textContent = '✓ Copied!';
        btn.style.borderColor = '#10b981';
        btn.style.color = '#10b981';
        setTimeout(() => {{
          btn.textContent = originalText;
          btn.style.borderColor = '';
          btn.style.color = '';
        }}, 2000);
      }}).catch(err => {{
        console.error('Copy failed:', err);
      }});
    }});

    // Back to top button
    document.getElementById('btn-back-to-top').addEventListener('click', () => {{
      window.scrollTo({{ top: 0, behavior: 'smooth' }});
    }});

    // Nav Links Active State Tracking
    const navStudio = document.getElementById('nav-studio');
    const navDraw = document.getElementById('nav-draw');
    const navHow = document.getElementById('nav-how');

    window.addEventListener('scroll', () => {{
      const scrollY = window.scrollY;
      const drawTop = document.getElementById('draw-section').offsetTop - 100;
      const howTop = document.getElementById('how-it-works-section').offsetTop - 100;

      navStudio.classList.remove('active');
      navDraw.classList.remove('active');
      navHow.classList.remove('active');

      if (scrollY >= howTop) {{
        navHow.classList.add('active');
      }} else if (scrollY >= drawTop) {{
        navDraw.classList.add('active');
      }} else {{
        navStudio.classList.add('active');
      }}
    }});

    // INITIAL SETUP & BOOTSTRAP
    resizeCanvas();
    updateStudioUI();
    triggerPulse('forward');
    requestAnimationFrame(renderLoop);
    window.addEventListener('resize', resizeCanvas);

  }})();
  </script>
</body>
</html>
"""
    return html_code

print("Building complete single-file index.html...")
full_html = generate_html()

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(full_html)

print("Generated index.html successfully! Size:", len(full_html), "bytes.")
