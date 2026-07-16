import streamlit as st
import pandas as pd

# Sayfa Ayarları
st.set_page_config(page_title="ZARF YAPI - PRO DASHBOARD", layout="wide")

# CSS: Dinamik Mod Desteği
st.markdown("""
    <style>
    /* Koyu mod teması */
    .stApp.dark { background-color: #161a27; color: #e0e0e0; }
    .stApp.light { background-color: #f8f9fa; color: #0e1117; }
    
    h1 { color: #FFD700; text-align: center; font-weight: 800; }
    
    /* Kartlar */
    .card { background-color: #252936; padding: 20px; border-radius: 15px; border-left: 5px solid #FFD700; margin-bottom: 20px; }
    
    /* Butonlar */
    div.stButton > button { background-color: #FFD700 !important; color: #000080 !important; font-weight: bold; border-radius: 10px; width: 100%; }
    </style>
    """, unsafe_allow_html=True)

# Session State ile Modu Kaydetme
if 'mod' not in st.session_state:
    st.session_state.mod = 'dark'

def toggle_mod():
    st.session_state.mod = 'light' if st.session_state.mod == 'dark' else 'dark'

# Sayfa Rengini Uygula
st.markdown(f'<div class="stApp {st.session_state.mod}">', unsafe_allow_html=True)

# Başlık ve Logolar
c1, c2, c3 = st.columns([1, 4, 1])
with c1: st.image("https://cdn-icons-png.flaticon.com/512/3652/3652613.png", width=70)
with c2: st.markdown("<h1>ZARF YAPI ERZURUM</h1>", unsafe_allow_html=True)
with c3: 
    # Mod değiştirme butonu
    if st.button("🌓 MOD DEĞİŞTİR"):
        toggle_mod()
        st.rerun()

# Veri İşlemleri
DOSYA_ID = "1Kbzpbu-mxaXZmY52qXVoj0nxF_X4tO4l"
GID = "1034042521"
CSV_URL = f"https://docs.google.com/spreadsheets/d/{DOSYA_ID}/export?format=csv&gid={GID}"

@st.cache_data(ttl=10)
def load_data():
    df = pd.read_csv(CSV_URL).fillna(0)
    return df.loc[:, ~df.columns.str.contains('^Unnamed')]

df = load_data()

# Tablolar
st.markdown("<div class='card'><h3>📦 MEVCUT STOK DURUMU</h3></div>", unsafe_allow_html=True)
st.dataframe(df.iloc[:, 0:4], use_container_width=True)

st.markdown("<br><br>", unsafe_allow_html=True)

st.markdown("<div class='card'><h3>📋 TALEP VE SİPARİŞ TAKİBİ</h3></div>", unsafe_allow_html=True)
st.dataframe(df.iloc[:, 4:], use_container_width=True)

if st.button("🔄 VERİLERİ YENİLE"):
    st.cache_data.clear()
    st.rerun()

st.markdown("</div>", unsafe_allow_html=True) # Kapanış Divi
