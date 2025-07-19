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
    ⚠ *Simbol Bahaya:* ☣ Korosif | ☠ Beracun

    ### ⚠ Risiko Pajanan  
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

    ### 🛡 Pencegahan  
    - Gunakan APD lengkap: sarung tangan tahan asam, pelindung wajah, jas lab  
    - Hindari kontak langsung dan hirup uapnya  
    """)

elif bahan == "Natrium Hidroksida (NaOH)":
    st.header("🧪 Natrium Hidroksida (NaOH)")
    st.markdown("""
    ### 🧪 Karakteristik & Simbol Bahaya  
    - Padatan atau larutan sangat basa, korosif  
    ⚠ *Simbol Bahaya:* ☣ Korosif

    ### ⚠ Risiko Pajanan  
    - Luka bakar pada kulit dan mata  
    - Iritasi saluran pernapasan jika terhirup

    ### 🚨 Penanganan Darurat  
    - Bilas area terkena dengan air mengalir selama 15 menit  
    - Lepaskan pakaian terkontaminasi  
    - Segera minta pertolongan medis

    ### 📦 Penyimpanan Aman  
    - Simpan di tempat kering dan tertutup rapat  
    - Jauhkan dari bahan asam dan kelembapan

    ### 🛡 Pencegahan  
    - Gunakan sarung tangan, pelindung mata, dan jas lab  
    - Hindari kontak langsung dan hirup uapnya  
    """)

elif bahan == "Aseton (CH₃COCH₃)":
    st.header("🧪 Aseton (CH₃COCH₃)")
    st.markdown("""
    ### 🧪 Karakteristik & Simbol Bahaya  
    - Cairan mudah menguap, mudah terbakar  
    ⚠ *Simbol Bahaya:* 🔥 Mudah Terbakar | ⚠ Bahaya Kesehatan

    ### ⚠ Risiko Pajanan  
    - Iritasi mata dan kulit  
    - Dapat menyebabkan kantuk dan pusing jika terhirup dalam jumlah banyak

    ### 🚨 Penanganan Darurat  
    - Pindahkan korban ke udara segar  
    - Bilas kulit dan mata dengan air bersih  
    - Hindari sumber api dan ventilasi baik

    ### 📦 Penyimpanan Aman  
    - Simpan di tempat sejuk, tertutup, dan jauh dari sumber api

    ### 🛡 Pencegahan  
    - Gunakan ventilasi baik, hindari kontak langsung  
    - Gunakan pelindung mata dan sarung tangan  
    """)

elif bahan == "Hidrogen Peroksida (H₂O₂)":
    st.header("🧪 Hidrogen Peroksida (H₂O₂)")
    st.markdown("""
    ### 🧪 Karakteristik & Simbol Bahaya  
    - Cairan oksidator kuat, korosif  
    ⚠ *Simbol Bahaya:* ☣ Korosif | ⚠ Oksidator

    ### ⚠ Risiko Pajanan  
    - Luka bakar pada kulit dan mata  
    - Dapat menyebabkan iritasi saluran pernapasan

    ### 🚨 Penanganan Darurat  
    - Bilas area terkena dengan air mengalir  
    - Lepaskan pakaian terkontaminasi  
    - Segera cari bantuan medis jika parah

    ### 📦 Penyimpanan Aman  
    - Simpan di tempat sejuk, tertutup rapat dan jauh dari bahan mudah terbakar

    ### 🛡 Pencegahan  
    - Gunakan APD lengkap saat bekerja  
    - Hindari kontak langsung dan hirup uapnya  
    """)

elif bahan == "Klorin (Cl₂)":
    st.header("🧪 Klorin (Cl₂)")
    st.markdown("""
    ### 🧪 Karakteristik & Simbol Bahaya  
    - Gas berwarna hijau kekuningan dengan bau tajam  
    ⚠ *Simbol Bahaya:* ☠ Racun | ☣ Korosif

    ### ⚠ Risiko Pajanan  
    - Iritasi dan luka bakar saluran pernapasan  
    - Kerusakan paru-paru jika terhirup dalam jumlah banyak  
    - Iritasi kulit dan mata

    ### 🚨 Penanganan Darurat  
    - Segera evakuasi ke udara segar  
    - Bilas kulit dan mata dengan air bersih  
    - Gunakan alat pelindung lengkap saat penanganan kebocoran

    ### 📦 Penyimpanan Aman  
    - Simpan tabung gas di tempat berventilasi baik, jauh dari bahan mudah terbakar

    ### 🛡 Pencegahan  
    - Gunakan respirator, sarung tangan, dan pelindung mata  
    - Hindari kebocoran dan paparan langsung  
    """)

elif bahan == "Metanol (CH₃OH)":
    st.header("🧪 Metanol (CH₃OH)")
    st.markdown("""
    ### 🧪 Karakteristik & Simbol Bahaya  
    - Cairan mudah terbakar, toksik  
    ⚠ *Simbol Bahaya:* 🔥 Mudah Terbakar | ☠ Racun

    ### ⚠ Risiko Pajanan  
    - Keracunan serius jika tertelan  
    - Iritasi kulit dan mata  
    - Efek pada sistem saraf pusat, bisa menyebabkan kebutaan

    ### 🚨 Penanganan Darurat  
    - Jangan memaksa muntah jika tertelan, segera cari bantuan medis  
    - Bilas kulit dan mata dengan air bersih

    ### 📦 Penyimpanan Aman  
    - Simpan di tempat tertutup dan jauh dari api/sumber panas

    ### 🛡 Pencegahan  
    - Gunakan APD lengkap dan ventilasi baik  
    - Hindari paparan dan konsumsi  
    """)

elif bahan == "Amonia (NH₃)":
    st.header("🧪 Amonia (NH₃)")
    st.markdown("""
    ### 🧪 Karakteristik & Simbol Bahaya  
    - Gas tidak berwarna dengan bau tajam  
    ⚠ *Simbol Bahaya:* ☠ Racun | 🧪 Korosif

    ### ⚠ Risiko Pajanan  
    - Iritasi saluran pernapasan, batuk, sesak napas  
    - Luka bakar kulit dan mata  
    - Paparan tinggi dapat merusak paru-paru

    ### 🚨 Penanganan Darurat  
    - Pindahkan korban ke udara segar  
    - Bilas kulit dan mata dengan air mengalir  
    - Gunakan APD lengkap saat menangani kebocoran gas

    ### 📦 Penyimpanan Aman  
    - Simpan dalam tabung gas bertekanan di tempat berventilasi

    ### 🛡 Pencegahan  
    - Gunakan respirator, pelindung mata, dan sarung tangan  
    - Hindari kontak langsung dan inhalasi gas  
    """)

elif bahan == "Benzena (C₆H₆)":
    st.header("🧪 Benzena (C₆H₆)")
    st.markdown("""
    ### 🧪 Karakteristik & Simbol Bahaya  
    - Cairan mudah menguap, bau khas  
    ⚠ *Simbol Bahaya:* ☠ Racun | 🔥 Mudah Terbakar | ☣ Karsinogen

    ### ⚠ Risiko Pajanan  
    - Kerusakan sistem saraf, pusing, mual  
    - Iritasi kulit dan mata  
    - Paparan jangka panjang berisiko kanker darah

    ### 🚨 Penanganan Darurat  
    - Evakuasi ke udara segar  
    - Hindari kontak kulit dan mata  
    - Gunakan APD dan ventilasi baik

    ### 📦 Penyimpanan Aman  
    - Simpan di tempat sejuk dan tertutup rapat

    ### 🛡 Pencegahan  
    - Gunakan sarung tangan dan pelindung mata  
    - Kerja di ruang ventilasi baik atau fume hood  
    """)

elif bahan == "Formaldehida (CH₂O)":
    st.header("🧪 Formaldehida (CH₂O)")
    st.markdown("""
    ### 🧪 Karakteristik & Simbol Bahaya  
    - Gas atau larutan berbau tajam  
    ⚠ *Simbol Bahaya:* ☠ Racun | ☣ Karsinogen | 🧪 Korosif

    ### ⚠ Risiko Pajanan  
    - Iritasi saluran pernapasan  
    - Luka bakar kulit dan mata  
    - Risiko kanker hidung dan tenggorokan

    ### 🚨 Penanganan Darurat  
    - Pindahkan korban ke udara segar  
    - Bilas mata dan kulit dengan air mengalir  
    - Gunakan APD lengkap saat bekerja

    ### 📦 Penyimpanan Aman  
    - Simpan di tempat tertutup dan berventilasi baik

    ### 🛡 Pencegahan  
    - Gunakan respirator, sarung tangan, dan pelindung mata  
    - Kerja di fume hood  
    """)

elif bahan == "Klorofom (CHCl₃)":
    st.header("🧪 Klorofom (CHCl₃)")
    st.markdown("""
    ### 🧪 Karakteristik & Simbol Bahaya  
    - Cairan bening, bau manis  
    ⚠ *Simbol Bahaya:* ☠ Racun | ⚠ Bahaya Kesehatan

    ### ⚠ Risiko Pajanan  
    - Depresi sistem saraf pusat, mual, pusing  
    - Iritasi kulit dan mata  
    - Risiko kanker hati dan ginjal

    ### 🚨 Penanganan Darurat  
    - Evakuasi ke udara segar  
    - Bilas kulit dan mata dengan air  
    - Gunak
