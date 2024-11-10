"""
Nama : Mohamad Firdiansyah
NIM  : 2402041
Kelas : 1A
"""
# Perogram memprediksi untuk menjadi model catwalk
jenis_kelamin = input("Masukkan Jenis Kelamin (Wanita/Pria): ")
umur = int(input("Masukkan umur: "))
tinggi_badan = int(input("Masukkan tinggi badan: "))
iq = int(input("Masukkan IQ: "))

if (jenis_kelamin=="Wanita"):
    if ((umur>=18 and umur<=25) and tinggi_badan==170 and iq >=130):
        print("Anda dapat menjadi seorang model catwalk")
    elif ((not(umur>=18 and umur<=25)) and tinggi_badan==170 and iq>=130):
        print("Anda tidak dapat menjadi seorang model catwalk, karena umur anda bukan 18-25")
    elif ((umur>=18 and umur<=25) and tinggi_badan!=170 and iq>=130):
        print("Anda tidak dapat menjadi seorang model catwalk, karena tinggi badan anda bukan 170")
    elif ((umur>=18 and umur<=25)) and tinggi_badan==170 and not(iq>=130):
        print("Anda tidak dapat menjadi seorang model catwalk, karena IQ anda tidak memenuhi minimal yaitu 130")
    else:
        print("Anda tidak dapat menjadi seorang model catwalk, karena tidak memenuhi beberapa ketentuan")
elif (jenis_kelamin=="Pria"):
    if ((umur>=18 and umur<=25) and tinggi_badan==175 and iq >=130):
        print("Anda dapat menjadi seorang model catwalk")
    elif ((not(umur>=18 and umur <= 25)) and tinggi_badan==170 and iq>=130):
        print("Anda tidak dapat menjadi seorang model catwalk, karena umur anda bukan 18-25")
    elif ((umur>=18 and umur<=25) and tinggi_badan!=175 and iq>=130):
        print("Anda tidak dapat menjadi seorang model catwalk, karena tinggi badan anda bukan 175")
    elif ((umur>=18 and umur<=25)) and tinggi_badan==175 and not(iq>=130):
        print("Anda tidak dapat menjadi seorang model catwalk, karena IQ anda tidak memenuhi minimal yaitu 130")
    else:
        print("Anda tidak dapat menjadi seorang model catwalk, karena tidak memenuhi beberapa ketentuan")
else:
    print("Masukkan Jenis Kelamin yang valid (Wanita/Pria)")