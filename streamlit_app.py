import streamlit as st
import streamlit.components.v1 as components

# Configurazione pagina per rimuovere padding eccessivi (opzionale)
st.set_page_config(layout="wide")

# 1. Leggi il file HTML
with open("index.html", 'r', encoding='utf-8') as f:
    source_code = f.read()

components.html(source_code, height=None, scrolling=False)