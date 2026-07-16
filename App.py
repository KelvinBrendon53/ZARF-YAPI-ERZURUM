import streamlit as st
import pandas as pd
import time

st.title("📦 Zarf Yapı - Depo Stok")

DOSYA_ID = "1Kbzpbu-mxaXZmY52qXVoj0nxF_X4tO4l"
GID = "1034042521"
CSV_URL = f"https://docs.google.com/spreadsheets/d/{DOSYA_ID}/export?format=csv&gid={GID}"

# Veriyi çeken fonksiyon
def veri_cek():
    df = pd.read_csv(CSV_URL)
    return df.fillna(0)

# Sayfaya bir "placeholder" (yer tutucu) koyuyoruz
placeholder = st.empty()

# Sonsuz döngü (her 5 saniyede bir yeniler)
while True:
    try:
        data = veri_cek()
        with placeholder.container():
            st.dataframe(data, use_container_width=True)
            st.write(f"Son güncelleme: {time.strftime('%H:%M:%S')}")
        
        time.sleep(5) # 5 saniye bekle
        
    except Exception as e:
        st.error("Veri çekilemedi. Lütfen bağlantı ayarlarını kontrol edin.")
        break
