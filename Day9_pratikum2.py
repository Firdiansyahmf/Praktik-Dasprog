"""
Nama : Mohamad Firdiansyah
NIM  : 2402041
Kelas : 1A
"""
# Menghitung fungsi nilai total dan nilai rata-rata berdasarkan nilai yang diinputkan dari nilai total
def nilai(*angka):
    total = sum(angka)
    rataRata = total/len(angka)
    print(f"Total={total}")
    print(f"Rata-rata={rataRata}")
    return total, rataRata
nilai(2,3,5,10)
