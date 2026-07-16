import streamlit as st
import pandas as pd

# Sayfa Ayarları
st.set_page_config(page_title="Zarf Yapı Erzurum - MAXX", layout="wide")

# CSS: Siyah tablo, parlayan sarı detaylar ve mobil uyum
st.markdown("""
    <style>
    /* Arka planı koyu yap */
    .stApp { background-color: #0e1117; color: white; }
    
    /* Tabloyu siyah yap ve kenarlarını parlat */
    [data-testid="stDataFrame"] {
        background-color: #1a1c22 !important;
        border: 1px solid #FFD700 !important;
        border-radius: 10px;
    }
    
    /* Başlık ve Logolar */
    .header-style { 
        background: #1a1c22; 
        padding: 15px; 
        border-bottom: 3px solid #FFD700;
        text-align: center;
        border-radius: 15px;
    }
    
    /* Butonlar */
    div.stButton > button {
        background-color: #FFD700 !important;
        color: #000080 !important;
        font-weight: 800;
        width: 100%;
        border-radius: 10px;
    }
    </style>
    """, unsafe_allow_html=True)

# Başlık ve Çift Logo Satırı
st.markdown("<div class='header-style'>", unsafe_allow_html=True)
c1, c2, c3 = st.columns([1, 4, 1])

with c1:
    
    st.image("https://ffo3gv1cf3ir.merlincdn.net/SiteAssets/Hakkimizda/genel-bakis/logolarimiz/AMBLEM_SARI.jpg?20260716_03-135355", width=60)
with c2:
    st.markdown("<h1>ZARF YAPI ERZURUM<br><small style='color: #FFD700;'>STOK TAKİP</small></h1>", unsafe_allow_html=True)
with c3:
  
    st.image("C:\Users\muham\Downloads\logo.webp", width=60)
    
st.markdown("</div>", unsafe_allow_html=True)

# Veri
DOSYA_ID = "1Kbzpbu-mxaXZmY52qXVoj0nxF_X4tO4l"
GID = "1034042521"
CSV_URL = f"https://docs.google.com/spreadsheets/d/{DOSYA_ID}/export?format=csv&gid={GID}"

@st.cache_data(ttl=10)
def load_data():
    return pd.read_csv(CSV_URL).fillna(0)

# Tablo
df = load_data()
st.dataframe(df, use_container_width=True, height=600)

# Buton
if st.button("🔄 SİSTEMİ GÜNCELLE"):
    st.cache_data.clear()
    st.rerun()
