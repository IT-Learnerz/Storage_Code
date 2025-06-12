import os
os.system('cls'if os.name == 'nt' else 'clear')


def tampilan():
    print("Pilih Menu: \n1. Luas Persegi \n2. Luas Lingkaran")

def luas_persegi():
    sisi =float(input("Masukkan Panjang sisi persegi: "))
    luas =sisi * sisi
    print(f"Luas persegi dengan sisi {sisi} adalah {luas}")

def luas_lingkaran():
    r=float(input("Masukkan Jari-Jari: "))
    luas= 3,14 * r * r
    print(f"Luas lingkaran dengan jari-jari: {r} adalah {luas} ")

def fungsi():
    pilihan = (input("Pilihan Anda: "))
    if pilihan == "1":
        luas_persegi()
    elif pilihan == "2":
        luas_lingkaran()
    else:
        print("Mangsud?")

tampilan()
fungsi()
