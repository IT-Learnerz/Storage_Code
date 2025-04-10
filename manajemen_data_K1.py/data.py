daftar_siswa = []


def tambah_siswa():
    nama = input("masukkan nama: ")
    usia = input("masukkan usia: ")
    nilai = input("masukkan nilai rata rata: ")
    daftar_siswa.append ({"nama" : nama, "usia" : usia, "nilai rata rata" : nilai})
    print("siswa berhasil ditambahkan")
tambah_siswa()



def tampilkan_menu():
    print("\n pilih menu")
    print("1. tambah siswa")
    print("2. lihat data siswa")
    print("3. edit data siswa")
    print("4. hapus data siswa")
    print("5. keluar")
