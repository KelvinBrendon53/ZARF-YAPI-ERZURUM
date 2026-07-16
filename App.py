import streamlit as st
import pandas as pd

st.title("📦 Zarf Yapı - Depo Stok")

DOSYA_ID = "https://docs.google.com/spreadsheets/d/1Kbzpbu-mxaXZmY52qXVoj0nxF_X4tO4l/edit?gid=1034042521#gid=1034042521"
CSV_URL = f"https://docs.google.com/spreadsheets/d/{DOSYA_ID}/export?format=csv&gid=0"

# Veriyi çek
try:
    df = pd.read_csv(CSV_URL)
    df = df.fillna(0)
    st.dataframe(df, use_container_width=True)
except Exception as e:
    st.error("Veri çekilirken bir hata oluştu. Lütfen Sheets dosyanızın 'Herkesle Paylaşılabilir' olduğundan emin olun.")
    st.write(e)
