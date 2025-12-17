# 💧 Water Bucket Puzzle - Desktop GUI Version

Aplikasi puzzle ember air dengan antarmuka grafis menggunakan Tkinter. Game puzzle logika klasik di mana pemain harus mendapatkan jumlah air yang tepat menggunakan ember dengan ukuran berbeda.

## 📋 Deskripsi

Water Bucket Puzzle adalah permainan teka-teki logika yang menantang pemain untuk mendapatkan jumlah air tertentu di salah satu ember dengan hanya menggunakan operasi:
- Mengisi ember sampai penuh
- Mengosongkan ember
- Menuangkan air dari satu ember ke ember lainnya

## ✨ Fitur

- **Antarmuka Grafis Interaktif**: GUI yang user-friendly dengan visualisasi ember air
- **3 Tingkat Kesulitan**:
  - **Easy**: Target 4L dengan ember 8L, 5L, dan 3L
  - **Medium**: Target 6L dengan ember 10L, 7L, dan 3L
  - **Hard**: Target 5L dengan ember 12L, 8L, dan 5L
- **Visualisasi Real-time**: Melihat level air di setiap ember secara visual
- **Pelacakan Langkah**: Menghitung jumlah langkah yang diambil
- **Riwayat Aksi**: Mencatat semua aksi yang dilakukan pemain
- **Sistem Hint**: Mendapatkan petunjuk untuk menyelesaikan puzzle
- **Reset Game**: Mengulang permainan kapan saja
- **Exception Handling**: Penanganan error yang robust

## 🎮 Cara Bermain

1. **Pilih Tingkat Kesulitan**: Klik salah satu tombol tingkat kesulitan di bagian atas
2. **Lihat Target**: Perhatikan target air yang harus dicapai
3. **Lakukan Aksi**:
   - **ISI**: Mengisi ember sampai penuh
   - **KOSONG**: Mengosongkan ember sepenuhnya
   - **Tuang (→)**: Menuangkan air dari satu ember ke ember lain
4. **Menangkan**: Dapatkan jumlah air yang tepat sesuai target di salah satu ember
5. **Gunakan Hint**: Klik tombol "💡 HINT" jika membutuhkan bantuan

## 🔧 Instalasi

### Persyaratan Sistem
- Python 3.7 atau lebih tinggi
- Tkinter (biasanya sudah terinstall dengan Python)

### Langkah Instalasi

1. Clone atau download repository ini
```bash
git clone <repository-url>
cd water-bucket-puzzle
```

2. Pastikan Python terinstall
```bash
python --version
```

3. Jalankan aplikasi
```bash
python waterbucket_gui_tkinter.py
```

## 📦 Dependencies

```
tkinter (built-in dengan Python)
random (built-in dengan Python)
typing (built-in dengan Python)
```

Tidak ada dependency eksternal yang perlu diinstall!

## 🎯 Strategi Menyelesaikan

### Tips Umum:
- Mulai dengan mengisi ember terbesar
- Gunakan ember terkecil sebagai alat ukur
- Catat pola yang berhasil untuk digunakan kembali
- Berpikir mundur dari target yang ingin dicapai

### Contoh Solusi Easy (Target 4L):
1. Isi ember 5L penuh
2. Tuang ember 5L ke ember 3L (sisa 2L di ember 5L)
3. Kosongkan ember 3L
4. Tuang sisa 2L dari ember 5L ke ember 3L
5. Isi ember 5L penuh lagi
6. Tuang dari ember 5L ke ember 3L sampai penuh (butuh 1L)
7. Sekarang ember 5L berisi 4L ✓

## 🖥️ Struktur Kode

```
waterbucket_gui_tkinter.py
├── WaterBucketGUI (Class)
│   ├── __init__(): Inisialisasi aplikasi
│   ├── setup_ui(): Setup komponen UI
│   ├── setup_difficulty_frame(): Setup pilihan kesulitan
│   ├── setup_stats_frame(): Setup tampilan statistik
│   ├── setup_buckets_frame(): Setup area visualisasi ember
│   ├── setup_control_frame(): Setup tombol kontrol
│   ├── setup_action_frame(): Setup tombol aksi
│   ├── setup_history_frame(): Setup panel riwayat
│   ├── draw_buckets(): Menggambar semua ember
│   ├── draw_bucket(): Menggambar satu ember dengan air
│   ├── fill_bucket(): Mengisi ember penuh
│   ├── empty_bucket(): Mengosongkan ember
│   ├── pour_bucket(): Menuangkan air antar ember
│   ├── check_win(): Mengecek kondisi menang
│   ├── add_to_history(): Menambah ke riwayat
│   ├── update_display(): Update tampilan
│   ├── reset_game(): Reset permainan
│   ├── change_difficulty(): Ubah tingkat kesulitan
│   └── show_hint(): Tampilkan petunjuk
└── main(): Fungsi utama menjalankan aplikasi
```

## 🎨 Desain UI

- **Color Scheme**: 
  - Background: Light Gray (#F5F5F5)
  - Water: Blue (#1976D2)
  - Border: Dark Blue (#0D47A1)
  - Buttons: Various colors untuk fungsi berbeda
- **Fonts**: Arial untuk teks, Consolas untuk riwayat
- **Layout**: Responsive dengan proper spacing

## 🐛 Error Handling

Aplikasi dilengkapi dengan exception handling komprehensif:
- Try-catch blocks di setiap method penting
- Error messages yang informatif
- Graceful failure handling
- Validasi input

## 📝 Lisensi

Original code by Al Sweigart (al@inventwithpython.com)
Enhanced with Tkinter GUI and exception handling

## 👨‍💻 Pengembang

- Original: Al Sweigart
- GUI Enhancement: [Your Name]

## 🤝 Kontribusi

Kontribusi selalu diterima! Silakan:
1. Fork repository
2. Buat branch fitur (`git checkout -b feature/AmazingFeature`)
3. Commit perubahan (`git commit -m 'Add some AmazingFeature'`)
4. Push ke branch (`git push origin feature/AmazingFeature`)
5. Buat Pull Request

## 📧 Kontak

Untuk pertanyaan, saran, atau bug report, silakan buka issue di repository ini.

## 🎓 Pembelajaran

Game ini bagus untuk:
- Belajar logika dan problem solving
- Memahami algoritma dan strategi
- Pengenalan programming dengan Python
- Belajar GUI development dengan Tkinter

---

**Selamat Bermain! 💧🎮**
