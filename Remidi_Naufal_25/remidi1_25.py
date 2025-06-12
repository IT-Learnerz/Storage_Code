import os
os.system('cls' if os.name == 'nt' else 'clear')
isi = []

for i in range(0,5):
    val = int(input(f"Masukkan Bilangan ke-{i+1}: "))
    isi.append(val)

jumlah_genap=0
for num in isi:
    if num % 2 == 0:
        jumlah_genap += 1

print(f"Jumlah Bilangan genap: {jumlah_genap}")
