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
elif menu == "🧴 Penanganan Bahan Kimia":
    st.title("🧴 Penanganan Bahan Kimia")

    st.markdown("""
    Bahan kimia di laboratorium dapat bersifat berbahaya jika tidak ditangani dengan benar.  
    Berikut ini adalah panduan lengkap untuk memahami risiko serta cara penanganan dan penyimpanan dari beberapa bahan kimia umum.
    """)

    bahan = st.selectbox("Pilih bahan kimia yang ingin Anda pelajari:", [
        "Asam Sulfat (H₂SO₄)",
        "Natrium Hidroksida (NaOH)",
        "Aseton (CH₃COCH₃)",
        "Hidrogen Peroksida (H₂O₂)"
    ])

    if bahan == "Asam Sulfat (H₂SO₄)":
        st.header("Asam Sulfat (H₂SO₄)")
        st.warning("⚠️ **Bahaya:** Sangat korosif dan bereaksi hebat dengan air.")

        st.markdown("""
        **Karakteristik:**  
        - Cairan kental, tidak berwarna atau sedikit kekuningan  
        - Tidak mudah menguap, namun sangat reaktif  
        - Daya hancur tinggi terhadap jaringan hidup dan sebagian besar material

        **Risiko Pajanan:**  
        - Kontak dengan kulit: luka bakar parah  
        - Uapnya: iritasi saluran pernapasan  
        - Jika tercampur air: menghasilkan panas ekstrem dan percikan

        **Langkah Penanganan Darurat:**  
        - Jika terkena kulit: siram dengan air mengalir minimal 15 menit  
        - Jika terkena mata: bilas mata sambil dibuka perlahan, dan segera ke rumah sakit  
        - Jika tertelan: jangan muntahkan, segera hubungi medis

        **Penyimpanan Aman:**  
        - Gunakan wadah dari kaca tahan asam atau plastik khusus (HDPE)  
        - Simpan di tempat sejuk, gelap, dan berventilasi  
        - Jangan simpan dekat air, logam, atau bahan organik

        **Pencegahan:**  
        - Gunakan pelindung wajah, sarung tangan, dan apron kimia  
        - Selalu tambahkan asam ke air, bukan sebaliknya
        """)

    elif bahan == "Natrium Hidroksida (NaOH)":
        st.header("Natrium Hidroksida (NaOH)")
        st.warning("⚠️ **Bahaya:** Sangat basa, bersifat kaustik, dapat merusak jaringan tubuh.")

        st.markdown("""
        **Karakteristik:**  
        - Padatan putih atau larutan bening  
        - Bersifat higroskopis (menyerap uap air)  
        - Membentuk larutan yang sangat basa dan panas saat dilarutkan

        **Risiko Pajanan:**  
        - Iritasi atau luka bakar berat pada kulit dan mata  
        - Dapat menyebabkan kerusakan permanen jika kontak mata lama  
        - Uap dapat menyebabkan iritasi saluran pernapasan

        **Langkah Penanganan Darurat:**  
        - Kulit terkena: bilas dengan air tanpa henti selama 20 menit  
        - Mata terkena: bilas dengan larutan saline atau air bersih segera  
        - Jika tertelan: jangan dipaksa muntah, hubungi rumah sakit

        **Penyimpanan Aman:**  
        - Simpan dalam wadah plastik tahan basa dan tertutup rapat  
        - Hindari kontak dengan bahan asam  
        - Simpan di tempat kering, sejuk, dan berventilasi

        **Pencegahan:**  
        - Gunakan sarung tangan nitril, pelindung mata, dan jas laboratorium  
        - Tangani di bawah lemari asam jika memungkinkan
        """)

    elif bahan == "Aseton (CH₃COCH₃)":
        st.header("Aseton (CH₃COCH₃)")
        st.warning("⚠️ **Bahaya:** Sangat mudah terbakar, menyebabkan iritasi pernapasan.")

        st.markdown("""
        **Karakteristik:**  
        - Cairan bening, sangat mudah menguap  
        - Berbau khas (seperti pelarut cat kuku)  
        - Digunakan sebagai pelarut di banyak industri

        **Risiko Pajanan:**  
        - Menghirup uapnya menyebabkan pusing, sakit kepala, mual  
        - Kontak kulit menyebabkan kekeringan dan iritasi  
        - Bahaya kebakaran tinggi bahkan pada suhu ruangan

        **Langkah Penanganan Darurat:**  
        - Hirup uap: segera ke area berventilasi atau udara segar  
        - Kontak kulit: cuci dengan sabun dan air  
        - Terbakar: gunakan APAR CO₂ atau dry chemical

        **Penyimpanan Aman:**  
        - Gunakan wadah logam tahan pelarut dengan tutup rapat  
        - Jauhkan dari sumber api, percikan, dan listrik statis  
        - Simpan di kabinet bahan mudah terbakar (flammable storage)

        **Pencegahan:**  
        - Gunakan di ruangan terbuka atau berventilasi baik  
        - Hindari menghirup uap secara langsung
        """)

    elif bahan == "Hidrogen Peroksida (H₂O₂)":
        st.header("Hidrogen Peroksida (H₂O₂)")
        st.warning("⚠️ **Bahaya:** Oksidator kuat, reaktif, dan dapat menyebabkan luka bakar kimia.")

        st.markdown("""
        **Karakteristik:**  
        - Larutan bening, mirip air, tapi sangat reaktif  
        - Konsentrasi tinggi (di atas 30%) sangat berbahaya  
        - Digunakan sebagai desinfektan dan agen pemutih

        **Risiko Pajanan:**  
        - Kulit: luka bakar, iritasi  
        - Mata: iritasi serius atau kebutaan permanen  
        - Reaksi eksplosif jika kontak logam, bahan organik, atau panas

        **Langkah Penanganan Darurat:**  
        - Kulit terkena: bilas dengan air 15 menit  
        - Mata terkena: segera cuci mata dan hubungi dokter  
        - Terhirup: pindahkan ke area udara segar dan beri oksigen jika perlu

        **Penyimpanan Aman:**  
        - Simpan dalam botol berwarna gelap, jauh dari cahaya  
        - Hindari suhu tinggi dan bahan logam  
        - Gunakan wadah asli yang tahan oksidasi

        **Pencegahan:**  
        - Gunakan pelindung mata dan sarung tangan neoprene  
        - Hindari penggunaan logam atau benda berkarat saat menanganinya
        """)


# ==================== Halaman K3 ====================
elif menu == "🛡️ Keselamatan Kerja (K3)":
    st.title("🛡️ Keselamatan dan Kesehatan Kerja (K3)")
    st.write("""
    Informasi tentang keselamatan laboratorium dan alat pelindung diri (APD).
    """)
