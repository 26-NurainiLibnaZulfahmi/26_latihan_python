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
    return kalimat.upper()


def huruf_kecil(kalimat):
    return kalimat.lower()



