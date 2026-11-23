# ⚡ NetCheck Desktop

Aplikasi penguji kecepatan dan kualitas jaringan Wi-Fi berbasis Python GUI (Tkinter).

## 🚀 Fitur Utama
- 📶 **Pengujian Latency / Ping** (ms)
- 📥 **Pengujian Kecepatan Download** (Mbps)
- 📤 **Pengujian Kecepatan Upload** (Mbps)
- 🌐 **Deteksi Informasi Server & Lokasi Otomatis**
- 📊 **Penilaian Kualitas Koneksi Otomatis**
- ⏳ **Animasi Progress Bar & Catatan Waktu Tes**
- ⌨️ **Dukungan Shortcut Keyboard** (`Enter` untuk mulai, `Esc` untuk reset)
- 🏢 **Deteksi ISP & Alamat IP Publik**
- 📋 **Salin Ringkasan Hasil ke Clipboard**
- 📝 **Pencatatan Riwayat Pengujian Otomatis (`riwayat_speedtest.txt`)**

## 🛠️ Cara Menjalankan Aplikasi
1. Pastikan laptop terhubung ke jaringan internet/Wi-Fi.
2. Install pustaka yang dibutuhkan:
   ```bash
   pip install -r requirements.txt
   📊 Standar Penilaian Kualitas Koneksi
🚀 Koneksi Sangat Cepat: Download ≥ 20 Mbps

✅ Koneksi Stabil: Download 7 – 19.99 Mbps

⚠️ Koneksi Lambat: Download < 7 Mbps

✅ Skenario Pengujian Akhir (Checklist Demo)
Tes Koneksi Normal: Klik Mulai Tes (atau tekan Enter) saat Wi-Fi terhubung hingga muncul angka Ping, Download, Upload, Server, ISP, dan status kualitas.

Tes Responsivitas UI: Geser jendela aplikasi saat proses tes berlangsung untuk memastikan GUI tidak freeze (multithreading aktif).

Tes Utilitas: Klik Salin Hasil dan tempel (Ctrl + V) di Notepad, lalu cek file riwayat_speedtest.txt yang terbuat otomatis.

Tes Reset & Shortcut: Tekan tombol Reset (atau Esc) untuk mengembalikan tampilan ke kondisi awal.

Tes Penanganan Error: Matikan Wi-Fi lalu klik Mulai Tes untuk memastikan pesan error muncul dengan jelas tanpa aplikasi crash.