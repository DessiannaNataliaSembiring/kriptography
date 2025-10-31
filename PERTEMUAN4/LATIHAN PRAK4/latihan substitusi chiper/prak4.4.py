# ==========================================================
# LATIHAN: SUBSTITUSI CIPHER DASAR
# ==========================================================

print("=== LATIHAN SUBSTITUSI CIPHER ===")

# Input plaintext dan aturan substitusi sederhana
plaintext = input("Masukkan plaintext: ").upper()
huruf_asal = input("Masukkan huruf yang akan diganti: ").upper()
huruf_baru = input("Masukkan huruf pengganti: ").upper()

ciphertext = ""
for h in plaintext:
    if h == huruf_asal:
        ciphertext += huruf_baru
    else:
        ciphertext += h

print(f"\nHasil substitusi huruf {huruf_asal} → {huruf_baru}:")
print(f"Ciphertext: {ciphertext}")
