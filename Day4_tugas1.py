"""
Nama : Mohamad Firdiansyah
NIM  : 2402041
Kelas : 1A
"""
# Diketahui Input:
numbers = [10, 20, 20, 30, 40, 50, 50, 60] 
# Konversi ke set untuk menghilangkan duplikasi
numbers = set(numbers)
# Konversi kembali ke list dan menggunakan fungsi sorted() untuk urutannya
numbers = list(sorted(numbers))
print(numbers)