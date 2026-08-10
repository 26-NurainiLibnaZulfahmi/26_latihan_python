while True:
    print("\n--- CEK BILANGAN GANJIL ATAU GENAP ---")
    angka = int(input("Masukkan angka: "))
    if angka % 2 == 0:
        print(f"angka {angka} adalah bilangan genap")  
    else:
        print(f"angka {angka} adalah bilangan ganjil")
