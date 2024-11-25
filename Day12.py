"""
# 1. Linear Search
Non-Determenistik
Algoritma pencarian yang paling sederhana. 
Secara berurutan memeriksa setiap elemen daftar sampai menemukan nilai target.
Langkah-langkah:
    Mulai dari elemen pertama dari daftar.
    Bandingkan setiap elemen daftar dengan nilai target.
    Jika elemen sesuai dengan nilai target, kembalikan indeksnya.
    Jika nilai target tidak ditemukan setelah iterasi melalui seluruh daftar, 
    kembalikan -1.
"""
def linear_search(arr, target):
    """
    Parameters:
        arr (list): The list to be searched.
        target: The value to be searched for.
    """
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1

# Example usage:
arr = [2, 3, 4, 10, 40]
target = 10
result = linear_search(arr, target)
if result != -1:
    print(f"Linear Search: Element found at index {result}")
else:
    print("Linear Search: Element not found")

"""
# 2. Binary Search
Determenistik
Algoritma pencarian yang lebih efisien yang cocok untuk daftar 
yang disortir. Ini berulang kali membagi interval pencarian menjadi setengah sampai nilai target ditemukan.
Langkah-langkah:
    Mulailah dengan seluruh daftar yang diurutkan.
    Mengantarkan elemen tengah dari daftar.
    Jika elemen tengah sama dengan nilai target, kembalikan indeksnya.
    Jika elemen tengah kurang dari nilai target, cari di bagian kanan daftar.
    Jika elemen tengah lebih besar dari nilai target, cari di bagian kiri daftar.
    Ulangi langkah 2-5 sampai nilai target ditemukan atau interval pencarian kosong.
"""
def binary_search(arr, target, low, high):
    """
    Parameters:
        arr (list): The sorted list to be searched.
        target: The value to be searched for.
        low (int): The lower index of the search interval.
        high (int): The upper index of the search interval.
    """
    if low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            return binary_search(arr, target, mid + 1, high)
        else:
            return binary_search(arr, target, low, mid - 1)
    else:
        return -1

# Example usage:
arr = [2, 3, 4, 10, 40]
target = 10
result = binary_search(sorted(arr), target, 0, len(arr) - 1)
if result != -1:
    print(f"Binary Search: Element found at index {result}")
else:
    print("Binary Search: Element not found")

"""
# 3. Interpolation Search
Pencarian interpolasi adalah versi pencarian biner yang ditingkatkan, terutama yang 
cocok untuk array besar dan terdistribusi secara seragam. Ini menghitung posisi 
kemungkinan nilai target berdasarkan nilai kunci dan jangkauan ruang pencarian.
Langkah-langkah:
    Menghitung kemungkinan posisi nilai target menggunakan rumus interpolasi.
    Bandingkan nilai target dengan elemen pada posisi dihitung.
    Jika elemen sesuai dengan nilai target, kembalikan indeksnya.
    Jika elemen kurang dari nilai target, cari di bagian kanan daftar.
    Jika elemen lebih besar dari nilai target, cari di bagian kiri daftar.
    Ulangi langkah 1-5 sampai nilai target ditemukan atau interval pencarian kosong.
"""
import math

def interpolation_search(arr, target):
    """
    Parameters:
        arr (list): The sorted list to be searched.
        target: The value to be searched for.
    """
    low = 0
    high = len(arr) - 1
    while low <= high and target >= arr[low] and target <= arr[high]:
        pos = low + ((high - low) // (arr[high] - arr[low])) * (target - arr[low])
        if arr[pos] == target:
            return pos
        elif arr[pos] < target:
            low = pos + 1
        else:
            high = pos - 1
    return -1

# Example usage:
arr = [2, 3, 4, 10, 40]
target = 10
result = interpolation_search(sorted(arr), target)
if result != -1:
    print(f"Interpolation Search: Element found at index {result}")
else:
    print("Interpolation Search: Element not found")

"""
4. Jump Search
Jump search adalah algoritma pencarian lain yang cocok untuk array yang disortir.
Ini melompat ke depan dengan jumlah langkah tetap dan kemudian melakukan pencarian 
linier di kisaran yang lebih kecil.
Langkah-langkah:
    Tentukan ukuran blok untuk melompat ke depan.
    Lompat ke depan dengan ukuran blok sampai nilai target lebih besar dari elemen terakhir blok saat ini.
    Lakukan pencarian linier dalam blok saat ini untuk menemukan nilai target.
    Jika nilai target ditemukan, kembalikan indeksnya.
    Jika nilai target tidak ditemukan setelah iterasi melalui semua blok, kembali -1.
"""
import math

def jump_search(arr, target):
    """
    Parameters:
        arr (list): The sorted list to be searched.
        target: The value to be searched for.
    """
    n = len(arr)
    step = int(math.sqrt(n))
    prev = 0
    while arr[min(step, n) - 1] < target:
        prev = step
        step += int(math.sqrt(n))
        if prev >= n:
            return -1
    while arr[prev] < target:
        prev += 1
        if prev == min(step, n):
            return -1
    if arr[prev] == target:
        return prev
    return -1

# Example usage:
arr = [2, 3, 4, 10, 40]
target = 10
result = jump_search(sorted(arr), target)
if result != -1:
    print(f"Jump Search: Element found at index {result}")
else:
    print("Jump Search: Element not found")