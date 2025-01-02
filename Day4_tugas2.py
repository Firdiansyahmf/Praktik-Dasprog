"""
Nama : Mohamad Firdiansyah
NIM  : 2402041
Kelas : 1A
"""
# Diketahui:
students = {
    "Alice": "Computer Science",
    "Bob": "Mathematics",
    "Charlie": "Physics",
    "David": "Computer Science",
    "Eva": "Mathematics"
}
# Membuat variable list benama majors yang berisikan values dari dictionary students
majors = list(students.values())
# Membuat variable betipe int dengan fungsi count() untuk menyimpan jumlah tiap majorsnya
computerScience = majors.count("Computer Science")
mathematics = majors.count("Mathematics")
physics = majors.count("Physics")
# Menampilkan output
print(f"prodi computer science sebanyak {computerScience}")
print(f"prodi mathematics sebanyak {mathematics}")
print(f"prodi physics sebanyak {physics}")