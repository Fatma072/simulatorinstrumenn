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
        "🧴 Penanganan Bahan Kimia",
        "🛡️ Keselamatan Kerja (K3)"
    )
)

# ==================== Halaman Beranda ====================
if menu == "🏠 Beranda":
    st.title("💡 Aplikasi Simulator Instrumen Kimia")
    st.markdown("""
    ## Selamat Datang 👋
    Aplikasi ini membantu Anda memahami berbagai **simulasi instrumen laboratorium kimia**, 
    serta menyediakan panduan **penanganan bahan kimia** dan **keselamatan kerja (K3)**.
    """)

# ==================== Halaman Spektrofotometer ====================
elif menu == "🔬 Spektrofotometer":
    st.title("🔬 Simulasi Spektrofotometer UV-Vis")

    st.subheader("🔬 1. Simulasi Spektrum UV-Vis (λ Maksimal)")
    st.write("Simulasi ini menampilkan grafik absorbansi terhadap panjang gelombang.")

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

    # ==================== Simulasi Kurva Kalibrasi ====================
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

    # ==================== Hitung Konsentrasi ====================
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

# ==================== Halaman Penanganan Bahan Kimia ====================
     import streamlit as st

st.title("🧴 Penanganan Bahan Kimia")

bahan = st.selectbox("Pilih bahan kimia:", [
    "Asam Sulfat (H₂SO₄)",
    "Natrium Hidroksida (NaOH)",
    "Aseton (CH₃COCH₃)",
    "Hidrogen Peroksida (H₂O₂)",
    "Klorin (Cl₂)",
    "Metanol (CH₃OH)",
    "Amonia (NH₃)",
    "Benzena (C₆H₆)",
    "Formaldehida (CH₂O)",
    "Klorofom (CHCl₃)"
])

if bahan == "Asam Sulfat (H₂SO₄)":
    st.header("🧪 Asam Sulfat (H₂SO₄)")
    st.markdown("""
    ### 🧪 Karakteristik & Simbol Bahaya  
    - Cairan kental tidak berwarna, sangat korosif  
    - Dapat menyebabkan luka bakar berat pada kulit dan mata  
    ⚠️ **Simbol Bahaya:** ☣️ Korosif | ☠️ Beracun

    ### ⚠️ Risiko Pajanan  
    - Kontak kulit/mata: luka bakar, iritasi parah  
    - Terhirup: iritasi saluran pernapasan  
    - Tertelan: kerusakan saluran cerna

    ### 🚨 Penanganan Darurat  
    - Bilas area terkena dengan air mengalir minimal 15 menit  
    - Lepaskan pakaian yang terkontaminasi  
    - Segera cari bantuan medis

    ### 📦 Penyimpanan Aman  
    - Simpan di tempat dingin, kering, dan berventilasi baik  
    - Jauhkan dari bahan mudah terbakar dan basa kuat

    ### 🛡️ Pencegahan  
    - Gunakan APD lengkap: sarung tangan tahan asam, pelindung wajah, jas lab  
    - Hindari kontak langsung dan hirup uapnya  
    """)

elif bahan == "Natrium Hidroksida (NaOH)":
    st.header("🧪 Natrium Hidroksida (NaOH)")
    st.markdown("""
    ### 🧪 Karakteristik & Simbol Bahaya  
    - Padatan atau larutan sangat basa, korosif  
    ⚠️ **Simbol Bahaya:** ☣️ Korosif

    ### ⚠️ Risiko Pajanan  
    - Luka bakar pada kulit dan mata  
    - Iritasi saluran pernapasan jika terhirup

    ### 🚨 Penanganan Darurat  
    - Bilas area terkena dengan air mengalir selama 15 menit  
    - Lepaskan pakaian terkontaminasi  
    - Segera minta pertolongan medis

    ### 📦 Penyimpanan Aman  
    - Simpan di tempat kering dan tertutup rapat  
    - Jauhkan dari bahan asam dan kelembapan

    ### 🛡️ Pencegahan  
    - Gunakan sarung tangan, pelindung mata, dan jas lab  
    - Hindari kontak langsung dan hirup uapnya  
    """)

elif bahan == "Aseton (CH₃COCH₃)":
    st.header("🧪 Aseton (CH₃COCH₃)")
    st.markdown("""
    ### 🧪 Karakteristik & Simbol Bahaya  
    - Cairan mudah menguap, mudah terbakar  
    ⚠️ **Simbol Bahaya:** 🔥 Mudah Terbakar | ⚠️ Bahaya Kesehatan

    ### ⚠️ Risiko Pajanan  
    - Iritasi mata dan kulit  
    - Dapat menyebabkan kantuk dan pusing jika terhirup dalam jumlah banyak

    ### 🚨 Penanganan Darurat  
    - Pindahkan korban ke udara segar  
    - Bilas kulit dan mata dengan air bersih  
    - Hindari sumber api dan ventilasi baik

    ### 📦 Penyimpanan Aman  
    - Simpan di tempat sejuk, tertutup, dan jauh dari sumber api

    ### 🛡️ Pencegahan  
    - Gunakan ventilasi baik, hindari kontak langsung  
    - Gunakan pelindung mata dan sarung tangan  
    """)

elif bahan == "Hidrogen Peroksida (H₂O₂)":
    st.header("🧪 Hidrogen Peroksida (H₂O₂)")
    st.markdown("""
    ### 🧪 Karakteristik & Simbol Bahaya  
    - Cairan oksidator kuat, korosif  
    ⚠️ **Simbol Bahaya:** ☣️ Korosif | ⚠️ Oksidator

    ### ⚠️ Risiko Pajanan  
    - Luka bakar pada kulit dan mata  
    - Dapat menyebabkan iritasi saluran pernapasan

    ### 🚨 Penanganan Darurat  
    - Bilas area terkena dengan air mengalir  
    - Lepaskan pakaian terkontaminasi  
    - Segera cari bantuan medis jika parah

    ### 📦 Penyimpanan Aman  
    - Simpan di tempat sejuk, tertutup rapat dan jauh dari bahan mudah terbakar

    ### 🛡️ Pencegahan  
    - Gunakan APD lengkap saat bekerja  
    - Hindari kontak langsung dan hirup uapnya  
    """)

elif bahan == "Klorin (Cl₂)":
    st.header("🧪 Klorin (Cl₂)")
    st.markdown("""
    ### 🧪 Karakteristik & Simbol Bahaya  
    - Gas berwarna hijau kekuningan dengan bau tajam  
    ⚠️ **Simbol Bahaya:** ☠️ Racun | ☣️ Korosif

    ### ⚠️ Risiko Pajanan  
    - Iritasi dan luka bakar saluran pernapasan  
    - Kerusakan paru-paru jika terhirup dalam jumlah banyak  
    - Iritasi kulit dan mata

    ### 🚨 Penanganan Darurat  
    - Segera evakuasi ke udara segar  
    - Bilas kulit dan mata dengan air bersih  
    - Gunakan alat pelindung lengkap saat penanganan kebocoran

    ### 📦 Penyimpanan Aman  
    - Simpan tabung gas di tempat berventilasi baik, jauh dari bahan mudah terbakar

    ### 🛡️ Pencegahan  
    - Gunakan respirator, sarung tangan, dan pelindung mata  
    - Hindari kebocoran dan paparan langsung  
    """)

elif bahan == "Metanol (CH₃OH)":
    st.header("🧪 Metanol (CH₃OH)")
    st.markdown("""
    ### 🧪 Karakteristik & Simbol Bahaya  
    - Cairan mudah terbakar, toksik  
    ⚠️ **Simbol Bahaya:** 🔥 Mudah Terbakar | ☠️ Racun

    ### ⚠️ Risiko Pajanan  
    - Keracunan serius jika tertelan  
    - Iritasi kulit dan mata  
    - Efek pada sistem saraf pusat, bisa menyebabkan kebutaan

    ### 🚨 Penanganan Darurat  
    - Jangan memaksa muntah jika tertelan, segera cari bantuan medis  
    - Bilas kulit dan mata dengan air bersih

    ### 📦 Penyimpanan Aman  
    - Simpan di tempat tertutup dan jauh dari api/sumber panas

    ### 🛡️ Pencegahan  
    - Gunakan APD lengkap dan ventilasi baik  
    - Hindari paparan dan konsumsi  
    """)

elif bahan == "Amonia (NH₃)":
    st.header("🧪 Amonia (NH₃)")
    st.markdown("""
    ### 🧪 Karakteristik & Simbol Bahaya  
    - Gas tidak berwarna dengan bau tajam  
    ⚠️ **Simbol Bahaya:** ☠️ Racun | 🧪 Korosif

    ### ⚠️ Risiko Pajanan  
    - Iritasi saluran pernapasan, batuk, sesak napas  
    - Luka bakar kulit dan mata  
    - Paparan tinggi dapat merusak paru-paru

    ### 🚨 Penanganan Darurat  
    - Pindahkan korban ke udara segar  
    - Bilas kulit dan mata dengan air mengalir  
    - Gunakan APD lengkap saat menangani kebocoran gas

    ### 📦 Penyimpanan Aman  
    - Simpan dalam tabung gas bertekanan di tempat berventilasi

    ### 🛡️ Pencegahan  
    - Gunakan respirator, pelindung mata, dan sarung tangan  
    - Hindari kontak langsung dan inhalasi gas  
    """)

elif bahan == "Benzena (C₆H₆)":
    st.header("🧪 Benzena (C₆H₆)")
    st.markdown("""
    ### 🧪 Karakteristik & Simbol Bahaya  
    - Cairan mudah menguap, bau khas  
    ⚠️ **Simbol Bahaya:** ☠️ Racun | 🔥 Mudah Terbakar | ☣️ Karsinogen

    ### ⚠️ Risiko Pajanan  
    - Kerusakan sistem saraf, pusing, mual  
    - Iritasi kulit dan mata  
    - Paparan jangka panjang berisiko kanker darah

    ### 🚨 Penanganan Darurat  
    - Evakuasi ke udara segar  
    - Hindari kontak kulit dan mata  
    - Gunakan APD dan ventilasi baik

    ### 📦 Penyimpanan Aman  
    - Simpan di tempat sejuk dan tertutup rapat

    ### 🛡️ Pencegahan  
    - Gunakan sarung tangan dan pelindung mata  
    - Kerja di ruang ventilasi baik atau fume hood  
    """)

elif bahan == "Formaldehida (CH₂O)":
    st.header("🧪 Formaldehida (CH₂O)")
    st.markdown("""
    ### 🧪 Karakteristik & Simbol Bahaya  
    - Gas atau larutan berbau tajam  
    ⚠️ **Simbol Bahaya:** ☠️ Racun | ☣️ Karsinogen | 🧪 Korosif

    ### ⚠️ Risiko Pajanan  
    - Iritasi saluran pernapasan  
    - Luka bakar kulit dan mata  
    - Risiko kanker hidung dan tenggorokan

    ### 🚨 Penanganan Darurat  
    - Pindahkan korban ke udara segar  
    - Bilas mata dan kulit dengan air mengalir  
    - Gunakan APD lengkap saat bekerja

    ### 📦 Penyimpanan Aman  
    - Simpan di tempat tertutup dan berventilasi baik

    ### 🛡️ Pencegahan  
    - Gunakan respirator, sarung tangan, dan pelindung mata  
    - Kerja di fume hood  
    """)

elif bahan == "Klorofom (CHCl₃)":
    st.header("🧪 Klorofom (CHCl₃)")
    st.markdown("""
    ### 🧪 Karakteristik & Simbol Bahaya  
    - Cairan bening, bau manis  
    ⚠️ **Simbol Bahaya:** ☠️ Racun | ⚠️ Bahaya Kesehatan

    ### ⚠️ Risiko Pajanan  
    - Depresi sistem saraf pusat, mual, pusing  
    - Iritasi kulit dan mata  
    - Risiko kanker hati dan ginjal

    ### 🚨 Penanganan Darurat  
    - Evakuasi ke udara segar  
    - Bilas kulit dan mata dengan air  
    - Gunakan APD saat bekerja

    ### 📦 Penyimpanan Aman  
    - Simpan di tempat gelap, dingin, dan berventilasi

    ### 🛡️ Pencegahan  
    - Gunakan sarung tangan tahan bahan kimia dan pelindung mata  
    - Kerja di fume hood  
    """)

else:
    st.write("Silakan pilih bahan kimia untuk melihat informasi penanganan.")



# ==================== Halaman K3 ====================
elif menu == "🛡️ Keselamatan Kerja (K3)":
    st.title("🛡️ Keselamatan dan Kesehatan Kerja (K3)")
    st.write("""
    Informasi tentang keselamatan laboratorium dan alat pelindung diri (APD).
    """)
