# Fungsi untuk melakukan substitusi cipher
def substitusi_cipher(plaintext, aturan):
    ciphertext = ""
    for char in plaintext.upper():
        if char in aturan:               # Jika karakter ada dalam aturan substitusi
            ciphertext += aturan[char]   # Ganti dengan huruf sesuai aturan
        else:
            ciphertext += char           # Jika tidak ada (misalnya spasi atau tanda baca), biarkan
    return ciphertext


# === Aturan substitusi (dictionary) ===
aturan_substitusi = {
    'U': 'K',
    'N': 'N',
    'I': 'I',
    'K': 'K',
    'A': 'B'
}

# === Input plaintext dari pengguna ===
plaintext = input("Masukkan plaintext: ").upper()

# === Proses enkripsi menggunakan fungsi substitusi_cipher ===
ciphertext = substitusi_cipher(plaintext, aturan_substitusi)

# === Tampilkan hasil ===
print(f"Plaintext  : {plaintext}")
print(f"Ciphertext : {ciphertext}")
