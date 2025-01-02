"""
Nama : Mohamad Firdiansyah
NIM  : 2402041
Kelas : 1A
"""
# Diketahui:
student_info = {
    "Alice": {"age": 20, "major": "Computer Science"},
    "Bob": {"age": 21, "major": "Mathematics"},
    "Charlie": {"age": 19, "major": "Physics"},
}
# Dijawab:
nama = input("Inputkan nama siswa: ")
data_siswa = student_info.get(nama)
print(f"Umur {nama} adalah {data_siswa["age"]} dan Prodi nya adalah {data_siswa["major"]}")