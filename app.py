import streamlit as st
from ui.prediction_ui import render_prediction_ui
from ui.training_ui import render_training_ui

def load_css():
    st.markdown("""
    <style>

    /* ===== IMPORT ROBOTO FONT ===== */
    @import url('https://fonts.googleapis.com/css2?family=Roboto:wght@300;400;500;700&display=swap');

    /* ===== GLOBAL FONT ===== */
    html, body, [class*="css"] {
        font-family: 'Roboto', sans-serif !important;
    }

    .stApp {
        background: radial-gradient(circle at top, #0f172a, #020617);
        color: #f8fafc;
        font-family: 'Roboto', sans-serif;
    }

    h1, h2, h3 {
        font-weight: 600;
        letter-spacing: 0.4px;
    }

    /* -------- GLASS CARD -------- */
    .card {
        background: rgba(255,255,255,0.06);
        backdrop-filter: blur(14px);
        border-radius: 20px;
        padding: 26px;
        margin-bottom: 26px;
        box-shadow: 0 12px 32px rgba(0,0,0,0.45);
    }

    .card:empty {
        display: none !important;
    }

    /* -------- BUTTON -------- */
    .stButton > button {
        font-family: 'Roboto', sans-serif;
        background: linear-gradient(90deg, #ff4b2b, #ff416c);
        color: white;
        border-radius: 16px;
        padding: 0.7em 1.6em;
        border: none;
        font-size: 16px;
        font-weight: 500;
        transition: all 0.3s ease;
    }

    .stButton > button:hover {
        transform: scale(1.06);
        box-shadow: 0 10px 30px rgba(255,65,108,0.45);
    }

    /* ===== ENHANCED FILE UPLOADER ===== */
    section[data-testid="stFileUploader"] {
        width: 100%;
    }

    section[data-testid="stFileUploader"] 
    div[data-testid="stFileUploaderDropzone"] {
        min-height: 160px;
        padding: 32px 28px;
        border-radius: 20px;
        background: rgba(255,255,255,0.06);
        border: 2px dashed rgba(255,255,255,0.25);
        transition: all 0.25s ease-in-out;
    }

    section[data-testid="stFileUploader"] 
    div[data-testid="stFileUploaderDropzone"]:hover {
        border-color: #ff4b6e;
        box-shadow: 0 0 0 1px rgba(255,75,110,0.4),
                    0 0 24px rgba(255,75,110,0.25);
    }

    section[data-testid="stFileUploader"][aria-disabled="true"]
    div[data-testid="stFileUploaderDropzone"] {
        opacity: 0.55;
        cursor: not-allowed;
        box-shadow: none;
        border-color: rgba(255,255,255,0.12);
    }

    section[data-testid="stFileUploader"] svg {
        width: 52px;
        height: 52px;
    }

    section[data-testid="stFileUploader"] button {
        font-family: 'Roboto', sans-serif;
        font-size: 15px;
        padding: 0.6em 1.5em;
        border-radius: 12px;
    }

    section[data-testid="stFileUploader"] label {
        font-weight: 600;
        letter-spacing: 0.3px;
    }

    section[data-testid="stFileUploader"] small {
        font-size: 13px;
        opacity: 0.75;
    }

    hr {
        display: none;
    }

    </style>
    """, unsafe_allow_html=True)


st.set_page_config(
    page_title="Rare Disease AI Platform",
    layout="wide",
    initial_sidebar_state="collapsed"
)

load_css()

st.markdown("<h1>🧬 Generative AI–Driven Rare Disease Platform</h1>", unsafe_allow_html=True)
st.markdown(
    "A scalable, intelligent framework for rare disease diagnosis and synthetic data generation."
)

tab1, tab2 = st.tabs(["🔍 Prediction", "🧪 Training"])

with tab1:
    render_prediction_ui()

with tab2:
    render_training_ui()
