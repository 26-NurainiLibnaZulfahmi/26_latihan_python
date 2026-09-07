import sqlite3

def init_database():
    conn = sqlite3.connect("data_fungsi_program.db")
    cursor = conn.cursor()
    
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT UNIQUE,
            password TEXT
        )
    ''')
    
    conn.commit()
    conn.close()
    print("Database dan tabel 'users' berhasil disiapkan!")

init_database()

---------------------------------------------------------------------------------------------------------------

import sqlite3

def register_user(username, password):
    try:
        conn = sqlite3.connect("data_fungsi_program.db")
        cursor = conn.cursor()
        cursor.execute("INSERT INTO users (username, password) VALUES (?, ?)", (username, password))
        conn.commit()
        conn.close()
        return "Registrasi berhasil!"
    except sqlite3.IntegrityError:
        return "Username kamu sudah terdaftar!"

def login_user(username, password):
    conn = sqlite3.connect("data_fungsi_program.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users WHERE username = ? AND password = ?", (username, password))
    user = cursor.fetchone()
    conn.close()
    
    if user is not None:
        return True  
    else:
        return False


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

---------------------------------------------------------------------------------------------------------------

from my_module import register_user, login_user, cek_ganjil_genap, cek_bilangan_prima, huruf_besar, huruf_kecil

while True:
    print("\n=== PROGRAM UTAMA ===")
    print("1. Register")
    print("2. Login")
    print("3. Keluar")
    pilihan = input("Pilih menu (1/2/3): ")

    if pilihan == "1":
        username = input("Masukkan username baru: ")
        password = input("Masukkan password baru: ")
        print(register_user(username, password))

    elif pilihan == "2":
        username = input("Masukkan username: ")
        password = input("Masukkan password: ")
        
        if login_user(username, password):
            print("\n=== LOGIN BERHASIL! Selamat Datang ===")
            print(cek_ganjil_genap(10))
            print(cek_bilangan_prima(8))
            print(huruf_besar("halo semua"))
            print(huruf_kecil("HALO SEMUA"))
        else:
            print("\nLogin GAGAL! Username atau password salah.")

    elif pilihan == "3":
        print("Terima kasih! Program telah selesai.")
        break  # Menghentikan perulangan while True

    else:
        print("Pilihan tidak valid, silakan coba lagi!")
