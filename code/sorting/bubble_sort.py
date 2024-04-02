def sort(arr):
    for i in range(len(arr)):
        for j in range(len(arr)-i-1):
            if arr[j] > arr[j+1]:
                tmp = arr[j]
                arr[j] = arr[j+1]
                arr[j+1] = tmp
    print(arr)

arr = [6, 3, 8, 7, 6, 5, 8, 0, 0, 3]
sort(arr)
arr = [8, 8, 4, 0, 7, 2, 5, 4, 9, 2]
sort(arr)