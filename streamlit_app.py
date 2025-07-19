import streamlit as st

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

# Konten berdasarkan menu yang dipilih
if menu == "🏠 Beranda":
    st.title("💡 Aplikasi Simulator Instrumen Kimia")
    st.markdown(
        """
        ## Selamat Datang 👋

        Aplikasi ini membantu Anda memahami berbagai **simulasi instrumen laboratorium kimia**, 
        serta menyediakan panduan **penanganan bahan kimia** dan **keselamatan kerja (K3)**.

        Silakan pilih menu di sebelah kiri untuk mulai menggunakan aplikasi.
        """
    )

elif menu == "🔬 Spektrofotometer":
    st.title("🔬 Simulator Spektrofotometer")
    st.write("""
    Simulasi spektrofotometer untuk melihat hubungan antara konsentrasi dan absorbansi.
    """)

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
    st.title("🛡️ Keselam


