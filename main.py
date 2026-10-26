import tkinter as tk


def main():
    root = tk.Tk()
    root.title("NetCheck Desktop")
    root.geometry("400x300")

    label = tk.Label(root, text="NetCheck Desktop", font=("Arial", 16))
    label.pack(pady=20)

    root.mainloop()


if __name__ == "__main__":
    main()