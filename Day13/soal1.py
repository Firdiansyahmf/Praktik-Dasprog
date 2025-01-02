import os

fileName = "nilai_siswa.txt"

if not os.path.exists(fileName):
    print(f"File {fileName} tidak ditemukan.")
else:
    totalNilai = 0
    jumlahSiswa = 0
    
    with open(fileName, "r") as file:
        for line in file:
            if ":" in line:
                nama, nilai = line.split(":")
                nilai = nilai.strip()

                if nilai.isdigit():
                    nilai = int(nilai)
                    totalNilai += nilai
                    jumlahSiswa += 1
                else:
                    print(f"Nilai tidak valid pada baris: {line.strip()}")
    
    if jumlahSiswa > 0:
        rataRata = totalNilai / jumlahSiswa
        print(f"Nilai rata-rata: {rataRata:.2f}")
    else:
        print("Tidak ada data siswa yang valid.")