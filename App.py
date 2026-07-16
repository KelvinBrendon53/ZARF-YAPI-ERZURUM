import streamlit as st
import pandas as pd

st.title("📦 STOK LİSTESİ")

# Sadece Google Sheets URL'ini yapıştır
SHEET_URL = "https://docs.google.com/spreadsheets/d/1Kbzpbu-mxaXZmY52qXVoj0nxF_X4tO4l/edit?gid=1034042521#gid=1034042521"

# Veriyi oku (API anahtarı gerekmez)
df = pd.read_csv(SHEET_URL.replace("/edit?gid=0#gid=0", "/export?format=csv&gid=0"))

st.write("Mevcut Stok Durumun:")
st.dataframe(df)
