"""
Nama : Mohamad Firdiansyah
NIM  : 2402041
Kelas : 1A
"""
# Menghitung volume tabung dengan fungsi
r=float(input("Masukkan Jari-jari: "))
t=float(input("Masukkan Tinggi: "))
def volumeTabung(r,t):
    volume = 3.14 * r**2 * t 
    print(f"Luas volume tabung: {volume}")
    return volume
volumeTabung(r,t)