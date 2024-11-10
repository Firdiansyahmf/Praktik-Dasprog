#Flowchart Ganjil-Genap
angka = int(input("Masukkan Angka: "))
if angka % 2 == 0:
    print("Genap")
else:
    print("Ganjil")

#Mengenal Index pada string
print("Mencari karakter dimulai dari awal atau 0")
kata_1 = input("Masukkan Kata: ")
print(kata_1[0])

print("Mencari karakter dimulai dari akhir atau -1")
kata_2 = input("Masukkan Kata: ")
print(kata_2[-1])