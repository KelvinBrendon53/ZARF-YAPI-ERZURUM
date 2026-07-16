import streamlit as st
import pandas as pd

# Sayfa Ayarları
st.set_page_config(page_title="ERZURUM", layout="wide")

# CSS: YUMUŞAK KOYU MOD VE RENKLİ BAŞLIKLAR
st.markdown("""
    <style>
    /* Genel Arka Plan (Daha yumuşak bir koyu ton) */
    .stApp { background-color: #161a27; color: #e0e0e0; }
    
    /* Ana Başlıklar */
    h1 { color: #FFD700; text-align: center; font-weight: 800; text-shadow: 1px 1px 2px rgba(0,0,0,0.3); }
    
    /* Kart Tasarımları */
    .card { 
        background-color: #252936; 
        padding: 20px; 
        border-radius: 15px; 
        border-left: 5px solid #FFD700; 
        margin-bottom: 20px; 
        box-shadow: 0 4px 6px rgba(0,0,0,0.3);
    }
    
    /* TABLE / DATAFRAME STİLİ (JİLET GİBİ OKUMA) */
    /* Tablo gövdesi rengi */
    [data-testid="stDataFrame"] {
        background-color: #252936 !important;
        border: 1px solid #384056 !important;
        border-radius: 10px;
    }
    
    /* TABLO BAŞLIKLARI (SİYAH ZEMİN, SARI YAZI - SOLUKLUĞA SON) */
    [data-testid="stDataFrame"] div[role="columnheader"] {
        background-color: #0e1117 !important; /* Kapkara başlık zemini */
        color: #FFD700 !important;          /* Parlak sarı yazı */
        font-weight: bold !important;        /* Kalın */
        font-size: 14px !important;          /* Telefonda okunur boyutta */
        border-bottom: 2px solid #384056 !important;
    }
    
    /* Tablo içindeki metinler */
    [data-testid="stDataFrame"] div[role="gridcell"] {
        color: #e0e0e0 !important;
        font-size: 13px !important;
        border-bottom: 1px solid #384056 !important;
    }
    
    /* Butonlar (Turkcell Stili) */
    div.stButton > button { 
        background-color: #FFD700 !important; 
        color: #000080 !important; 
        font-weight: bold; 
        border-radius: 10px; 
        width: 100%; 
        border: none;
        box-shadow: 0 2px 4px rgba(0,0,0,0.2);
    }
    div.stButton > button:hover { background-color: #ffe066 !important; }
    
    </style>
    """, unsafe_allow_html=True)

# Başlık ve Logolar
c1, c2, c3 = st.columns([1, 4, 1])
with c1: st.image("https://ffo3gv1cf3ir.merlincdn.net/SiteAssets/Hakkimizda/genel-bakis/logolarimiz/AMBLEM_SARI.jpg?20260716_03-135355", width=85)
with c2: st.markdown("<h1>ZARF YAPI ERZURUM</h1>", unsafe_allow_html=True)
with c3: st.image("https://zarfyapi.com/assets/logo.png", width=85)

# Veri İşlemleri
DOSYA_ID = "1Kbzpbu-mxaXZmY52qXVoj0nxF_X4tO4l"
GID = "1034042521"
CSV_URL = f"https://docs.google.com/spreadsheets/d/{DOSYA_ID}/export?format=csv&gid={GID}"

@st.cache_data(ttl=10)
def load_data():
    try:
        df = pd.read_csv(CSV_URL).fillna(0)
        # İsimsiz sütunları temizle
        df = df.loc[:, ~df.columns.str.contains('^Unnamed')]
        return df
    except Exception:
        return pd.DataFrame({"Durum": ["Hata! Bağlantı kontrol et."] })

df = load_data()

# TABLO 1: STOK DURUMU
st.markdown("<div class='card'><h3>📦 MEVCUT STOK DURUMU</h3></div>", unsafe_allow_html=True)
# İlk 4 sütun
st.dataframe(df.iloc[:, 0:4], use_container_width=True, height=400)

st.markdown("<br><br>", unsafe_allow_html=True)

# TABLO 2: SİPARİŞ TAKİBİ
st.markdown("<div class='card'><h3>📋 TALEP VE SİPARİŞ TAKİBİ</h3></div>", unsafe_allow_html=True)
# Kalan sütunlar
st.dataframe(df.iloc[:, 4:], use_container_width=True, height=400)

# Güncelleme
if st.button("🔄 VERİLERİ YENİLE"):
    st.cache_data.clear()
    st.rerun()

st.markdown("<p class='yesil-imza'>Kurucu: Muhammed Emin YILMAZ</p>", unsafe_allow_html=True)
