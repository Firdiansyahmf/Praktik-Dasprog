import time
startTime = time.time()

def quickSort(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[0]
        left = [x for x in arr[1:] if x <= pivot]
        right = [x for x in arr[1:] if x > pivot]
        return quickSort(left) + [pivot] + quickSort(right)
    
arrData =  [7, 1, 36, 26, 63, 93, 55, 16, 19, 38, 74, 65, 18, 59, 8, 43, 24, 79, 49, 35, 23, 78, 51, 2, 46, 28, 60, 76, 10, 85, 66, 29, 82, 58, 69, 75, 48, 100, 5, 32, 40, 33, 34, 90, 81, 42, 57, 44, 41, 77]
print("Sebelum sorting\t:", arrData)
print("Setelah sorting\t:", quickSort(arrData))
endTime = time.time()
print(f"Waktu eksekusi\t: {endTime - startTime:.6f} detik")