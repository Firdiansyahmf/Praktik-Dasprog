"""
Nama : Mohamad Firdiansyah
NIM  : 2402041
Kelas : 1A
"""
def binarySearch(arr, target, kecil, besar):
    if kecil <= besar:
        tengah = (kecil + besar) // 2
        if arr[tengah] == target:
            return tengah
        elif arr[tengah] < target:
            return binarySearch(arr, target, tengah + 1, besar)
        else:
            return binarySearch(arr, target, kecil, tengah - 1)
    else:
        return -1

arr = [2, 5, 8, 12, 16, 23, 38, 56, 72, 91]
target = 23
hasil = binarySearch(sorted(arr), target, 0, len(arr) - 1)
if hasil != -1:
    print(f"Binary Search: Elemen ditemukan di index {hasil}")
else:
    print("Binary Search: Elemen tidak ditemukan")