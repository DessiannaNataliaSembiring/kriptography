# SistemBilangan.py
# Program konversi bilangan biner ke desimal menggunakan class

class Biner:
    @staticmethod
    def toDecimal(value: str):
        """
        Mengonversi bilangan biner ke desimal.
        Parameter:
            value (str): bilangan biner, misalnya '1010'
        Return:
            int: hasil konversi ke desimal
        """
        try:
            # Validasi agar hanya berisi 0 dan 1
            if not all(char in '01' for char in value):
                raise ValueError("Input hanya boleh mengandung angka 0 dan 1.")
            return int(value, 2)
        except ValueError as e:
            print(f"Terjadi kesalahan: {e}")
            return None


if __name__ == "__main__":
    print("=== Sistem Bilangan: Konversi Biner ke Desimal ===")

    biner_input = input("Masukkan bilangan biner: ").strip()
    hasil = Biner.toDecimal(biner_input)

    if hasil is not None:
        print(f"Bilangan desimal dari {biner_input} adalah {hasil}")
    else:
        print("Konversi gagal. Pastikan input berupa angka biner yang valid (0 atau 1).")
