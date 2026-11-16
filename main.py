import tkinter as tk
from tkinter import ttk
import speedtest
import threading
from datetime import datetime


class NetCheckApp:

    def __init__(self, root):
        self.root = root
        self.root.title("NetCheck Desktop")
        self.root.geometry("400x430")
        self.root.resizable(False, False)
        self.root.configure(bg="#f0f4f8")

        style = ttk.Style()
        style.configure("TFrame", background="#f0f4f8")
        style.configure("TLabel", background="#f0f4f8", foreground="#1e293b")

        # Judul dengan Icon Emoji
        title_label = ttk.Label(
            root, text="⚡ NetCheck Desktop", font=("Helvetica", 16, "bold")
        )
        title_label.pack(pady=18)

        # Frame Hasil
        frame = ttk.Frame(root)
        frame.pack(pady=10, padx=20)

        ttk.Label(
            frame, text="Ping (ms):", font=("Helvetica", 10, "bold")
        ).grid(row=0, column=0, sticky="w", pady=6)
        self.lbl_ping = ttk.Label(frame, text="-", font=("Helvetica", 10))
        self.lbl_ping.grid(row=0, column=1, sticky="e", padx=30)

        ttk.Label(
            frame, text="Download (Mbps):", font=("Helvetica", 10, "bold")
        ).grid(row=1, column=0, sticky="w", pady=6)
        self.lbl_download = ttk.Label(frame, text="-", font=("Helvetica", 10))
        self.lbl_download.grid(row=1, column=1, sticky="e", padx=30)

        ttk.Label(
            frame, text="Upload (Mbps):", font=("Helvetica", 10, "bold")
        ).grid(row=2, column=0, sticky="w", pady=6)
        self.lbl_upload = ttk.Label(frame, text="-", font=("Helvetica", 10))
        self.lbl_upload.grid(row=2, column=1, sticky="e", padx=30)

        ttk.Label(
            frame, text="Server:", font=("Helvetica", 10, "bold")
        ).grid(row=3, column=0, sticky="w", pady=6)
        self.lbl_server = ttk.Label(frame, text="-", font=("Helvetica", 9))
        self.lbl_server.grid(row=3, column=1, sticky="e", padx=30)

        # Tombol Tes
        self.btn_start = ttk.Button(
            root, text="Mulai Tes", command=self.start_test
        )
        self.btn_start.pack(pady=8)

        # Tombol Reset Hasil
        self.btn_reset = ttk.Button(
            root, text="Reset", command=self.reset_results
        )
        self.btn_reset.pack(pady=5)

        # Status
        self.s_var = tk.StringVar(value="Siap")
        self.lbl_status = ttk.Label(
            root, textvariable=self.s_var, font=("Helvetica", 9, "italic")
        )
        self.lbl_status.pack(pady=5)

        # Waktu Pengujian Terakhir
        self.lbl_time = ttk.Label(
            root, text="Terakhir dites: -", font=("Helvetica", 8), foreground="#64748b"
        )
        self.lbl_time.pack(pady=8)

    def reset_results(self):
        """Fungsi untuk membersihkan tampilan hasil pengujian"""
        self.lbl_ping.config(text="-")
        self.lbl_download.config(text="-")
        self.lbl_upload.config(text="-")
        self.lbl_server.config(text="-")
        self.lbl_time.config(text="Terakhir dites: -")
        self.s_var.set("Siap")

    def run_speedtest(self):
        try:
            self.s_var.set("🔍 Mencari server terbaik...")
            st = speedtest.Speedtest()
            st.get_best_server()

            server_info = st.results.server
            nama_server = f"{server_info['sponsor']} ({server_info['name']})"
            self.lbl_server.config(text=nama_server)

            self.s_var.set("📡 Mengukur Ping...")
            ping = st.results.ping
            self.lbl_ping.config(text=f"{ping:.0f}")

            self.s_var.set("📥 Mengukur kecepatan Download...")
            download_speed = st.download() / 1_000_000
            self.lbl_download.config(text=f"{download_speed:.2f}")

            self.s_var.set("📤 Mengukur kecepatan Upload...")
            upload_speed = st.upload() / 1_000_000
            self.lbl_upload.config(text=f"{upload_speed:.2f}")

            if download_speed >= 20:
                kualitas = "🚀 Koneksi Sangat Cepat"
            elif download_speed >= 7:
                kualitas = "✅ Koneksi Stabil"
            else:
                kualitas = "⚠️ Koneksi Lambat"

            self.s_var.set(f"Pengujian Selesai! ({kualitas})")
            waktu_sekarang = datetime.now().strftime("%H:%M:%S")
            self.lbl_time.config(text=f"Terakhir dites: {waktu_sekarang}")

        except speedtest.ConfigRetrievalError:
            self.s_var.set("❌ Gagal: Tidak dapat terhubung ke server speedtest")
        except speedtest.NoMatchedServers:
            self.s_var.set("❌ Gagal: Server tidak ditemukan, cek Wi-Fi Anda")
        except Exception:
            self.s_var.set("❌ Gagal: Terjadi gangguan koneksi jaringan")
        finally:
            self.btn_start.config(state="normal")

    def start_test(self):
        self.btn_start.config(state="disabled")
        self.lbl_ping.config(text="-")
        self.lbl_download.config(text="-")
        self.lbl_upload.config(text="-")
        self.lbl_server.config(text="-")

        threading.Thread(target=self.run_speedtest, daemon=True).start()


if __name__ == "__main__":
    root = tk.Tk()
    app = NetCheckApp(root)
    root.mainloop()