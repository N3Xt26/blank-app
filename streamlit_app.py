import streamlit as st
import streamlit.components.v1 as components

# 1. Leggi il contenuto del file HTML
with open("index.html", 'r', encoding='utf-8') as f:
    source_code = f.read()

# 2. Renderizza l'HTML come componente
# Puoi regolare l'altezza (height) e se mostrare la barra di scorrimento (scrolling)
components.html(source_code, height=1080, scrolling=True)