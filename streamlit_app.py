import streamlit as st
import streamlit.components.v1 as components

# 1. Configurazione totale
st.set_page_config(
    page_title="Alcol Finder",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# 2. CSS Massiccio per azzerare Streamlit
st.markdown("""
    <style>
        /* Nasconde tutto: Menu, Footer, Header e i pulsanti di gestione (profilo/coroncina) */
        header, footer, .stAppDeployButton, #MainMenu, .stActionButton, .stToolbar, #stDecoration {
            visibility: hidden;
            display: none !important;
        }
        
        /* Rimuove ogni spazio bianco intorno al contenuto */
        .main .block-container {
            padding: 0px !important;
            margin: 0px !important;
            max-width: 100% !important;
            height: 100vh !important;
        }

        /* L'iframe diventa il padrone assoluto dello schermo */
        iframe {
            position: fixed;
            top: 0;
            left: 0;
            width: 100vw !important;
            height: 100vh !important;
            border: none;
            z-index: 999999;
        }

        /* Impedisce lo scroll della pagina "contenitore" di Streamlit */
        .stApp {
            overflow: hidden;
            background-color: transparent;
        }
    </style>
""", unsafe_allow_html=True)

# 3. Caricamento e rendering
try:
    with open("index.html", 'r', encoding='utf-8') as f:
        source_code = f.read()
    
    # L'altezza qui è di sicurezza, il CSS sopra comanda
    components.html(source_code, height=2000) 
except FileNotFoundError:
    st.error("File index.html non trovato! Assicurati che sia nella stessa cartella.")