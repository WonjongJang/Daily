


arr = [1, 2, 3, 4, 5, 6]

for i in range(len(arr)-1):
    min = i
    for j in range(i, len(arr)):
        if arr[min] > arr[j]:
            min = j
    arr[i], arr[min] = arr[min], arr[i]

print(arr[3])