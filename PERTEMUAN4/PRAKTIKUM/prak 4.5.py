# Fungsi Transposisi Cipher
def transposisi_cipher(plaintext):
    # Tentukan panjang tiap bagian (dibagi 4 kolom)
    part_length = len(plaintext) // 4

    # Bagi teks menjadi beberapa bagian
    parts = [plaintext[i:i + part_length] for i in range(0, len(plaintext), part_length)]

    # Tampilkan proses pembentukan blok
    print("Bagian plaintext:")
    for i, part in enumerate(parts):
        print(f"Bagian {i + 1}: '{part}'")

    # Inisialisasi ciphertext kosong
    ciphertext = ""

    # Proses transposisi kolom demi kolom
    for col in range(4):
        for part in parts:
            if col < len(part):
                ciphertext += part[col]
                print(f"Menambahkan '{part[col]}' dari Bagian {parts.index(part) + 1} ke ciphertext.")

    # Kembalikan hasil ciphertext
    return ciphertext


# === Program Utama ===
plaintext = input("Masukkan plaintext: ")

# Panggil fungsi transposisi_cipher
ciphertext = transposisi_cipher(plaintext)

# Tampilkan hasil akhir
print(f"\nCiphertext: '{ciphertext}'")
