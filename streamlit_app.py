import streamlit as st
import streamlit.components.v1 as components

# Imposta la pagina a tutto schermo e rimuovi i margini di Streamlit
st.set_page_config(layout="wide", page_title="Alcol Finder")

# CSS per nascondere i margini interni di Streamlit e rendere l'iframe fluido
st.markdown("""
    <style>
        .main .block-container {
            padding: 0 !important;
            max-width: 100% !important;
        }
        iframe {
            display: block;
            border: none;
        }
    </style>
""", unsafe_allow_html=True)

with open("index.html", 'r', encoding='utf-8') as f:
    source_code = f.read()

# Usa 100vh (altezza visuale) per occupare tutto lo schermo disponibile
components.html(source_code, height=800) # L'altezza verrà gestita meglio via CSS o vh