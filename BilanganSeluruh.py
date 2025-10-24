# BilanganSeluruh.py
# Program konversi bilangan OKTAL ke DESIMAL, BINER, dan HEKSADESIMAL

class Oktal:
    @staticmethod
    def toDecimal(value: str):
        """
        Mengonversi bilangan oktal ke desimal.
        Parameter:
            value (str): bilangan oktal (misalnya '17')
        Return:
            int: hasil konversi ke desimal
        """
        try:
            # Validasi: hanya digit 0–7 yang diperbolehkan
            if not all(char in '01234567' for char in value):
                raise ValueError("Input hanya boleh berisi angka 0 sampai 7.")
            return int(value, 8)
        except ValueError as e:
            print(f"Terjadi kesalahan: {e}")
            return None

    @staticmethod
    def toBinary(value: str):
        """
        Mengonversi bilangan oktal ke biner.
        """
        desimal = Oktal.toDecimal(value)
        if desimal is not None:
            return bin(desimal)[2:]
        return None

    @staticmethod
    def toHex(value: str):
        """
        Mengonversi bilangan oktal ke heksadesimal.
        """
        desimal = Oktal.toDecimal(value)
        if desimal is not None:
            return hex(desimal)[2:].upper()  # [2:] hilangkan '0x'
        return None


if __name__ == "__main__":
    print("=== SISTEM BILANGAN: Konversi OKTAL ke DESIMAL, BINER, dan HEKSA ===")

    oktal_input = input("Masukkan bilangan oktal: ").strip()
    
    desimal = Oktal.toDecimal(oktal_input)
    biner = Oktal.toBinary(oktal_input)
    heksa = Oktal.toHex(oktal_input)

    if desimal is not None:
        print(f"\nHasil konversi dari oktal {oktal_input}:")
        print(f"Desimal     : {desimal}")
        print(f"Biner       : {biner}")
        print(f"Heksadesimal: {heksa}")
    else:
        print("Konversi gagal. Pastikan input hanya berisi angka 0 sampai 7.")
