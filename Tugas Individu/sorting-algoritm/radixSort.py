import time
startTime = time.time()

def sortByPlace(arr, place):
    size = len(arr)
    output = [0] * size
    count = [0] * 10
    for num in arr:
        index = (num // place) % 10
        count[index] += 1
    for i in range(1, 10):
        count[i] += count[i - 1]
    for i in range (size - 1, -1, -1):
        index = (arr[i] // place) % 10
        output[count[index] - 1] = arr[i]
        count[index] -= 1
    for i in range(size):
        arr[i] = output[i]

def radixSort(arr):
    maxNum = max(arr)
    place = 1
    while maxNum // place > 0:
        sortByPlace(arr, place)
        place *= 10

arrData =  [7, 1, 36, 26, 63, 93, 55, 16, 19, 38, 74, 65, 18, 59, 8, 43, 24, 79, 49, 35, 23, 78, 51, 2, 46, 28, 60, 76, 10, 85, 66, 29, 82, 58, 69, 75, 48, 100, 5, 32, 40, 33, 34, 90, 81, 42, 57, 44, 41, 77]
print("Sebelum sorting\t:", arrData)
print("Setelah sorting\t:", radixSort(arrData))
endTime = time.time()
print(f"Waktu eksekusi\t: {endTime - startTime:.6f} detik")