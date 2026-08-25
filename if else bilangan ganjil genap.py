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
