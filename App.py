import streamlit as st
import pandas as pd
import time

# Sayfa ayarları (Tarayıcı sekmesinde düzgün görünmesi için)
st.set_page_config(page_title="Zarf Yapı | Depo", layout="wide")

# Modern Tasarım için CSS (Renkler: Zarf Yapı stili - Lacivert/Gri/Turuncu)
st.markdown("""
    <style>
    .stApp { background-color: #0e1117; }
    h1 { color: #FFA500; text-align: center; font-family: 'Arial Black'; }
    .stDataFrame { border: 2px solid #FFA500; border-radius: 10px; }
    div[data-testid="stMetricValue"] { color: #ffffff; }
    </style>
    """, unsafe_allow_html=True)

st.title("🏗️ ZARF YAPI - STOK TAKİP")

DOSYA_ID = "1Kbzpbu-mxaXZmY52qXVoj0nxF_X4tO4l"
GID = "1034042521"
CSV_URL = f"https://docs.google.com/spreadsheets/d/{DOSYA_ID}/export?format=csv&gid={GID}"

# Veri çekme fonksiyonu
@st.cache_data(ttl=10) # 10 saniyede bir veriyi taze tutar
def load_data():
    df = pd.read_csv(CSV_URL)
    return df.fillna(0)

# Ana ekran düzeni
col1, col2, col3 = st.columns([1, 6, 1])

with col2:
    try:
        df = load_data()
        
        # Mobil uyumlu olması için metinlerin net olması
        st.dataframe(df, use_container_width=True, height=500)
        
        # Küçük bir şık detay: Güncelleme butonu (Manuel kontrol daha karizmatik durur)
        if st.button("🔄 STOKLARI GÜNCELLE"):
            st.rerun()
            
    except Exception:
        st.error("⚠️ Sunucuya bağlanamadık. İnternet veya Link Ayarlarını kontrol et reis!")

st.markdown("---")
st.caption("© 2026 Zarf Yapı İnşaat Ltd. | Teknik Ofis Takip Sistemi")
