class Mobil:
    def __init__(self, warna, merek, kecepatan):
        self.warna = warna
        self.merek = merek
        self.kecepatan = kecepatan

    def jalan(self):
        if self.kecepatan <= 70:
            print(f"Warna Mobil: {self.warna} dan mereknya: {self.merek} berjalan santai dengan kecepatan {self.kecepatan}")
        else:
            print(f"Warna Mobil: {self.warna} dan mereknya: {self.merek} berjalan dengan kencang pada kecepatan {self.kecepatan}")

# Input dari user
warna1 = "Hitam"
merek1 = "Subaru"
kecepatan1 = int(input("Masukin Speed Mobil 1: "))

warna2 = "Putih"
merek2 = "BMW"
kecepatan2 = int(input("Masukin Speed Mobil 2: "))

# Membuat objek mobil
mobil1 = Mobil(warna1, merek1, kecepatan1)
mobil2 = Mobil(warna2, merek2, kecepatan2)

# Memanggil method jalan() untuk setiap mobil
mobil1.jalan()
mobil2.jalan()
