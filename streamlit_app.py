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
        /* Nasconde header, footer e menu */
        header, footer, .stAppDeployButton, #MainMenu {visibility: hidden; display: none;}
        
        /* Rimuove padding e margini del contenitore principale */
        .main .block-container {
            padding: 0px !important;
            margin: 0px !important;
            max-width: 100% !important;
            height: 100vh !important;
        }

        /* Forza l'iframe a occupare tutto lo spazio senza bordi */
        iframe {
            position: fixed;
            top: 0;
            left: 0;
            width: 100vw !important;
            height: 100vh !important;
            border: none;
            margin: 0;
            padding: 0;
            overflow: hidden;
            z-index: 999999;
        }
        
        /* Nasconde eventuali scrollbar di Streamlit */
        .stApp {
            overflow: hidden;
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