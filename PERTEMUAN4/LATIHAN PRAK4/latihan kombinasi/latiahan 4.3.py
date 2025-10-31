import itertools

# ==========================================================
# FUNGSI FAKTORIAL
# ==========================================================
def faktorial(x):
    """Menghitung faktorial dari x"""
    if x == 0 or x == 1:
        return 1
    hasil = 1
    for i in range(2, x + 1):
        hasil *= i
    return hasil


# ==========================================================
# FUNGSI KOMBINASI
# ==========================================================
def kombinasi(n, r):
    """Menghitung nilai kombinasi C(n, r)"""
    if r > n:
        return 0
    faktorial_n = faktorial(n)
    faktorial_r = faktorial(r)
    faktorial_n_r = faktorial(n - r)
    return faktorial_n // (faktorial_r * faktorial_n_r)


# ==========================================================
# PROGRAM UTAMA
# ==========================================================
print("=== PROGRAM KOMBINASI DENGAN INISIAL HURUF ===")

# Input nilai n dan r
n = int(input("Masukkan jumlah total objek (n): "))
r = int(input("Masukkan jumlah objek yang dipilih (r): "))

# Buat daftar huruf inisial (A, B, C, D, ...)
huruf = [chr(65 + i) for i in range(n)]  # 65 = 'A' dalam ASCII

# Hitung nilai kombinasi
nilai_kombinasi = kombinasi(n, r)
print(f"\nJumlah kombinasi C({n}, {r}) adalah: {nilai_kombinasi}")

# Tampilkan semua hasil kombinasi
print("\nDaftar semua kombinasi yang mungkin:")
hasil_kombinasi = list(itertools.combinations(huruf, r))

for i, komb in enumerate(hasil_kombinasi, start=1):
    print(f"{i}. {', '.join(komb)}")

print("\nProgram selesai.")
