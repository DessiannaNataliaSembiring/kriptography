def text_to_hex(text):
    """Konversi setiap karakter menjadi HEX (uppercase)."""
    return [format(ord(c), '02X') for c in text]

def to_matrix_4x4(hex_list):
    """Susun list HEX menjadi matriks 4x4 AES (kolom per kolom)."""
    matrix = [[0] * 4 for _ in range(4)]
    for i in range(16):
        row = i % 4
        col = i // 4
        matrix[row][col] = hex_list[i]
    return matrix

def print_matrix(matrix, title):
    """Print matriks dalam format AES 4x4."""
    print(f"\n=== {title} ===")
    for row in matrix:
        print(" ".join(row))

# -----------------------------
# Input Data
# -----------------------------
plaintext = "PRATIKUMKRIPTOGA"
cipherkey = "UNIKASANTOTHOMAS"

# Konversi ke HEX
hex_plain = text_to_hex(plaintext)
hex_key = text_to_hex(cipherkey)

# Susun menjadi matriks 4x4
matrix_plain = to_matrix_4x4(hex_plain)
matrix_key = to_matrix_4x4(hex_key)

# Cetak Hasil Akhir
print_matrix(matrix_plain, "PLAINTEXT (HEX) dalam Matriks 4x4")
print_matrix(matrix_key, "CIPHERKEY (HEX) dalam Matriks 4x4")
