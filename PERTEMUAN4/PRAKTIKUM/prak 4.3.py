# ==========================================================
# Program: Menghitung Kombinasi C(n, r)
# ==========================================================

def faktorial(x):
    """Fungsi untuk menghitung faktorial dari x"""
    if x == 0 or x == 1:
        return 1
    hasil = 1
    for i in range(2, x + 1):
        hasil *= i
    return hasil


def kombinasi(n, r):
    """Fungsi untuk menghitung kombinasi C(n, r) = n! / (r! * (n - r)!)"""
    if r > n:
        return 0
    faktorial_n = faktorial(n)
    faktorial_r = faktorial(r)
    faktorial_n_r = faktorial(n - r)
    return faktorial_n // (faktorial_r * faktorial_n_r)


# ==========================================================
# PROGRAM UTAMA
# ==========================================================
print("=== PROGRAM MENGHITUNG KOMBINASI C(n, r) ===")
n = int(input("Masukkan jumlah total objek (n): "))
r = int(input("Masukkan jumlah objek yang dipilih (r): "))

hasil = kombinasi(n, r)
print(f"\nJumlah kombinasi C({n}, {r}) adalah: {hasil}")
