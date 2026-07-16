import streamlit as st
import pandas as pd

st.title("📦 Zarf Yapı - Depo Stok")

# Dosya ID'niz (Linkteki o uzun kod)
DOSYA_ID = "https://docs.google.com/spreadsheets/d/1Kbzpbu-mxaXZmY52qXVoj0nxF_X4tO4l/edit?gid=1034042521#gid=1034042521"

# GID değeri: Sayfanın ID'si. 
# Eğer hata alırsan tarayıcıda "STOK LİSTESİ" sekmesine tıkla, 
# adres çubuğunun en sonunda #gid= ile başlayan sayı neyse onu buraya yaz.
# Genelde ilk sayfa 0'dır, ama emin olalım:
GID = "1" 

CSV_URL = f"https://docs.google.com/spreadsheets/d/{DOSYA_ID}/export?format=csv&gid={1034042521}"

try:
    df = pd.read_csv(CSV_URL)
    
    # Boş hücreleri temizle
    df = df.fillna(0)
    
    # "STOK LİSTESİ" verilerini göster
    st.dataframe(df, use_container_width=True)
    
except Exception as e:
    st.write("Veri yüklenemedi. Lütfen 'Web'de Yayınla'dan CSV olarak yayınladığınızdan emin olun.")
