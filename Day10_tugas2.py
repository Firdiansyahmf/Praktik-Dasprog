"""
Nama : Mohamad Firdiansyah
NIM  : 2402041
Kelas : 1A
"""
import numpy as np
arrNilai = np.array([80,80,80,80,80,90,90,90,90,90,85,85,85,85,85,82,82,82,82,82,91,92,93,94,95,96,97,98,99,100])
arrNilaiSortBesarKecil = arrNilai[::-1] # [start:stop:step]
print(f"Nilai ujian 30 orang : {arrNilaiSortBesarKecil}")
print(f"5 Nilai terbesar : {arrNilaiSortBesarKecil[0:5]}")