import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

st.subheader("🔬 1. Simulasi Spektrum UV-Vis (λ Maksimal)")
st.markdown("Masukkan data panjang gelombang dan absorbansi:")

contoh_data = "250,0.18\n300,0.45\n350,0.60\n400,0.40\n450,0.25"
input_uvvis = st.text_area("Atau masukkan data manual (λ [nm], Absorbansi)", contoh_data, height=150)
uploaded_file = st.file_uploader("Atau unggah file CSV untuk spektrum", type=["csv"], key="file_spektrum")

df_uv = None
if uploaded_file is not None:
    try:
        df_uv = pd.read_csv(uploaded_file)
        if df_uv.shape[1] != 2:
            st.warning("File harus memiliki 2 kolom: panjang gelombang dan absorbansi")
            df_uv = None
    except Exception as e:
        st.error(f"Format file salah: {e}")
elif input_uvvis:
    try:
        lines = input_uvvis.strip().split('\n')
        data = [tuple(map(float, line.split(','))) for line in lines]
        df_uv = pd.DataFrame(data, columns=["Panjang Gelombang (nm)", "Absorbansi"])
    except Exception as e:
        st.error(f"Gagal membaca data teks: {e}")

if df_uv is not None:
    idx_max = df_uv["Absorbansi"].idxmax()
    lambda_max = df_uv.loc[idx_max, "Panjang Gelombang (nm)"]
    st.success(f"λ maks terdeteksi pada: *{lambda_max} nm*")

    warna_garis = st.color_picker("Pilih warna garis spektrum", "#000000")
    overlay = st.checkbox("Tampilkan spektrum referensi? (simulasi)")

    fig, ax = plt.subplots()
    ax.plot(df_uv["Panjang Gelombang (nm)"], df_uv["Absorbansi"], color=warna_garis, label='Spektrum Sampel')
    ax.axvline(lambda_max, color='red', linestyle='--', label=f'λ maks = {lambda_max} nm')

    if overlay:
        ref_lambda = df_uv["Panjang Gelombang (nm)"]
        ref_abs = np.interp(ref_lambda, ref_lambda, df_uv["Absorbansi"]) * 0.8
        ax.plot(ref_lambda, ref_abs, color='gray', linestyle=':', label='Referensi')

    ax.set_xlabel("Panjang Gelombang (nm)")
    ax.set_ylabel("Absorbansi")
    ax.set_title("Spektrum UV-Vis")
    ax.legend()
    st.pyplot(fig)


elif menu == "🧪 Kromatografi":
    st.title("🧪 Simulator Kromatografi")
    st.write("""
    Simulasi kromatografi untuk memahami pemisahan komponen dalam campuran.
    """)

elif menu == "🧴 Penanganan Bahan Kimia":
    st.title("🧴 Penanganan Bahan Kimia")
    st.write("""
    Panduan menyimpan dan menangani bahan kimia dengan aman di laboratorium.
    """)

elif menu == "🛡️ Keselamatan Kerja (K3)":
    st.title("🛡️ Keselamatan dan Kesehatan Kerja (K3)")
    st.write("""
    Informasi tentang keselamatan laboratorium dan alat pelindung diri (APD).
    """)

