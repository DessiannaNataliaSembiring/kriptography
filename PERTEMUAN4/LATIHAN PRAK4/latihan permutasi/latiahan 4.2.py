import itertools

def atur_buku(n, r):
    """
    Menghitung semua cara mengatur n buku di r rak.
    Asumsi: setiap buku bisa diletakkan di rak mana pun.
    """
    buku = [f"Buku{i+1}" for i in range(n)]
    rak = [f"Rak{j+1}" for j in range(r)]

    hasil = list(itertools.product(rak, repeat=n))  # kombinasi r^n

    print(f"\nTerdapat {len(hasil)} cara mengatur {n} buku ke {r} rak:\n")
    for i, kombinasi in enumerate(hasil, start=1):
        print(f"Cara {i}:")
        for b, r_ in zip(buku, kombinasi):
            print(f"  {b} → {r_}")
        print()

# Input dari user
print("\n=== PENGATURAN BUKU DI RAK ===")
n = int(input("Masukkan jumlah buku (n): "))
r = int(input("Masukkan jumlah rak (r): "))

atur_buku(n, r)
