"""
Nama : Mohamad Firdiansyah
NIM  : 2402041
Kelas : 1A
"""
angka = int(input("Masukkan angka: "))
if (angka > 0):
    if (angka%2==1):
        print(f"{angka} adalah bilangan positif dan termasuk bilangan ganjil")
    else:
        print(f"{angka} adalah bilangan positif dan termasuk bilangan genap")
elif (angka==0):
    print(f"{angka} adalah bukan bilangan positif maupun negatif dan termasuk bilangan genap")
else: 
    if (angka%2==1):
        print(f"{angka} adalah bilangan negatif dan termasuk bilangan ganjil")
    else:
        print(f"{angka} adalah bilangan negatif dan termasuk bilangan genap")