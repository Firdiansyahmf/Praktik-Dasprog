"""
Nama : Mohamad Firdiansyah
NIM  : 2402041
Kelas : 1A
"""
# Studi Kasus Toko
def linearSearch(arrBarang, target):
    for i in range(len(arrBarang)):
        if arrBarang[i] == target:
            return i
    return -1

arrBarang = [
    "Air Mineral", "Bawang Merah", "Kunyit", "Tahu", "Tempe",
    "Kecap", "Telur", "Gula", "Beras", "Wortel",
    "Sawi", "Bayam", "Tomat", "Kangkung", "Kemiri"
]

target = input("Masukkan nama barang: ")
hasil = linearSearch(arrBarang, target)
if hasil != -1:
    print(f"Linear Search: Elemen ditemukan di index {hasil}")
else:
    print("Linear Search: Elemen tidak ditemukan")