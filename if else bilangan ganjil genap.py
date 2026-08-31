bilangan = int(input("Masukkan bilangan: "))
ganjil_genap = "Bilangan ganjil" if bilangan % 2 !=0 else "Bilangan genap"
print("Bilangan", bilangan, "adalah", ganjil_genap)


print("--------------------------------------------")


while True:
    print("\n--- CEK BILANGAN GANJIL ATAU GENAP ---")
    angka = int(input("Masukkan angka: "))
    if angka % 2 == 0:
        print(f"angka {angka} adalah bilangan genap")  
    else:
        print(f"angka {angka} adalah bilangan ganjil")


print("--------------------------------------------")


def cek_ganjil_genap(angka):
    if angka % 2 == 0:
        return f"{angka} adalah bilangan Genap."
    else:
        return f"{angka} adalah bilangan Ganjil."


def cek_bilangan_prima(angka):
    if angka < 2:
        return f"{angka} bukan bilangan prima."

    for i in range(2, int(angka**0.5) + 1):
        if angka % i == 0:
            return f"{angka} bukan bilangan prima."

    return f"{angka} adalah bilangan Prima."


def huruf_besar(kalimat):
    kalimat = input ("Masukkan kalimat dengan huruf kecil: ")
    print("Kalimat dalam huruf besar:", huruf_besar(kalimat))
    return kalimat.upper()


def huruf_kecil(kalimat):
    kalimat = input ("Masukkan kalimat dengan huruf besar: ")
    print("Kalimat dalam huruf kecil:", huruf_kecil(kalimat))
    return kalimat.lower()


print("--------------------------------------------")


def main():
    while True:
        print("\n=== MENU PROGRAM ===")
        print("1. Ganjil Genap")
        print("2. Bilangan Prima")
        print("3. Exit")

        pilihan = input("Pilih menu diatas (1-3): ")

        if pilihan == "1":
            angka = int(input("Masukkan angka: "))
            print(cek_ganjil_genap(angka))
        elif pilihan == "2":
            angka = int(input("Masukkan angka: "))
            print(cek_bilangan_prima(angka))
        elif pilihan == "3":
            print("Program selesai. Terima kasih!")
            break
        else:
            print("Pilihan tidak valid. Coba lagi")


if __name__ == "__main__":
    main()
