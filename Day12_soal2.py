"""
Nama : Mohamad Firdiansyah
NIM  : 2402041
Kelas : 1A
"""
# Studi Daftar Mahasiswa RPL UPI
def linearSearch(arrMahasiswaRpl, target):
    for i in range(len(arrMahasiswaRpl)):
        if arrMahasiswaRpl[i] == target:
            return i
    return -1

arrMahasiswaRpl = [
    "Firdi", "Edo", "Jerem", "Ardi", "Rian",
    "Dika", "Fajar", "Novi", "Winda", "Siti",
    "Bagas", "Deni", "Lila", "Yuni", "Indra", 
    "Tika", "Rama", "Lutfi", "Reza", "Fier"
]


target = input("Masukkan nama Mahasiswa RPL UPI: ")
hasil = linearSearch(arrMahasiswaRpl, target)
if hasil != -1:
    print(f"Linear Search: Elemen ditemukan di index {hasil}")
else:
    print("Linear Search: Elemen tidak ditemukan")