# Bilangan3.py
# Program konversi bilangan HEXA ke DESIMAL, BINER, dan OKTAL

class Hexa:
    @staticmethod
    def toDecimal(value: str):
        """
        Mengonversi bilangan heksadesimal ke desimal.
        Parameter:
            value (str): bilangan heksadesimal, misalnya '1A'
        Return:
            int: hasil konversi ke desimal
        """
        try:
            # Validasi: hanya karakter 0–9 dan A–F (atau a–f)
            if not all(c.upper() in '0123456789ABCDEF' for c in value):
                raise ValueError("Input hanya boleh berisi karakter 0-9 atau A-F.")
            return int(value, 16)
        except ValueError as e:
            print(f"Terjadi kesalahan: {e}")
            return None

    @staticmethod
    def toBinary(value: str):
        """
        Mengonversi bilangan heksadesimal ke biner.
        """
        desimal = Hexa.toDecimal(value)
        if desimal is not None:
            return bin(desimal)[2:]
        return None

    @staticmethod
    def toOctal(value: str):
        """
        Mengonversi bilangan heksadesimal ke oktal.
        """
        desimal = Hexa.toDecimal(value)
        if desimal is not None:
            return oct(desimal)[2:]
        return None


if __name__ == "__main__":
    print("=== SISTEM BILANGAN: Konversi HEXADESIMAL ke DESIMAL, BINER, dan OKTAL ===")

    heksa_input = input("Masukkan bilangan heksadesimal (0-9, A-F): ").strip().upper()

    desimal = Hexa.toDecimal(heksa_input)
    biner = Hexa.toBinary(heksa_input)
    oktal = Hexa.toOctal(heksa_input)

    if desimal is not None:
        print(f"\nHasil konversi dari heksadesimal {heksa_input}:")
        print(f"Desimal : {desimal}")
        print(f"Biner   : {biner}")
        print(f"Oktal   : {oktal}")
    else:
        print("Konversi gagal. Pastikan input hanya berisi angka 0-9 dan huruf A-F.")
