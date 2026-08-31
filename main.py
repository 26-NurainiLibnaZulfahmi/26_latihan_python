import mymodule

print(mymodule.cek_bilangan_prima(7))
print(mymodule.cek_ganjil_genap(14))
print(mymodule.huruf_besar("halo semua"))
print(mymodule.huruf_kecil("HALO SEMUA"))


def main():
    while True:
        print("\n=== MENU PROGRAM ===")
        print("1. Ganjil Genap")
        print("2. Bilangan Prima")
        print("3. Huruf Besar")
        print("4. Huruf Kecil")
        print("5. Exit")

        pilihan = input("Pilih menu (1-5): ")

        if pilihan == "1":
            angka = int(input("Masukkan angka: "))
            print(mymodule.cek_ganjil_genap(angka))
        elif pilihan == "2":
            angka = int(input("Masukkan angka: "))
            print(mymodule.cek_bilangan_prima(angka))
        elif pilihan == "3":
            kalimat = input("Masukkan kalimat: ")
            print(mymodule.huruf_besar(kalimat))
        elif pilihan == "4":
            kalimat = input("Masukkan kalimat: ")
            print(mymodule.huruf_kecil(kalimat))
        elif pilihan == "5":
            print("Terima kasih! Program selesai.")
            break
        else:
            print("Pilihan tidak valid. Silakan coba lagi.")


if __name__ == "__main__":
    main()
