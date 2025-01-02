"""
Nama : Mohamad Firdiansyah
NIM  : 2402041
Kelas : 1A
"""
# Membuat sebuah tuple buah
buah = ("apel", "jeruk", "ceri", "durian", "apel", "mangga")
# 1. Mengambil tuple ke 2-5
print(buah[1:5])
# 2. Buat agar item "durian" dapat dihapus
list_buah = list(buah)
list_buah.pop(3)
buah = tuple(list_buah)
print(buah)
# 3. Buat agar ada tambahan item "Manggis" diantara item "jeruk" dan "ceri"
list_buah = list(buah)
list_buah.insert(2 , "Manggis")
buah = tuple(list_buah)
print(buah)