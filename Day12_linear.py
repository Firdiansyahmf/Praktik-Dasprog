"""
Nama : Mohamad Firdiansyah
NIM  : 2402041
Kelas : 1A
"""
def linearSearch(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1

arr = [10, 15, 30, 70, 80, 60, 20, 90, 40]
target = 20
hasil = linearSearch(arr, target)
if hasil != -1:
    print(f"Linear Search: Elemen diukan di index {hasil}")
else:
    print("Linear Search: Elemen tidak diukan")