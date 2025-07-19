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
        "🔬 Spektrofotometer"
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

st.subheader("🔬 1. Simulasi Spektrum UV-Vis (λ Maksimal)")
st.write("Simulasi ini menampilkan grafik absorbansi terhadap panjang gelombang.")

# Input manual data UV-Vis
contoh_data = "200,0.01\n250,0.18\n300,0.45\n350,0.60\n400,0.40\n450,0.25"
input_uvvis = st.text_area("Masukkan data panjang gelombang dan absorbansi (λ [nm], Absorbansi)", contoh_data, height=150)

df_uv = None
if input_uvvis:
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
else:
    st.info("Silakan masukkan data panjang gelombang dan absorbansi di atas untuk melihat grafik.")


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

# Lanjutkan dengan menu lainnya...

elif menu == "🧴 Penanganan Bahan Kimia":
    st.title("🧴 Penanganan Bahan Kimia")
    st.write("Pelajari cara menangani bahan kimia dnegan aman di laboratorium.")

    bahan = st.selectbox("Pilih bahan kimia:", [
        "Asam Sulfat (H₂SO₄)",
        "Natrium Hidroksida (NaOH)",
        "Aseton (CH₃COCH₃)",
        "Hidrogen Peroksida (H₂O₂)"
    ])

    if bahan == "Asam Sulfat (H₂SO₄)":
        st.warning("⚠️ Korosif! Gunakan pelindung wajah dan sarung tangan tahan asam.")
    elif bahan == "Natrium Hidroksida (NaOH)":
        st.warning("⚠️ Sangat basa dan korosif. Hindari kontak langsung.")
    elif bahan == "Aseton (CH₃COCH₃)":
        st.warning("⚠️ Mudah terbakar! Gunakan di ruangan berventilasi.")
    elif bahan == "Hidrogen Peroksida (H₂O₂)":
        st.warning("⚠️ Oksidator kuat. Hindari kontak dengan bahan organik.")



 
    
elif menu == "🛡️ Keselamatan Kerja (K3)":
    st.title("🛡️ Keselamatan dan Kesehatan Kerja (K3)")
    st.write("""
    Informasi tentang keselamatan laboratorium dan alat pelindung diri (APD).
    """)

