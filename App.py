import streamlit as st
import pandas as pd

st.title("📦 Zarf Yapı - Depo Stok")

# Senin verdiğin linkteki ID ve GID numarası
DOSYA_ID = "1Kbzpbu-mxaXZmY52qXVoj0nxF_X4tO4l"
GID = "1034042521"

# CSV formatına çevrilmiş özel link
CSV_URL = f"https://docs.google.com/spreadsheets/d/{DOSYA_ID}/export?format=csv&gid={GID}"

try:
    # Veriyi çek
    df = pd.read_csv(CSV_URL)
    
    # Sayıların tam gözükmesi ve temizlenmesi için
    df = df.fillna(0)
    
    # Veriyi ekranda göster
    st.dataframe(df, use_container_width=True)
    
except Exception as e:
    st.error("Veri çekilemedi. Lütfen dosyanın 'Herkese açık' (Görüntüleyici) olduğundan emin ol.")
    st.write(f"Hata detayı: {e}")
