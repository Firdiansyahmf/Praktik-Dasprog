"""
Nama : Mohamad Firdiansyah
NIM  : 2402041
Kelas : 1A
"""
# Program pengecekan nilai
nilai = int(input("Masukkan nilai: "))
if (nilai>=90):
    print("Nilai adalah A")
elif (nilai>=80 and nilai<90):
    print("Nilai adalah B")
elif (nilai>=70 and nilai<80):
    print("Nilai adalah C")
else:
    print("Nilai adalah D")
