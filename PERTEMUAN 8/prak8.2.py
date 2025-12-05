def text_to_hex(text):
    """Konversi karakter ke HEX (uppercase)."""
    return [format(ord(c), '02X') for c in text]

def to_matrix_4x4(hex_list):
    """Susun 16 byte menjadi matriks 4x4 AES (kolom per kolom)."""
    matrix = [[0] * 4 for _ in range(4)]
    for i in range(16):
        row = i % 4
        col = i // 4
        matrix[row][col] = hex_list[i]
    return matrix

def xor_matrices(m1, m2):
    """XOR antara dua matriks 4x4 HEX."""
    result = [[0] * 4 for _ in range(4)]
    for r in range(4):
        for c in range(4):
            v1 = int(m1[r][c], 16)
            v2 = int(m2[r][c], 16)
            result[r][c] = format(v1 ^ v2, '02X')
    return result

def print_matrix(matrix, title):
    """Cetak matriks 4x4 dengan judul."""
    print(f"\n=== {title} ===")
    for row in matrix:
        print(" ".join(row))

# ---------------------------------------
# Input Data
# ---------------------------------------
plaintext = "PRATIKUMKRIPTOGA"
cipherkey = "UNIKASANTOTHOMAS"

# Konversi ke HEX
hex_plain = text_to_hex(plaintext)
hex_key = text_to_hex(cipherkey)

# Susun menjadi matriks 4x4 AES
matrix_plain = to_matrix_4x4(hex_plain)
matrix_key = to_matrix_4x4(hex_key)

# Tahap AddRoundKey (XOR)
matrix_xor = xor_matrices(matrix_plain, matrix_key)

# Output
print_matrix(matrix_plain, "PLAINTEXT (HEX)")
print_matrix(matrix_key, "CIPHERKEY (HEX)")
print_matrix(matrix_xor, "HASIL XOR (AddRoundKey)")
