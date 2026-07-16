import streamlit as st
import pandas as pd

# Sayfa Ayarları
st.set_page_config(page_title="ZARF YAPI - PRO DASHBOARD", layout="wide")

# CSS: Karanlık Mod ve Modern Kart Tasarımı
st.markdown("""
    <style>
    .stApp { background-color: #0e1117; }
    h1 { color: #FFD700; text-align: center; font-weight: 800; }
    .card { background-color: #1a1c22; padding: 20px; border-radius: 15px; border-left: 5px solid #FFD700; margin-bottom: 20px; }
    [data-testid="stDataFrame"] { border: 2px solid #333; border-radius: 10px; }
    div.stButton > button { background-color: #FFD700 !important; color: #000080 !important; font-weight: bold; border-radius: 10px; width: 100%; }
    </style>
    """, unsafe_allow_html=True)

# Başlık ve Logolar
c1, c2, c3 = st.columns([1, 4, 1])
with c1: st.image("https://cdn-icons-png.flaticon.com/512/3652/3652613.png", width=70)
with c2: st.markdown("<h1>ZARF YAPI ERZURUM</h1>", unsafe_allow_html=True)
with c3: st.image("https://cdn-icons-png.flaticon.com/512/2829/2829562.png", width=70)

# Veri İşlemleri
DOSYA_ID = "1Kbzpbu-mxaXZmY52qXVoj0nxF_X4tO4l"
GID = "1034042521"
CSV_URL = f"https://docs.google.com/spreadsheets/d/{DOSYA_ID}/export?format=csv&gid={GID}"

@st.cache_data(ttl=10)
def load_data():
    df = pd.read_csv(CSV_URL).fillna(0)
    # İsimsiz sütunları temizle
    df = df.loc[:, ~df.columns.str.contains('^Unnamed')]
    return df

df = load_data()

# TABLO 1: STOK DURUMU
st.markdown("<div class='card'><h3>📦 MEVCUT STOK DURUMU</h3></div>", unsafe_allow_html=True)
st.dataframe(df.iloc[:, 0:4], use_container_width=True)

st.markdown("<br><br>", unsafe_allow_html=True) # İki tablo arasına sağlam boşluk

# TABLO 2: TALEP VE SİPARİŞ
st.markdown("<div class='card'><h3>📋 TALEP VE SİPARİŞ TAKİBİ</h3></div>", unsafe_allow_html=True)
st.dataframe(df.iloc[:, 4:], use_container_width=True)

# Güncelleme
if st.button("🔄 VERİLERİ YENİLE"):
    st.cache_data.clear()
    st.rerun()

st.caption("© 2026 Zarf Yapı Erzurum | Teknik Ofis | Fiber Proje Takip Sistemi")
