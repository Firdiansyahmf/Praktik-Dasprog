"""
Nama : Mohamad Firdiansyah
NIM  : 2402041
Kelas : 1A
"""
# Deret Fibonacci dengan fungsi sebanyak N dari user input
def fibonacci(n):
    listVar = []
    a1, a2 = 0, 1
    for _ in range(n + 1): 
        listVar.append(a1)
        a1, a2 = a2, a1+a2
    return listVar

fn = input("Masukkan jumlah suku deret Fibonacci: ")
if fn.isdigit():
    fn = int(fn)
    deret = fibonacci(fn)
    print("n\tF(n)")
    for index in range(fn+1):
        print(f"{index}\t{deret[index]}")
else:
    print("Input tidak valid")