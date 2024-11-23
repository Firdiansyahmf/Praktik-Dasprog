import time
startTime = time.time()

def countingSort(arr):
    n = len(arr)
    if n == 0:
        return arr  
    k = max(arr)
    count = [0] * (k + 1)
    output = [0] * n
    for i in range(n):
        count[arr[i]] += 1
    for i in range(1, k + 1):
        count[i] += count[i - 1]
    for i in range(n - 1, -1, -1):
        output[count[arr[i]] - 1] = arr[i]
        count[arr[i]] -= 1
    return output

arrData =  [7, 1, 36, 26, 63, 93, 55, 16, 19, 38, 74, 65, 18, 59, 8, 43, 24, 79, 49, 35, 23, 78, 51, 2, 46, 28, 60, 76, 10, 85, 66, 29, 82, 58, 69, 75, 48, 100, 5, 32, 40, 33, 34, 90, 81, 42, 57, 44, 41, 77]
print("Sebelum sorting\t:", arrData)
print("Setelah sorting\t:", countingSort(arrData))
endTime = time.time()
print(f"Waktu eksekusi\t: {endTime - startTime:.6f} detik")