import streamlit as st
from pathlib import Path

# ============================
# PENGATURAN HALAMAN
# ============================
st.set_page_config(
    page_title="EduVolt – Alat Edukatif Penghasil Listrik",
    layout="wide"
)

# ============================
# GAYA (CSS) AGAR TIDAK PUTIH
# ============================
page_bg = """
<style>
body {
    background-color: #0f172a;
    color: #f1f5f9;
}

h1, h2, h3, h4 {
    color: #38bdf8 !important;
}

.stButton>button {
    background-color: #38bdf8;
    color: black;
    padding: 0.6rem 1.2rem;
    border-radius: 8px;
    border: none;
    font-weight: 600;
}

.stButton>button:hover {
    background-color: #7dd3fc;
    color: black;
}

.block-container {
    padding-top: 2rem;
}

</style>
"""
st.markdown(page_bg, unsafe_allow_html=True)

# ============================
# JUDUL
# ============================
st.title("EduVolt – Alat Edukatif Penghasil Listrik")
st.subheader("“Media pembelajaran berbasis eksperimen nyata untuk memahami energi listrik.”")

# ============================
# FOTO ALAT
# ============================
st.header("📸 Foto Alat EduVolt")

if Path("assets/alat.jpg").exists():
    st.image("assets/alat.jpg", use_column_width=True, caption="Foto utama EduVolt")
else:
    st.warning("Upload foto alat Anda ke folder: assets/alat.jpg")

st.markdown("---")

# ============================
# VIDEO DEMONSTRASI
# ============================
st.header("🎥 Video Demonstrasi Alat")

demo_path = Path("assets/demo.mp4")
if demo_path.exists():
    st.video(str(demo_path))
else:
    st.warning("Upload video demo ke folder: assets/demo.mp4")

st.markdown("---")

# ============================
# DESKRIPSI AKADEMIS
# ============================

st.header("📚 Latar Belakang")
st.write("""
Pemahaman mengenai energi listrik dan proses konversinya masih menjadi tantangan bagi peserta didik,
khususnya pada jenjang sekolah menengah. Banyak konsep dasar seperti induksi elektromagnetik, arus listrik,
dan energi mekanik sulit dipahami jika hanya dijelaskan secara teoritis.

EduVolt dikembangkan sebagai **media pembelajaran berbasis eksperimen nyata** yang memvisualisasikan
bagaimana energi mekanik diubah menjadi energi listrik dan bagaimana listrik tersebut dapat dimanfaatkan
untuk menyalakan beban seperti lampu dan pengisian perangkat elektronik.
""")

st.header("📘 Teori Fisika yang Mendasari")
st.write("""
EduVolt bekerja berdasarkan **prinsip induksi elektromagnetik**, yaitu fenomena ketika perubahan gerak
atau perubahan medan magnet menghasilkan tegangan listrik. Ketika baling-baling berputar, motor DC
berperan sebagai generator yang mengonversi energi mekanik menjadi energi listrik.

Tegangan keluaran kemudian dikontrol dan disalurkan ke beberapa beban,
seperti lampu LED dan modul pengisian daya. Prinsip ini merupakan dasar penting dalam
pembangkit listrik skala besar maupun perangkat portabel.
""")

st.header("⭐ Keunggulan Proyek EduVolt")
st.markdown("""
- Menggunakan komponen sederhana yang mudah ditemukan  
- Tahan lama dan aman untuk demonstrasi kelas  
- Dapat menyalakan lampu dan mengisi daya ponsel  
- Visual yang menarik sehingga mempermudah pemahaman konsep  
- Dapat digunakan sebagai alat praktikum fisika mandiri  
""")

st.header("⚙️ Konsep Fisika yang Ditunjukkan")
st.write("""
Beberapa konsep fisika yang divisualisasikan melalui EduVolt:

1. **Energi Mekanik → Energi Listrik**  
   Putaran baling-baling menggerakkan rotor motor sehingga menghasilkan arus.

2. **Generator Sederhana**  
   Motor DC digunakan sebagai generator kecil.

3. **Arus, Tegangan, dan Daya**  
   Pengguna dapat melihat hubungan beban listrik terhadap terang lampu dan arus yang dihasilkan.

4. **Penerapan Konsep pada Kehidupan Nyata**  
   Sistem kerja EduVolt mirip dengan kincir angin, turbin, dan pembangkit listrik sederhana.
""")

st.markdown("---")

# ============================
# ULASAN PENGUNJUNG
# ============================
st.header("📝 Ulasan Pengunjung")

name = st.text_input("Nama Anda:")
review = st.text_area("Tulis ulasan Anda:")

if st.button("Kirim Ulasan"):
    st.success("Terima kasih! Ulasan Anda telah diterima.")

