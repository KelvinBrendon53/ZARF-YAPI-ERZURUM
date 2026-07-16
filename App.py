import streamlit as st
import pandas as pd

# Sayfa Ayarları
st.set_page_config(page_title="Zarf Yapı Erzurum - Stok", layout="wide")

# CSS ile "MAXX" Tasarım (Turkcell ve Fiber Estetiği)
st.markdown("""
    <style>
    .stApp { background-color: #f8f9fa; }
    /* Başlık Bölgesi */
    .title-box { 
        background: linear-gradient(90deg, #FFD700 0%, #000080 100%); 
        padding: 20px; 
        border-radius: 15px; 
        text-align: center;
        color: white;
        margin-bottom: 20px;
    }
    /* Tablo Çerçevesi */
    .stDataFrame { border: 2px solid #000080; border-radius: 10px; }
    /* Buton Tasarımı */
    div.stButton > button {
        background-color: #FFD700 !important;
        color: #000080 !important;
        font-weight: bold;
        width: 100%;
        border-radius: 10px;
    }
    </style>
    """, unsafe_allow_html=True)

# Logo ve Başlık (Turkcell/Fiber Teması)
col_logo, col_title = st.columns([1, 4])
with col_logo:
    # İnternetten şık bir fiber/internet ikonu çekiyoruz
    st.image("https://cdn-icons-png.flaticon.com/512/3652/3652613.png", width=100)
with col_title:
    st.markdown("<div class='title-box'><h1>ZARF YAPI ERZURUM<br>STOK TAKİP</h1></div>", unsafe_allow_html=True)

# Veri İşlemleri
DOSYA_ID = "1Kbzpbu-mxaXZmY52qXVoj0nxF_X4tO4l"
GID = "1034042521"
CSV_URL = f"https://docs.google.com/spreadsheets/d/{DOSYA_ID}/export?format=csv&gid={GID}"

@st.cache_data(ttl=10)
def load_data():
    df = pd.read_csv(CSV_URL)
    return df.fillna(0)

# Gövde
df = load_data()
st.dataframe(df, use_container_width=True)

# Güncelleme Butonu
if st.button("🔄 VERİLERİ YENİLE"):
    st.cache_data.clear()
    st.rerun()

st.markdown("---")
st.markdown("🚀 **Zarf Yapı Erzurum - Fiber Optik Stok Yönetimi**")
