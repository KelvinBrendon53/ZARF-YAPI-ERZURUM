import streamlit as st
import pandas as pd

st.title("📦 Zarf Yapı - Depo Stok")

# Google Sheets'ten veriyi çekmek için tek ve net link
# Lütfen şu satırı dosyanın en üstüne aynen kopyala
CSV_URL = "https://docs.google.com/spreadsheets/d/1Kbzpbu-mxaXZmY52qXVoj0nxF_X4tO4l/edit?gid=1034042521#gid=1034042521" 

try:
    # Veriyi çekiyoruz
    df = pd.read_csv(CSV_URL)
    
    # Sayısal hataları (nan) 0 ile dolduruyoruz
    df = df.fillna(0)
    
    # Tabloyu ekranda göster
    st.dataframe(df, use_container_width=True)
    
except Exception as e:
    st.error("Veri alınamadı. Lütfen dosyanın 'Herkesle Paylaşılabilir' olduğundan emin ol.")
