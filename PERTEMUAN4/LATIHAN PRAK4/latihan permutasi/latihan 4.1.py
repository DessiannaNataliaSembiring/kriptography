import itertools

def permutasi_menyeluruh(arr):
    return list(itertools.permutations(arr))

def permutasi_sebagian(arr, k):
    return list(itertools.permutations(arr, k))

def permutasi_keliling(arr):
    if len(arr) == 1:
        return [arr]
    pertama = arr[0]
    permutasi_penuh = list(itertools.permutations(arr[1:]))
    return [[pertama] + list(perm) for perm in permutasi_penuh]

def permutasi_berkelompok(grup):
    hasil = [[]]
    for kelompok in grup:
        hasil_baru = []
        for hsl in hasil:
            for perm in itertools.permutations(kelompok):
                hasil_baru.append(hsl + list(perm))
        hasil = hasil_baru
    return hasil


def menu():
    print("\n=== PROGRAM PERMUTASI ===")
    print("1. Permutasi Menyeluruh")
    print("2. Permutasi Sebagian")
    print("3. Permutasi Keliling")
    print("4. Permutasi Berkelompok")
    print("0. Keluar")

    while True:
        pilih = input("\nPilih jenis permutasi (0-4): ")

        if pilih == '1':
            data = input("Masukkan elemen (pisahkan dengan spasi): ").split()
            hasil = permutasi_menyeluruh(data)
            print("\nHasil Permutasi Menyeluruh:")
            for h in hasil:
                print(h)

        elif pilih == '2':
            data = input("Masukkan elemen (pisahkan dengan spasi): ").split()
            k = int(input("Masukkan nilai k: "))
            hasil = permutasi_sebagian(data, k)
            print("\nHasil Permutasi Sebagian:")
            for h in hasil:
                print(h)

        elif pilih == '3':
            data = input("Masukkan elemen (pisahkan dengan spasi): ").split()
            hasil = permutasi_keliling(data)
            print("\nHasil Permutasi Keliling:")
            for h in hasil:
                print(h)

        elif pilih == '4':
            jml_grup = int(input("Masukkan jumlah kelompok: "))
            grup = []
            for i in range(jml_grup):
                elemen = input(f"Masukkan elemen untuk kelompok {i+1} (pisahkan dengan spasi): ").split()
                grup.append(elemen)
            hasil = permutasi_berkelompok(grup)
            print("\nHasil Permutasi Berkelompok:")
            for h in hasil:
                print(h)

        elif pilih == '0':
            print("Program selesai.")
            break
        else:
            print("Pilihan tidak valid, coba lagi.")

# Jalankan menu interaktif
menu()
