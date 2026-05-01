import streamlit as st
import os

# 1. KONFIGURASI HALAMAN
st.set_page_config(page_title="Filosofi Kaloja", layout="centered")

# 2. GPS OTOMATIS (Mencari lokasi folder D:\intan SMA\Fiksi_Kaloja)
base_dir = os.path.dirname(os.path.abspath(__file__))

# 3. FUNGSI TAMPILKAN GAMBAR
def tampilkan_gambar(nama_file, caption=None, tipe="besar"):
    path_lengkap = os.path.join(base_dir, nama_file)
    if os.path.exists(path_lengkap):
        if tipe == "besar":
            # Untuk Banner, Sinom, dan Kembang Waru (Lebar Penuh)
            st.image(path_lengkap, caption=caption, use_container_width=True)
        else:
            # Untuk Angka (Ukuran Kecil & Pas di Kolom)
            st.image(path_lengkap, caption=caption, use_container_width=True)
    else:
        st.error(f"File '{nama_file}' tidak ditemukan.")

# --- BAGIAN TAMPILAN ---

st.title("Sugeng Rawuh! ✨")

# Banner Utama (Besar)
tampilkan_gambar("scroll.jpg", tipe="besar")

st.markdown("---")

# Filosofi Sinom Parijotho (Besar)
tampilkan_gambar("sinom.jpg", tipe="besar")
st.subheader("Sinom Parijotho")
st.write("""
Terinspirasi dari tanaman khas lereng Gunung Muria, Sinom Parijotho merupakan simbol kemakmuran dan keselarasan. 
Nama **"Sinom"** melambangkan pertumbuhan daun muda, sementara Parijotho melambangkan anugerah alam yang bermanfaat. 
""")

st.write("") 

# Filosofi Kembang Waru (Besar)
tampilkan_gambar("kembangwaru.jpg", tipe="besar")
st.subheader("Kembang Waru")
st.write("""
Kembang waru merupakan roti khas Kotagede yang memiliki sejarah panjang sebagai warisan Kerajaan Mataram Islam. 
Di balik bentuknya yang cantik, delapan sisinya memiliki makna **Asta Brata**.
""")

st.markdown("---")

# Koleksi Angka Aksara Jawa (Kecil & Berjejer)
st.header("🔢 Koleksi Angka Aksara Jawa")

# Membuat grid 5 kolom
cols = st.columns(5)

# Looping angka 0-9 (Tipe "kecil" agar mengikuti lebar kolom saja)
for i in range(10):
    with cols[i % 5]:
        tampilkan_gambar(f"angka{i}.jpeg", caption=f"Angka {i}", tipe="kecil")

# Footer
st.write("")
st.info("💡 **Tips Menulis Angka 10+:** Sistem angka Jawa adalah desimal. Contoh: ꧇꧑꧐꧇")

st.write("---")
st.caption("© 2026 Kaloja - Antekriya")