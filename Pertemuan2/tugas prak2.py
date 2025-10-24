import tkinter as tk
from tkinter import messagebox

# Fungsi untuk memproses ekspresi
def hitung():
    ekspresi = entry_input.get()

    try:
        # Menghapus spasi agar bisa memproses ekspresi tanpa spasi
        ekspresi_bersih = ekspresi.replace(" ", "")
        hasil = eval(ekspresi_bersih)

        # Menampilkan hasil di kolom output
        label_proses.config(text=f"Hasil Diproses: {ekspresi_bersih}")
        label_output.config(text=f"Output (Hasil): {hasil}")

    except Exception as e:
        messagebox.showerror("Error", f"Terjadi kesalahan: {e}")

# Membuat jendela utama
root = tk.Tk()
root.title("Kalkulator Hybrid")
root.geometry("400x250")
root.configure(bg="#f4f4f4")

# Judul
judul = tk.Label(root, text="Kalkulator Hybrid", font=("Arial", 16, "bold"), bg="#f4f4f4")
judul.pack(pady=10)

# Input ekspresi
frame_input = tk.Frame(root, bg="#f4f4f4")
frame_input.pack(pady=5)

label_input = tk.Label(frame_input, text="Input (Ekspresi):", font=("Arial", 11), bg="#f4f4f4")
label_input.grid(row=0, column=0, padx=5, pady=5)

entry_input = tk.Entry(frame_input, width=30, font=("Arial", 11))
entry_input.grid(row=0, column=1, padx=5, pady=5)

# Tombol hitung
btn_hitung = tk.Button(root, text="Hitung", command=hitung, font=("Arial", 11, "bold"), bg="#4CAF50", fg="white", width=10)
btn_hitung.pack(pady=10)

# Label hasil
label_proses = tk.Label(root, text="Hasil Diproses:", font=("Arial", 11), bg="#f4f4f4")
label_proses.pack()

label_output = tk.Label(root, text="Output (Hasil):", font=("Arial", 11), bg="#f4f4f4")
label_output.pack()

# Jalankan program
root.mainloop()
