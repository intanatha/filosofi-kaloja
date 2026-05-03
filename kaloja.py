import streamlit as st
import os

# 1. KONFIGURASI HALAMAN
st.set_page_config(page_title="Filosofi Kaloja", layout="centered")

# 2. GPS OTOMATIS (Mencari lokasi folder di laptop maupun di Cloud)
base_dir = os.path.dirname(os.path.abspath(__file__))

# 3. FUNGSI TAMPILKAN GAMBAR
def tampilkan_gambar(nama_file, caption=None, full_width=True):
    path_lengkap = os.path.join(base_dir, nama_file)
    if os.path.exists(path_lengkap):
        st.image(path_lengkap, caption=caption, use_container_width=full_width)
    else:
        st.error(f"File '{nama_file}' tidak ditemukan.")

# --- BAGIAN TAMPILAN ---

st.title("Sugeng Rawuh! ✨")

# Banner Utama
tampilkan_gambar("scroll.jpg")

st.markdown("---")

# Filosofi Sinom Parijotho
tampilkan_gambar("sinom.jpg")
st.subheader("Batik Sinom Parijotho Salak")
st.write("""
Batik Sinom Parijotho Salak adalah batik khas Kabupaten Sleman yang melambangkan **kemakmuran, kesejahteraan, dan harapan masyarakat yang terayomi**. 

Motif ini menggabungkan tanaman **Parijotho** (simbol kesuburan lereng Merapi) dengan **Salak Pondoh** (hasil bumi utama) dan motif **sinom** (daun muda), yang dimaknai sebagai energi pertumbuhan dan kesejahteraan warga.
""")

st.write("") 

# Filosofi Kembang Waru
tampilkan_gambar("kembangwaru.jpg")
st.subheader("Roti Kembang Waru")
st.write("""
**Kembang Waru** merupakan roti khas Kotagede yang memiliki sejarah panjang karena dipercaya sebagai warisan kerajaan Mataram Islam. 

Di balik bentuknya yang cantik, delapan sisinya memiliki makna **delapan laku seorang pemimpin (Asta Brata)** yang merupakan personifikasi dari delapan elemen unsur alam yakni:
* ☀️ **Matahari**
* 🌙 **Bulan**
* ⭐ **Bintang**
* ☁️ **Mega (Awan)**
* 💧 **Tirta (Air)**
* 🌱 **Kismo (Tanah)**
* 🌊 **Samudra**
* 🌬️ **Maruto (Angin)**
""")

st.markdown("---")

# Koleksi Angka Aksara Jawa (Versi HP Friendly)
st.header("🔢 Koleksi Angka Aksara Jawa")

# Baris Pertama (0-4)
kolom_baris1 = st.columns(5)
for i in range(5):
    with kolom_baris1[i]:
        tampilkan_gambar(f"angka{i}.jpeg", caption=f"Angka {i}")

# Baris Kedua (5-9)
kolom_baris2 = st.columns(5)
for i in range(5, 10):
    with kolom_baris2[i-5]:
        tampilkan_gambar(f"angka{i}.jpeg", caption=f"Angka {i}")

st.write("")

# Tips Penulisan Angka (Versi Lengkap)
with st.expander("📖 Baca Selengkapnya: Penulisan Angka 10 ke Atas"):
    st.write("""
    Penulisan angka dalam aksara Jawa untuk bilangan 10 ke atas dilakukan dengan menggabungkan lambang angka dasar sesuai urutan nilainya, mirip dengan sistem penulisan angka modern. 
    
    Dalam penulisan tradisional Jawa, angka biasanya diapit tanda **pangkat pasanten** (“ : : ”) agar dapat dibedakan dari huruf aksara Jawa lainnya.
    
    **Contoh:**
    * **10** = :꧑꧐: (Angka 1 dan 0)
    * **11** = :꧑꧑: (Angka 1 dan 1)
    * **12** = :꧑꧒: (Angka 1 dan 2)
    * **25** = :꧒꧕: (Angka 2 dan 5)
    * **100** = :꧑꧐꧐: (Angka 1, 0, dan 0)
    """)

st.write("---")
st.caption("© 2026 Kaloja - Materi Filosofi & Aksara Jawa")