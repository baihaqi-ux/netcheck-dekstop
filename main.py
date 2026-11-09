import tkinter as tk
from tkinter import ttk
import speedtest
import threading

class NetCheckApp:
    def __init__(self, root):
        self.root = root
        self.root.title("NetCheck Desktop")
        self.root.geometry("380x350")
        self.root.resizable(False, False)

        # Judul
        title_label = ttk.Label(root, text="NetCheck Desktop", font=("Helvetica", 16, "bold"))
        title_label.pack(pady=15)

        # Frame Hasil
        frame = ttk.Frame(root)
        frame.pack(pady=10, padx=20)

        ttk.Label(frame, text="Ping (ms):", font=("Helvetica", 10, "bold")).grid(row=0, column=0, sticky="w", pady=6)
        self.lbl_ping = ttk.Label(frame, text="-", font=("Helvetica", 10))
        self.lbl_ping.grid(row=0, column=1, sticky="e", padx=30)

        ttk.Label(frame, text="Download (Mbps):", font=("Helvetica", 10, "bold")).grid(row=1, column=0, sticky="w", pady=6)
        self.lbl_download = ttk.Label(frame, text="-", font=("Helvetica", 10))
        self.lbl_download.grid(row=1, column=1, sticky="e", padx=30)

        ttk.Label(frame, text="Upload (Mbps):", font=("Helvetica", 10, "bold")).grid(row=2, column=0, sticky="w", pady=6)
        self.lbl_upload = ttk.Label(frame, text="-", font=("Helvetica", 10))
        self.lbl_upload.grid(row=2, column=1, sticky="e", padx=30)

        # Tombol Tes
        self.btn_start = ttk.Button(root, text="Mulai Tes", command=self.start_test)
        self.btn_start.pack(pady=15)

        # Status
        self.s_var = tk.StringVar(value="Siap")
        self.lbl_status = ttk.Label(root, textvariable=self.s_var, font=("Helvetica", 9, "italic"))
        self.lbl_status.pack(pady=5)

    def run_speedtest(self):
        try:
            self.s_var.set("Mencari server terbaik...")
            st = speedtest.Speedtest()
            st.get_best_server()

            self.s_var.set("Mengukur Ping...")
            ping = st.results.ping
            self.lbl_ping.config(text=f"{ping:.0f}")

            self.s_var.set("Mengukur kecepatan Download...")
            download_speed = st.download() / 1_000_000
            self.lbl_download.config(text=f"{download_speed:.2f}")

            self.s_var.set("Mengukur kecepatan Upload...")
            upload_speed = st.upload() / 1_000_000
            self.lbl_upload.config(text=f"{upload_speed:.2f}")

            self.s_var.set("Pengujian Selesai!")

        except Exception:
            self.s_var.set("Gagal: Periksa koneksi Wi-Fi Anda")
        finally:
            self.btn_start.config(state="normal")

    def start_test(self):
        self.btn_start.config(state="disabled")
        self.lbl_ping.config(text="-")
        self.lbl_download.config(text="-")
        self.lbl_upload.config(text="-")
        
        # Threading agar UI tidak Not Responding saat proses tes
        threading.Thread(target=self.run_speedtest, daemon=True).start()

if __name__ == "__main__":
    root = tk.Tk()
    app = NetCheckApp(root)
    root.mainloop()