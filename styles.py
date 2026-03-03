"""
styles.py — All CSS for the SecureScan AI dark theme.
Imported by app.py to keep the main file clean.
"""

DARK_THEME_CSS = """
<style>
/* ===== FONTS ===== */
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800&family=JetBrains+Mono:wght@400;500;600&display=swap');

/* ===== GLOBAL ===== */
.stApp {
    background: linear-gradient(135deg, #0a0a0f 0%, #0d1117 50%, #0a0a0f 100%) !important;
    color: #e6edf3 !important;
    font-family: 'Inter', sans-serif !important;
}
#MainMenu, footer, header { visibility: hidden; }
::-webkit-scrollbar { width: 6px; }
::-webkit-scrollbar-track { background: #0d1117; }
::-webkit-scrollbar-thumb { background: #1a3a4a; border-radius: 3px; }

/* ===== SIDEBAR ===== */
section[data-testid="stSidebar"] {
    background: linear-gradient(180deg, #0d1117 0%, #080c12 100%) !important;
    border-right: 1px solid rgba(0, 255, 136, 0.1) !important;
}
section[data-testid="stSidebar"] .stMarkdown h1,
section[data-testid="stSidebar"] .stMarkdown h2,
section[data-testid="stSidebar"] .stMarkdown h3 { color: #e6edf3 !important; }
section[data-testid="stSidebar"] .stMarkdown p,
section[data-testid="stSidebar"] .stMarkdown li { color: #8b949e !important; }

/* ===== HERO ===== */
.hero-title {
    font-family: 'Inter', sans-serif; font-size: 2.8rem; font-weight: 800;
    background: linear-gradient(135deg, #00ff88, #00d4ff, #7b61ff);
    -webkit-background-clip: text; -webkit-text-fill-color: transparent;
    background-clip: text; text-align: center; margin-bottom: 0; letter-spacing: -1px;
}
.hero-subtitle {
    font-family: 'Inter', sans-serif; font-size: 1.05rem; color: #8b949e;
    text-align: center; margin-top: 4px; margin-bottom: 30px; letter-spacing: 0.5px;
}

/* ===== GLASS CARDS ===== */
.glass-card {
    background: rgba(13, 17, 23, 0.7); backdrop-filter: blur(20px);
    border: 1px solid rgba(0, 255, 136, 0.08); border-radius: 16px;
    padding: 24px; margin-bottom: 16px; transition: all 0.3s ease;
}
.glass-card:hover {
    border-color: rgba(0, 255, 136, 0.2);
    box-shadow: 0 0 30px rgba(0, 255, 136, 0.05);
}

/* ===== METRIC CARDS ===== */
.metric-card {
    background: rgba(13, 17, 23, 0.8); backdrop-filter: blur(16px);
    border: 1px solid rgba(255, 255, 255, 0.06); border-radius: 14px;
    padding: 20px 24px; text-align: center; transition: all 0.3s ease;
    position: relative; overflow: hidden;
}
.metric-card::before {
    content: ''; position: absolute; top: 0; left: 0; right: 0;
    height: 3px; border-radius: 14px 14px 0 0;
}
.metric-card:hover { transform: translateY(-2px); box-shadow: 0 8px 25px rgba(0,0,0,0.3); }
.metric-card .metric-value {
    font-family: 'JetBrains Mono', monospace; font-size: 2.2rem;
    font-weight: 700; margin: 8px 0 4px 0;
}
.metric-card .metric-label {
    font-size: 0.75rem; font-weight: 600; text-transform: uppercase;
    letter-spacing: 1.5px; color: #8b949e;
}
.metric-critical::before { background: linear-gradient(90deg, #ff4757, #ff6b81); }
.metric-critical .metric-value { color: #ff4757; }
.metric-high::before { background: linear-gradient(90deg, #ffa502, #ffbe76); }
.metric-high .metric-value { color: #ffa502; }
.metric-medium::before { background: linear-gradient(90deg, #00d4ff, #54e0ff); }
.metric-medium .metric-value { color: #00d4ff; }
.metric-total::before { background: linear-gradient(90deg, #00ff88, #7bffbf); }
.metric-total .metric-value { color: #00ff88; }

/* ===== BADGES ===== */
.badge { display: inline-block; padding: 4px 12px; border-radius: 20px; font-size: 0.7rem; font-weight: 700; letter-spacing: 1px; text-transform: uppercase; }
.badge-critical { background: rgba(255,71,87,0.15); color: #ff4757; border: 1px solid rgba(255,71,87,0.3); }
.badge-high { background: rgba(255,165,2,0.15); color: #ffa502; border: 1px solid rgba(255,165,2,0.3); }
.badge-medium { background: rgba(0,212,255,0.15); color: #00d4ff; border: 1px solid rgba(0,212,255,0.3); }
.badge-low { background: rgba(0,255,136,0.15); color: #00ff88; border: 1px solid rgba(0,255,136,0.3); }

/* ===== FINDING CARDS ===== */
.finding-card {
    background: rgba(22, 27, 34, 0.8); border: 1px solid rgba(255,255,255,0.04);
    border-radius: 12px; padding: 18px 22px; margin-bottom: 10px;
    border-left: 3px solid; transition: all 0.2s ease;
}
.finding-card:hover { background: rgba(30, 37, 46, 0.9); }
.finding-card.sev-Critical { border-left-color: #ff4757; }
.finding-card.sev-High { border-left-color: #ffa502; }
.finding-card.sev-Medium { border-left-color: #00d4ff; }
.finding-card.sev-Low { border-left-color: #00ff88; }
.finding-title { font-weight: 600; font-size: 1rem; color: #e6edf3; margin-bottom: 6px; }
.finding-desc { font-size: 0.85rem; color: #8b949e; margin-bottom: 8px; }
.finding-match {
    font-family: 'JetBrains Mono', monospace; font-size: 0.78rem;
    background: rgba(0,0,0,0.4); padding: 6px 12px; border-radius: 6px;
    color: #ff6b81; margin: 3px 0; word-break: break-all;
    border: 1px solid rgba(255,255,255,0.04);
}

/* ===== REMEDIATION ===== */
.remediation-box {
    background: rgba(0,255,136,0.04); border: 1px solid rgba(0,255,136,0.12);
    border-radius: 12px; padding: 20px 24px; margin-top: 16px;
}
.remediation-box h4 { color: #00ff88; margin-bottom: 12px; }
.remediation-box p { color: #b0bec5; font-size: 0.9rem; margin: 6px 0; }

/* ===== BUTTONS ===== */
.stButton > button {
    background: linear-gradient(135deg, #00ff88, #00d4ff) !important;
    color: #0a0a0f !important; font-weight: 700 !important; font-size: 1rem !important;
    border: none !important; border-radius: 12px !important; padding: 12px 24px !important;
    letter-spacing: 0.5px !important; transition: all 0.3s ease !important;
}
.stButton > button:hover {
    box-shadow: 0 0 30px rgba(0,255,136,0.3) !important;
    transform: translateY(-1px) !important;
}

/* ===== INPUTS ===== */
.stTextArea textarea, .stTextInput input {
    background: rgba(13,17,23,0.9) !important;
    border: 1px solid rgba(0,255,136,0.1) !important; border-radius: 10px !important;
    color: #e6edf3 !important; font-family: 'JetBrains Mono', monospace !important;
    font-size: 0.85rem !important;
}
.stTextArea textarea:focus, .stTextInput input:focus {
    border-color: rgba(0,255,136,0.3) !important;
    box-shadow: 0 0 15px rgba(0,255,136,0.05) !important;
}
section[data-testid="stFileUploader"] {
    background: rgba(13,17,23,0.6) !important;
    border: 2px dashed rgba(0,255,136,0.15) !important;
    border-radius: 12px !important; padding: 12px !important;
}
section[data-testid="stFileUploader"]:hover { border-color: rgba(0,255,136,0.3) !important; }

/* ===== MISC ===== */
.streamlit-expanderHeader { background: rgba(22,27,34,0.8) !important; border-radius: 10px !important; color: #e6edf3 !important; font-weight: 600 !important; }
hr { border-color: rgba(255,255,255,0.05) !important; }
.scan-phase { font-family: 'JetBrains Mono', monospace; font-size: 0.85rem; color: #00ff88; padding: 4px 0; }
.status-dot { display: inline-block; width: 8px; height: 8px; border-radius: 50%; margin-right: 8px; animation: pulse 2s ease-in-out infinite; }
@keyframes pulse { 0%, 100% { opacity: 0.4; } 50% { opacity: 1; box-shadow: 0 0 8px currentColor; } }
.sidebar-stat { background: rgba(22,27,34,0.6); border: 1px solid rgba(255,255,255,0.04); border-radius: 10px; padding: 12px 16px; margin-bottom: 8px; text-align: center; }
.sidebar-stat .stat-val { font-family: 'JetBrains Mono', monospace; font-size: 1.4rem; font-weight: 700; color: #00ff88; }
.sidebar-stat .stat-label { font-size: 0.7rem; color: #8b949e; text-transform: uppercase; letter-spacing: 1px; }
.history-row { background: rgba(22,27,34,0.6); border: 1px solid rgba(255,255,255,0.04); border-radius: 10px; padding: 14px 20px; margin-bottom: 8px; display: flex; align-items: center; justify-content: space-between; }
.history-row:hover { background: rgba(30,37,46,0.8); }
.stMarkdown p, .stMarkdown li { color: #b0bec5; }
h1, h2, h3, h4 { color: #e6edf3 !important; }
</style>
"""
