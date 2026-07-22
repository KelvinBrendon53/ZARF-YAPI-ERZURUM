import streamlit as st
import pandas as pd


st.set_page_config(page_title="ZARF YAPI - PRO DASHBOARD", layout="wide")

st.markdown("""
    <style>
    .stApp { background-color: #161a27; color: #e0e0e0; }
    h1 { color: #FFD700; text-align: center; font-weight: 800; text-shadow: 1px 1px 2px rgba(0,0,0,0.3); }
    .card { background-color: #252936; padding: 20px; border-radius: 15px; border-left: 5px solid #FFD700; margin-bottom: 20px; }
    .yesil-imza { color: #00FF00; font-weight: bold; text-align: center; font-size: 18px; margin-top: 30px; }
    
    [data-testid="stDataFrame"] { background-color: #384056 !important; border: 1px solid #252936 !important; border-radius: 10px; }
    [data-testid="stDataFrame"] div[role="columnheader"] { background-color: #0e1117 !important; color: #FFD700 !important; font-weight: bold !important; }
    
    div.stButton > button { background-color: #FFD700 !important; color: #000080 !important; font-weight: bold; border-radius: 10px; width: 100%; border: none; }
    </style>
    """, unsafe_allow_html=True)

c1, c2, c3 = st.columns([1, 4, 1])
with c1: st.image("https://ffo3gv1cf3ir.merlincdn.net/SiteAssets/Hakkimizda/genel-bakis/logolarimiz/AMBLEM_SARI.jpg?20260716_03-135355", width=85)
with c2: st.markdown("<h1>ZARF YAPI ERZURUM</h1>", unsafe_allow_html=True)
with c3: st.image("https://zarfyapi.com/assets/logo.png", width=85)

DOSYA_ID = "1Kbzpbu-mxaXZmY52qXVoj0nxF_X4tO4l"
GID = "1034042521"
CSV_URL = f"https://docs.google.com/spreadsheets/d/{DOSYA_ID}/export?format=csv&gid={GID}"

@st.cache_data(ttl=10)
def load_data():
    df = pd.read_csv(CSV_URL).fillna("") 
    df = df.loc[:, ~df.columns.str.contains('^Unnamed')]
    
    # Binlik ayırıcıyı nokta (.) yapma operasyonu
    for col in df.columns:
        if any(kelime in col for kelime in ['STOK', 'GELEN', 'ÇIKIŞ']):
            def format_binlik(val):
                clean_val = str(val).replace('.', '').replace(',', '').strip()
                if clean_val.isdigit():
                    return f"{int(clean_val):,}".replace(',', '.')
                return val
            df[col] = df[col].apply(format_binlik)
            
    return df
            
df = load_data()

if not df.empty:
    st.markdown("<div class='card'><h3>📦 MEVCUT STOK DURUMU</h3></div>", unsafe_allow_html=True)
    st.dataframe(df.iloc[:, 0:4], use_container_width=True, height=400)
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    if len(df.columns) > 4:
        st.markdown("<div class='card'><h3>📋 TALEP VE SİPARİŞ TAKİBİ</h3></div>", unsafe_allow_html=True)
        st.dataframe(df.iloc[:, 4:], use_container_width=True, height=400)
else:
    st.error("Veri yüklenemedi!")

if st.button("🔄 VERİLERİ YENİLE"):
    st.cache_data.clear()
    st.rerun()

st.markdown("<p class='yesil-imza'>Kurucu: Muhammed Emin YILMAZ</p>", unsafe_allow_html=True)
