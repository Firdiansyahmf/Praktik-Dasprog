"""
Nama : Mohamad Firdiansyah
NIM  : 2402041
Kelas : 1A
"""
"""
Program menginputkan angka yang berhenti
hingga bertemu input negatif. Angka positif
yang telah di input akan dijumlahkan.
"""
jumlahAngka=0
print("input: ")
while True:
    angka=int(input(""))
    if(angka<=0):
        break
    jumlahAngka += angka
print(f"\noutput:\ntotal = {jumlahAngka}")