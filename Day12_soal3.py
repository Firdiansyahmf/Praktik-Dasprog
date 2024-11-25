"""
Nama : Mohamad Firdiansyah
NIM  : 2402041
Kelas : 1A
"""
# Linear Search VS Binary Search
import time

# Linear Search
startTimeLinear = time.time()
def linearSearch(array, target):
    for i in range(len(array)):
        if array[i] == target:
            return i
    return -1
array = [
    1, 2, 5, 7, 8, 10, 16, 18, 19, 23, 
    24, 26, 28, 29, 32, 33, 34, 35, 36, 
    38, 40, 41, 42, 43, 44, 46, 48, 49, 
    51, 55, 57, 58, 59, 60, 63, 65, 66, 
    69, 74, 75, 76, 77, 78, 79, 81, 82, 
    85, 90, 93, 100
]
target = 60
hasil = linearSearch(array, target)
if hasil != -1:
    print(f"Linear Search: Elemen ditemukan di index {hasil}")
else:
    print("Linear Search: Elemen tidak ditemukan")

endTimeLinear = time.time()
print(f"Waktu eksekusi Linear Search\t: {endTimeLinear - startTimeLinear:.6f} detik\n")

# Binary Search
startTimeBinary = time.time()
def binarySearch(array, target, kecil, besar):
    if kecil <= besar:
        tengah = (kecil + besar) // 2
        if array[tengah] == target:
            return tengah
        elif array[tengah] < target:
            return binarySearch(array, target, tengah + 1, besar)
        else:
            return binarySearch(array, target, kecil, tengah - 1)
    else:
        return -1
array = [
    1, 2, 5, 7, 8, 10, 16, 18, 19, 23, 
    24, 26, 28, 29, 32, 33, 34, 35, 36, 
    38, 40, 41, 42, 43, 44, 46, 48, 49, 
    51, 55, 57, 58, 59, 60, 63, 65, 66, 
    69, 74, 75, 76, 77, 78, 79, 81, 82, 
    85, 90, 93, 100
]
target = 60
hasil = binarySearch(sorted(array), target, 0, len(array) - 1)
if hasil != -1:
    print(f"Binary Search: Elemen ditemukan di index {hasil}")
else:
    print("Binary Search: Elemen tidak ditemukan")
endTimeBinary = time.time()
print(f"Waktu eksekusi Binary Search\t: {endTimeBinary - startTimeBinary:.6f} detik\n")

# Perbandingan kecepatan
if (endTimeLinear - startTimeLinear) < (endTimeBinary - startTimeBinary):
    print("Linear Search lebih cepat dibandingkan Binary Search")
else:
    print("Binary Search lebih cepat dibandingkan Linear Search")
