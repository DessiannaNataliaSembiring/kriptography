import itertools

# ==========================================================
# a. PERMUTASI MENYELURUH
# ==========================================================
def permutasi_menyeluruh(arr):
    """Menghasilkan semua permutasi dari seluruh elemen arr"""
    return list(itertools.permutations(arr))

# Contoh penggunaan
data1 = [1, 2, 3]
print("=== Permutasi Menyeluruh ===")
for p in permutasi_menyeluruh(data1):
    print(p)
print()


# ==========================================================
# b. PERMUTASI SEBAGIAN
# ==========================================================
def permutasi_sebagian(arr, k):
    """Menghasilkan semua permutasi dari sebagian elemen arr sebanyak k"""
    return list(itertools.permutations(arr, k))

# Contoh penggunaan
data2 = [1, 2, 3, 4]
print("=== Permutasi Sebagian (k=2) ===")
for p in permutasi_sebagian(data2, 2):
    print(p)
print()


# ==========================================================
# c. PERMUTASI KELILING
# ==========================================================
def permutasi_keliling(arr):
    """
    Permutasi keliling (circular permutation):
    Elemen dianggap dalam bentuk siklus, urutan rotasi dianggap sama.
    """
    if len(arr) == 1:
        return [arr]
    pertama = arr[0]
    permutasi_penuh = list(itertools.permutations(arr[1:]))
    return [[pertama] + list(perm) for perm in permutasi_penuh]

# Contoh penggunaan
data3 = [1, 2, 3]
print("=== Permutasi Keliling ===")
for p in permutasi_keliling(data3):
    print(p)
print()


# ==========================================================
# d. PERMUTASI DATA BERKELOMPOK
# ==========================================================
def permutasi_berkelompok(grup):
    """
    Permutasi data berkelompok: setiap kelompok diubah urutannya sendiri,
    lalu dikombinasikan dengan kelompok lain.
    """
    hasil = [[]]
    for kelompok in grup:
        hasil_baru = []
        for hsl in hasil:
            for perm in itertools.permutations(kelompok):
                hasil_baru.append(hsl + list(perm))
        hasil = hasil_baru
    return hasil

# Contoh penggunaan
grup_data = [[1, 2], [3, 4]]
print("=== Permutasi Data Berkelompok ===")
for p in permutasi_berkelompok(grup_data):
    print(p)
print()
