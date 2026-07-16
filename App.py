import streamlit as st
import pandas as pd

st.title("📦 STOK LİSTESİ")

# Sadece Google Sheets URL'ini yapıştır
SHEET_URL = "https://docs.google.com/spreadsheets/d/1Kbzpbu-mxaXZmY52qXVoj0nxF_X4tO4l/edit?usp=sharing&ouid=113342756401026466437&rtpof=true&sd=true"

# Veriyi oku (API anahtarı gerekmez)
df = pd.read_csv(SHEET_URL.replace("/edit?gid=0#gid=0", "/export?format=csv&gid=0"))

df = pd.read_csv(csv_url)
df = df.fillna(0) 

# Tabloyu ekranda göster
st.dataframe(df, use_container_width=True)
