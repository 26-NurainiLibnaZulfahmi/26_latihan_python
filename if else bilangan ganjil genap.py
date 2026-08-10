while True:
    print("\n--- CEK BILANGAN GANJIL ATAU GENAP ---")
    
    # Meminta pengguna untuk memasukkan angka
    angka = int(input("Masukkan angka: "))
    
    # Memeriksa apakah angka habis dibagi 2 atau tidak
    if angka % 2 == 0:
        print(f"{angka} adalah bilangan genap")  
    else:
        print(f"{angka} adalah bilangan ganjil")
    
