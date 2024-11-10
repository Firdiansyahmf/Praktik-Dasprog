"""
Nama : Mohamad Firdiansyah
NIM  : 2402041
Kelas : 1A
"""
# Membuat sebuah list buah
buah = ["apel", "jeruk", "ceri", "durian", "apel", "mangga"]
# 1. Mengambil list ke 2-5
print(buah[1:5])
# 2. Hapus item "apel" yang kedua
buah.pop(4)
print(buah)
# 3. Ganti item dengan nama "ceri" menjadi "cherry"
buah[2] = "cherry"
print(buah)
# 4. Tambah item dengan nama "strawberry" ke dalam index ke-3
buah.insert(3, "strawberry")
print(buah)
# 5. Urutkan item pada list sesuai dengan abjadnya
buah.sort()
print(buah)