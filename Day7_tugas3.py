"""
Nama : Mohamad Firdiansyah
NIM  : 2402041
Kelas : 1A
"""
"""
Leni ingin mengetahui deret angka dari 1-50
dimana saat bertemu kelipatan 5 maka outputnya adalah
"pass".
"""
angka = 0
for angka in range(1, 51):
    if angka%5==0:
        print("pass")
    else:
        print(angka)