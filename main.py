import tkinter as tk
from tkinter import ttk


class NetCheckApp:
    def __init__(self, root):
        self.root = root
        self.root.title("NetCheck Desktop")
        self.root.geometry("400x350")
        self.root.resizable(False, False)

        # Variabel yang terhubung ke label, kalau diubah tampilan ikut berubah
        self.ping_var = tk.StringVar(value="-")
        self.download_var = tk.StringVar(value="-")
        self.upload_var = tk.StringVar(value="-")
        self.status_var = tk.StringVar(value="Siap")

        self.build_ui()

    def build_ui(self):
        title = ttk.Label(self.root, text="NetCheck Desktop", font=("Arial", 18, "bold"))
        title.pack(pady=15)

        # Frame berisi tabel hasil (label kiri, nilai kanan)
        frame = ttk.Frame(self.root)
        frame.pack(pady=10)

        rows = [
            ("Ping (ms):", self.ping_var),
            ("Download (Mbps):", self.download_var),
            ("Upload (Mbps):", self.upload_var),
        ]
        for i, (teks, variabel) in enumerate(rows):
            ttk.Label(frame, text=teks, font=("Arial", 12)).grid(
                row=i, column=0, sticky="w", padx=10, pady=8
            )
            ttk.Label(frame, textvariable=variabel, font=("Arial", 12, "bold")).grid(
                row=i, column=1, sticky="e", padx=10, pady=8
            )

        self.start_button = ttk.Button(self.root, text="Mulai Tes", command=self.start_test)
        self.start_button.pack(pady=15)

        ttk.Label(self.root, textvariable=self.status_var).pack()

    def start_test(self):
        # Placeholder: logika tes asli ditambahkan di Step 3-5
        self.status_var.set("Fitur tes belum dibuat")


def main():
    root = tk.Tk()
    app = NetCheckApp(root)
    root.mainloop()


if __name__ == "__main__":
    main()