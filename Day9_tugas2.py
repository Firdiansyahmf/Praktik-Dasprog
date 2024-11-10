"""
Nama : Mohamad Firdiansyah
NIM  : 2402041
Kelas : 1A
"""
# Program login 3 kesempatan
def login():
    paswBenar="Latihan"
    maxCoba=3
    print("~~~ Menu Login ~~~")
    print("username : Daspro2023")
    for coba in range(maxCoba):
        pasw=input("password : ")
        if pasw==paswBenar:
            print("Login berhasil!")
            return
        else:
            print("password salah. Coba lagi.")
            if coba==maxCoba-1:
                print("Anda telah mencoba 3x\n~~~ Keluar dari menu login ~~~")
login()