import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

# Konfigurasi halaman
st.set_page_config(page_title="Simulator Kimia", layout="wide")

# Sidebar menu
menu = st.sidebar.selectbox(
    "Pilih Halaman",
    (
        "🏠 Beranda",
        "🔬 Spektrofotometer",
        "⚗️ Titrasi",
        "🧪 Kromatografi",
        "🧴 Penanganan Bahan Kimia",
        "🛡️ Keselamatan Kerja (K3)"
    )
)

# ==================== Konten halaman ====================

if menu == "🏠 Beranda":
    st.title("💡 Aplikasi Simulator Instrumen Kimia")
    st.markdown("""
    ## Selamat Datang 👋
    Aplikasi ini membantu Anda memahami berbagai **simulasi instrumen laboratorium kimia**, 
    serta menyediakan panduan **penanganan bahan kimia** dan **keselamatan kerja (K3)**.
    """)

elif menu == "🔬 Spektrofotometer":
    st.title("🔬 Simulasi Spektrofotometer UV-Vis")

    st.subheader("1. Simulasi Spektrum UV-Vis (λ Maksimal)")
    contoh_data = "200,0.01\n250,0.18\n300,0.45\n350,0.60\n400,0.40\n450,0.25"
    input_uvvis = st.text_area("Masukkan data panjang gelombang dan absorbansi:", contoh_data, height=150)
    uploaded_file = st.file_uploader("Atau unggah file CSV (2 kolom)", type=["csv"])

    df_uv = None
    if uploaded_file is not None:
        try:
            df_uv = pd.read_csv(uploaded_file)
            if df_uv.shape[1] != 2:
                st.warning("CSV harus memiliki 2 kolom: panjang gelombang dan absorbansi.")
                df_uv = None
        except Exception as e:
            st.error(f"Kesalahan file: {e}")
    elif input_uvvis:
        try:
            data = [tuple(map(float, line.split(','))) for line in input_uvvis.strip().split('\n')]
            df_uv = pd.DataFrame(data, columns=["Panjang Gelombang (nm)", "Absorbansi"])
        except Exception as e:
            st.error(f"Gagal parsing data teks: {e}")

    if df_uv is not None:
        idx_max = df_uv["Absorbansi"].idxmax()
        lambda_max = df_uv.loc[idx_max, "Panjang Gelombang (nm)"]
        st.success(f"λ Maksimum terdeteksi pada: **{lambda_max} nm**")

        warna = st.color_picker("Warna garis", "#0000ff")
        overlay = st.checkbox("Tampilkan spektrum referensi (simulasi)?")

        fig, ax = plt.subplots()
        ax.plot(df_uv["Panjang Gelombang (nm)"], df_uv["Absorbansi"], color=warna, label='Sampel')
        ax.axvline(lambda_max, color='red', linestyle='--', label=f'λ maks = {lambda_max} nm')

        if overlay:
            ref_abs = np.interp(df_uv["Panjang Gelombang (nm)"], df_uv["Panjang Gelombang (nm)"], df_uv["Absorbansi"]) * 0.8
            ax.plot(df_uv["Panjang Gelombang (nm)"], ref_abs, color='gray', linestyle=':', label='Referensi')

        ax.set_xlabel("Panjang Gelombang (nm)")
        ax.set_ylabel("Absorbansi")
        ax.set_title("Spektrum UV-Vis")
        ax.legend()
        st.pyplot(fig)

    st.subheader("2. Simulasi Kurva Kalibrasi")
    default_data = {
        "Konsentrasi (ppm)": [0, 5, 10, 15, 20, 25],
        "Absorbansi": [0.02, 0.13, 0.27, 0.40, 0.52, 0.64]
    }

    df = pd.DataFrame(default_data)
    edited_df = st.data_editor(df, use_container_width=True)

    X = np.array(edited_df["Konsentrasi (ppm)"]).reshape(-1, 1)
    y = np.array(edited_df["Absorbansi"])

    model = LinearRegression()
    model.fit(X, y)

    slope = model.coef_[0]
    intercept = model.intercept_
    r2 = model.score(X, y)

    st.markdown(f"""
    **Persamaan regresi:**  
    Absorbansi = {slope:.4f} × Konsentrasi + {intercept:.4f}  
    Koefisien determinasi (R²) = {r2:.4f}
    """)

    fig, ax = plt.subplots()
    ax.scatter(X, y, color='blue', label='Data Standar')
    ax.plot(X, model.predict(X), color='green', label='Regresi Linear')
    ax.set_xlabel("Konsentrasi (ppm)")
    ax.set_ylabel("Absorbansi")
    ax.legend()
    st.pyplot(fig)

    st.subheader("3. Hitung Konsentrasi Sampel")
    absorbansi_sampel = st.number_input("Nilai absorbansi sampel", min_value=0.0, step=0.01)
    slope_input = st.number_input("Slope", value=float(slope), format="%.4f")
    intercept_input = st.number_input("Intercept", value=float(intercept), format="%.4f")

    if st.button("Hitung Konsentrasi"):
        try:
            konsentrasi = (absorbansi_sampel - intercept_input) / slope_input
            st.success(f"Perkiraan konsentrasi sampel: **{konsentrasi:.2f} ppm**")
        except ZeroDivisionError:
            st.error("Slope tidak boleh nol.")

elif menu == "⚗️ Titrasi":
    st.title("⚗️ Simulator Titrasi")
    st.write("""
    Simulasi titrasi untuk mempelajari perubahan pH selama penambahan titran.
    """)

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

