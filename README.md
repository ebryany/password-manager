# 🔐 ZeroFive Password Manager

<div align="center">

![Version](https://img.shields.io/badge/Versi-1.0-blue)
![Python](https://img.shields.io/badge/Python-3.6%2B-yellow)
![Security](https://img.shields.io/badge/Keamanan-Enkripsi%20Fernet-green)
![Language](https://img.shields.io/badge/Bahasa-Indonesia-red)

<img src="https://raw.githubusercontent.com/security-icons/security-icons/master/128/lock-password-fill.png" alt="Password Manager Logo" width="150"/>

### Manajer Password Aman dengan Tampilan Terminal yang Menarik
*Dibuat oleh zerofive_sec - febryan.000*

</div>

---

## 📋 Daftar Isi
- [Fitur Utama](#-fitur-utama)
- [Persyaratan Sistem](#-persyaratan-sistem)
- [Cara Instalasi](#-cara-instalasi)
- [Cara Penggunaan](#-cara-penggunaan)
- [Keamanan](#-keamanan)
- [Tips Penggunaan](#-tips-penggunaan)
- [Pemecahan Masalah](#-pemecahan-masalah)

## ✨ Fitur Utama

### 🔒 Keamanan Tingkat Tinggi
- Enkripsi data menggunakan Fernet (symmetric encryption)
- Penyimpanan password terenkripsi
- Tidak ada password yang disimpan dalam bentuk teks biasa

### 📂 Manajemen Password yang Mudah
- Organisasi password berdasarkan kategori
- Penyimpanan informasi lengkap (username, URL, catatan)
- Pencarian dan filter password berdasarkan kategori

### 💾 Backup dan Restore
- Export password ke file JSON terenkripsi
- Import password dari backup
- Pemilihan lokasi file melalui dialog visual

### 🎨 Antarmuka Pengguna
- Tampilan terminal yang menarik dan berwarna
- Menu yang mudah dipahami
- Pesan status yang informatif
- ASCII art banner yang menarik

## 💻 Persyaratan Sistem

1. Python 3.6 atau lebih baru
2. Paket Python yang diperlukan:
   ```
   cryptography >= 3.4.7
   colorama >= 0.4.4
   rich >= 10.2.2
   ```

## 🚀 Cara Instalasi

1. Clone repositori ini:
   ```bash
   git clone https://github.com/febryan000/zerofive-password-manager.git
   cd zerofive-password-manager
   ```

2. Install dependensi yang diperlukan:
   ```bash
   pip install -r requirements.txt
   ```

## 📖 Cara Penggunaan

### Memulai Program
```bash
python password_manager.py
```

### Menu Utama
1. **Tambah Password** 
   - Menambahkan password baru
   - Masukkan kategori, nama, username, dan password
   - Tambahkan URL dan catatan (opsional)

2. **Lihat Password**
   - Menampilkan daftar password tersimpan
   - Filter berdasarkan kategori
   - Tampilan dalam bentuk tabel yang rapi

3. **Update Password**
   - Memperbarui password yang sudah ada
   - Pilih berdasarkan kategori dan nama
   - Password lama tetap tersimpan dalam history

4. **Hapus Password**
   - Menghapus password yang tidak diperlukan
   - Konfirmasi sebelum penghapusan
   - Tidak bisa dibatalkan setelah dihapus

5. **Export Password**
   - Export semua password ke file JSON
   - Pilih lokasi penyimpanan melalui dialog visual
   - File hasil export terenkripsi

6. **Import Password**
   - Import password dari file backup
   - Pilih file melalui dialog visual
   - Mendukung format JSON terenkripsi

## 🔒 Keamanan

### Enkripsi Data
- Menggunakan algoritma Fernet untuk enkripsi
- Kunci enkripsi disimpan secara aman
- Data terenkripsi saat disimpan dan diekspor

### Penyimpanan Aman
- Password tidak pernah disimpan dalam bentuk teks biasa
- File database terenkripsi
- Kunci enkripsi diproteksi oleh sistem operasi

## 💡 Tips Penggunaan

1. **Organisasi Password**
   - Buat kategori yang jelas (misal: "Email", "Sosial Media", "Perbankan")
   - Gunakan nama yang mudah diingat
   - Tambahkan catatan untuk informasi tambahan

2. **Backup Rutin**
   - Export password secara berkala
   - Simpan file backup di tempat yang aman
   - Lakukan test import untuk memastikan backup berfungsi

3. **Keamanan**
   - Gunakan password yang kuat
   - Jangan bagikan file database
   - Selalu logout setelah menggunakan

## ❓ Pemecahan Masalah

### Password Tidak Tersimpan
- Pastikan ada ruang penyimpanan yang cukup
- Periksa permission folder
- Pastikan program berjalan dengan hak akses yang tepat

### Error Saat Import
- Pastikan format file JSON valid
- Periksa encoding file
- Pastikan file tidak rusak

### Masalah Tampilan
- Pastikan terminal mendukung UTF-8
- Sesuaikan ukuran terminal
- Pastikan font terminal mendukung karakter khusus

## 👨‍💻 Kredit dan Lisensi

### Dibuat dengan ❤️ oleh:
- **zerofive_sec**
- **febryan.000**

### Lisensi
Proyek ini dilisensikan di bawah MIT License. Lihat file LICENSE untuk detail lebih lanjut.

---

<div align="center">

### 🌟 Dukung Proyek Ini 🌟

Jika Anda menyukai proyek ini, berikan bintang di GitHub!

[Report Bug](https://github.com/febryan000/zerofive-password-manager/issues) · [Request Feature](https://github.com/febryan000/zerofive-password-manager/issues)

</div>
