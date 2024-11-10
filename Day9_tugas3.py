"""
Nama : Mohamad Firdiansyah
NIM  : 2402041
Kelas : 1A
"""
# Program menghitung waktu berlari dan selesai berlari
def waktu():
    print("Input mulai:")
    jamA=int(input("Jam: "))
    menitA=int(input("Menit: "))
    detikA=int(input("Detik: "))
    print("Input selesai:")
    jamB=int(input("Jam: "))
    menitB=int(input("Menit: "))
    detikB=int(input("Detik: "))
    print("Hitung selisih:")
    print(f"Output: {jamB-jamA} jam - {menitB-menitA} menit - {detikB-detikA} detik")
    return
waktu()