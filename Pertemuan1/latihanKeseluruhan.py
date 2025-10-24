import tkinter as tk
from tkinter import messagebox

# ============= LATIHAN 1 =============
def latihan1():
    def hitung():
        try:
            a = float(entry1.get())
            b = float(entry2.get())
            hasil = f"""
Penjumlahan: {a+b}
Pengurangan: {a-b}
Perkalian  : {a*b}
Pembagian  : {a/b if b != 0 else 'Error: Tidak bisa dibagi nol'}
"""
            messagebox.showinfo("Hasil Latihan 1", hasil)
        except ValueError:
            messagebox.showerror("Error", "Masukkan angka yang valid!")

    win = tk.Toplevel(root)
    win.title("Latihan 1 - Aritmatika Dasar")
    win.geometry("300x200")

    tk.Label(win, text="Masukkan angka pertama:").pack()
    entry1 = tk.Entry(win)
    entry1.pack()

    tk.Label(win, text="Masukkan angka kedua:").pack()
    entry2 = tk.Entry(win)
    entry2.pack()

    tk.Button(win, text="Hitung", command=hitung).pack(pady=5)
    tk.Button(win, text="Kembali ke Menu Utama", command=win.destroy).pack(pady=5)


# ============= LATIHAN 2 =============
def latihan2():
    def hitung():
        try:
            a = float(entry1.get())
            b = float(entry2.get())
            op = entry_op.get()
            if op == '+':
                hasil = a+b
            elif op == '-':
                hasil = a-b
            elif op == '*':
                hasil = a*b
            elif op == '/':
                hasil = a/b if b != 0 else "Error: Nol"
            else:
                hasil = "Operator tidak valid!"
            messagebox.showinfo("Hasil Latihan 2", f"Hasil: {hasil}")
        except ValueError:
            messagebox.showerror("Error", "Masukkan angka yang valid!")

    win = tk.Toplevel(root)
    win.title("Latihan 2 - Kalkulator Sederhana")
    win.geometry("300x220")

    tk.Label(win, text="Masukkan angka pertama:").pack()
    entry1 = tk.Entry(win)
    entry1.pack()

    tk.Label(win, text="Masukkan angka kedua:").pack()
    entry2 = tk.Entry(win)
    entry2.pack()

    tk.Label(win, text="Operator (+, -, *, /):").pack()
    entry_op = tk.Entry(win)
    entry_op.pack()

    tk.Button(win, text="Hitung", command=hitung).pack(pady=5)
    tk.Button(win, text="Kembali ke Menu Utama", command=win.destroy).pack(pady=5)


# ============= LATIHAN 3 =============
def latihan3():
    def hitung():
        try:
            sikap = float(e1.get())
            tugas = float(e2.get())
            uts   = float(e3.get())
            uas   = float(e4.get())
            total = (sikap*0.10)+(tugas*0.30)+(uts*0.25)+(uas*0.35)

            if 81 <= total <= 100:
                huruf, bobot = "A", 4
            elif total >= 76:
                huruf, bobot = "B+", 3.5
            elif total >= 71:
                huruf, bobot = "B", 3
            elif total >= 66:
                huruf, bobot = "C+", 2.5
            elif total >= 56:
                huruf, bobot = "C", 2
            elif total >= 46:
                huruf, bobot = "D", 1
            else:
                huruf, bobot = "E", 0

            ket = "Lulus" if total >= 56 else "Tidak Lulus"

            hasil = f"Total: {total:.2f}\nNilai Huruf: {huruf} (Bobot {bobot})\nKeterangan: {ket}"
            messagebox.showinfo("Hasil Nilai Akhir", hasil)
        except ValueError:
            messagebox.showerror("Error", "Masukkan nilai angka yang valid!")

    win = tk.Toplevel(root)
    win.title("Latihan 3 - Hitung Nilai Akademik")
    win.geometry("300x300")

    tk.Label(win, text="Nilai Sikap/Kehadiran:").pack()
    e1 = tk.Entry(win); e1.pack()

    tk.Label(win, text="Nilai Tugas:").pack()
    e2 = tk.Entry(win); e2.pack()

    tk.Label(win, text="Nilai UTS:").pack()
    e3 = tk.Entry(win); e3.pack()

    tk.Label(win, text="Nilai UAS:").pack()
    e4 = tk.Entry(win); e4.pack()

    tk.Button(win, text="Hitung Nilai", command=hitung).pack(pady=5)
    tk.Button(win, text="Kembali ke Menu Utama", command=win.destroy).pack(pady=5)


# ============= MENU UTAMA =============
root = tk.Tk()
root.title("Menu Utama Latihan Python")
root.geometry("350x250")

tk.Label(root, text="=== MENU UTAMA ===", font=("Arial", 14, "bold")).pack(pady=15)

tk.Button(root, text="Latihan 1 - Aritmatika Dasar", command=latihan1, width=30).pack(pady=5)
tk.Button(root, text="Latihan 2 - Kalkulator", command=latihan2, width=30).pack(pady=5)
tk.Button(root, text="Latihan 3 - Nilai Akademik", command=latihan3, width=30).pack(pady=5)

root.mainloop()
